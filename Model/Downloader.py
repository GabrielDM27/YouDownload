from ast import List, Mod, Tuple
from pytube import YouTube, request
import Model.Data as Data
import Model.Fetcher as Fetcher
from Util.DownloadStatus import DownloadStatus
from Util.IDownloadProgressSubscriber import IDownloadProgressSubscriber
from Util.RemoveIllegalCharacter import RemoveIllegalCharacter
import os
import time

class Downloader:
    def __init__(self) -> None:
        self.activeDownloadPath=""
        self.activeYoutubeVideo:YouTube=None
        self.downloadStatus:DownloadStatus=DownloadStatus.DOWNLOADING
        self.downloadProgressStep=0
        self.activeNbOfDownload=0
        self.totalNumberOfDownload=0
        self.downloadProgressSubscribers:List[IDownloadProgressSubscriber]=[]
        

    def writeStreamToFile(self, stream):
        iterableStream = request.stream(stream.url)
        with open(self.activeDownloadPath, "wb") as file :
            while (self.downloadStatus == DownloadStatus.DOWNLOADING):
                if(self.downloadStatus == DownloadStatus.CANCELLED):
                    break
                streamChunk = next(iterableStream,None)
                if(streamChunk):
                    file.write(streamChunk)
                else:
                    break  

    def setSelectionDownload(self, selection:Tuple):
        self.downloadStatus=DownloadStatus.DOWNLOADING
        self.activeNbOfDownload=0
        self.totalNumberOfDownload = len(selection)
        self.downloadProgressStep = 1/self.totalNumberOfDownload*100

    def setActiveDownload(self,data:Data.Data,path:str,index:int):
            self.activeYoutubeVideo = data.videoData[index]
            validName = RemoveIllegalCharacter.windowsFileExplorer(self.activeYoutubeVideo.title)
            self.activeDownloadPath= path+"/"+ validName + ".mp3"

    def downloadAudio(self,data:Data.Data,fetcher:Fetcher.Fetcher,path:str,index:int):
        maxNbOfTry = 4
        for nbOfTry in range(0,maxNbOfTry+1):
            try:
                audioStream = self.activeYoutubeVideo.streams.get_audio_only()
                self.writeStreamToFile(audioStream)
                break
            except Exception as e :#If an error occured during download, retry after refetching the content
                print(str(e))
                if nbOfTry == maxNbOfTry:
                    self.downloadStatus=DownloadStatus.ERROR
                else:
                    fetcher.fetchContent(self.activeYoutubeVideo.watch_url,index)
                    self.setActiveDownload(data,path,index)
                    time.sleep(1)

    def downloadCompleted(self):
        self.activeDownloadPath=""
        self.activeYoutubeVideo=None
        self.downloadStatus = DownloadStatus.COMPLETED

    def downloadAudioSelection(self,data:Data.Data,fetcher:Fetcher.Fetcher,path,selection:Tuple):
        self.setSelectionDownload(selection)
        for index in selection:
            self.activeNbOfDownload+=1
            self.setActiveDownload(data,path,index)
            self.publishDownloadProgress()
            self.downloadAudio(data,fetcher,path,index)
            if(self.downloadStatus != DownloadStatus.DOWNLOADING):
                break

        if(self.downloadStatus == DownloadStatus.DOWNLOADING):    
            self.downloadCompleted()
        if(self.downloadStatus == DownloadStatus.CANCELLED):
            if os.path.isfile(self.activeDownloadPath):
                os.remove(self.activeDownloadPath)

        self.publishDownloadProgress()

    def cancelDownload(self):
        self.downloadStatus=DownloadStatus.CANCELLED

    def subscribeToDownloadProgress(self,subscriber:IDownloadProgressSubscriber):
        self.downloadProgressSubscribers.append(subscriber)

    def removeSubscriberToDownloadProgress(self,subscriber:IDownloadProgressSubscriber):
        self.downloadProgressSubscribers.remove(subscriber)

    def publishDownloadProgress(self):
        for subscriber in self.downloadProgressSubscribers:
            subscriber.updateDownloadProgress()

