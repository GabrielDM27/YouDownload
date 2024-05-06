from pytube import YouTube, request
from Domain.FetchingVideoInError import FetchingVideoInError
from Util.RemoveIllegalCharacter import RemoveIllegalCharacter
from Domain.Data import Data
import os
import time

class Downloader:
    def __init__(self) -> None:
        self.activeDownloadPath=""
        self.downloadProgress=0
        self.totalDownloadSize=0
        self.isDownloading=False
        self.isCancelled=False

    def writeStreamToFile(self,path,stream):
        iterableStream = request.stream(stream.url)
        with open(path, "wb") as file :
            while (self.isDownloading and not(self.isCancelled)):
                streamChunk = next(iterableStream,None)
                if(streamChunk):
                    file.write(streamChunk)
                else:
                    self.isDownloading=False
                    break  
    
    def __downloadAudio(self, path, data:Data, index:int):
        video:YouTube = data.videoData[index]
        validName = RemoveIllegalCharacter.windowsFileExplorer(video.title)
        self.activeDownloadPath= path+"\\"+ validName + ".mp3"
        self.isDownloading=True
        self.isCancelled=False
        audioStream = video.streams.get_audio_only()
        self.writeStreamToFile(self.activeDownloadPath, audioStream)

    def downloadAudio(self, path, data:Data, index:int):
        for nbOfTry in range(0,4):
            try:
                self.__downloadAudio(path,data,index)
                return
            except:#If an error occured during download, retry after refetching the content
                FetchingVideoInError.refetchContent(data,index)
                time.sleep(1)

        raise Exception(f"Error while downloading : \n{data.videoData[index].title}")


    def deleteCanceledFile(self):
        if os.path.isfile(self.activeDownloadPath):
            os.remove(self.activeDownloadPath)

    def cancelDownload(self):
        self.isCancelled=True
        self.deleteCanceledFile()

    def updateProgress(self):
        pass