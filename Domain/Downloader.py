from ast import List, Tuple
from pytube import YouTube, request
from Util.DownloadStatus import DownloadStatus
from Util.IDownloadProgressSubscriber import IDownloadProgressSubscriber
from Util.RemoveIllegalCharacter import RemoveIllegalCharacter
from Domain.Data import Data
import os
import time

class Downloader:
    def __init__(self) -> None:
        self.activeDownloadPath=""
        self.activeYoutubeVideo:YouTube
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
                    self.downloadStatus = DownloadStatus.COMPLETED
                    break  

    def setSelectionDownload(self, selection:Tuple):
        self.activeNbOfDownload=0
        self.totalNumberOfDownload = len(selection)
        self.downloadProgressStep = 1/self.totalNumberOfDownload
        self.downloadStatus = DownloadStatus.DOWNLOADING

    def setActiveDownload(self,path:str,activeVideo:YouTube):
            self.activeYoutubeVideo = activeVideo
            validName = RemoveIllegalCharacter.windowsFileExplorer(self.activeYoutubeVideo.title)
            self.activeDownloadPath= path+"/"+ validName + ".mp3"

    def downloadAudio(self):
        try:
            self.downloadStatus=DownloadStatus.DOWNLOADING
            audioStream = self.activeYoutubeVideo.streams.get_audio_only()
            self.writeStreamToFile(audioStream)
        except Exception as e :#If an error occured during download, retry after refetching the content
            print(str(e))
            self.downloadStatus=DownloadStatus.ERROR
            time.sleep(1)

        

    def downloadAudioSelection(self,path,data:Data,selection:Tuple):
        self.totalNumberOfDownload = len(selection)
        self.downloadProgressStep = 1/self.totalNumberOfDownload*100

        for index in selection:
            self.activeNbOfDownload+=1
            self.activeYoutubeVideo:YouTube = data.videoData[index]
            validName = RemoveIllegalCharacter.windowsFileExplorer(self.activeYoutubeVideo.title)
            self.activeDownloadPath= path+"/"+ validName + ".mp3"
            self.downloadAudio()

    def deleteCanceledFile(self):
        if os.path.isfile(self.activeDownloadPath):
            os.remove(self.activeDownloadPath)

    def cancelDownload(self):
        self.downloadStatus=DownloadStatus.CANCELLED
        self.deleteCanceledFile()

