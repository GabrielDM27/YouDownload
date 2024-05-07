from Domain.Downloader import Downloader
from Domain.Fetcher import Fetcher
from Domain.Data import Data
from Util.IDownloadProgressSubscriber import IDownloadProgressSubscriber


class DomainController:

    def __init__(self) -> None:
        self.data = Data()
        self.fetcher = Fetcher()
        self.downloader = Downloader(self)

    def printTitle(self):
        self.data.printTitle()

    def fetchContent(self,url:str,index:int=None):
        self.fetcher.fetchContent(self.data,url,index)
    
    def getVideoTitles(self):
        return self.data.getVideoTitles()
    
    def downloadAudio(self,path,selection):
        self.downloader.downloadAudioSelection(path,self.data,selection)

    def removeVideo(self,indexVideoToRemove):
        self.data.removeVideo(indexVideoToRemove)

    def cancelDownload(self):
        self.downloader.cancelDownload()

    def subscribeToDownloadProgress(self,subscriber:IDownloadProgressSubscriber):
        self.downloader.addSubscriber(subscriber)

    def refetchVideo(self):
        self.fetchContent(self.downloader.activeYoutubeVideo.watch_url, self.downloader.activeNbOfDownload-1)
        self.downloader.activeYoutubeVideo = self.data.videoData[self.downloader.activeNbOfDownload-1]
