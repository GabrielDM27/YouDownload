from typing import List
import Model.Downloader as Downloader
import Model.Fetcher as Fetcher
import Model.Data as Data
from Util.DownloadStatus import DownloadStatus
from Util.IDownloadProgressSubscriber import IDownloadProgressSubscriber


class ModelFacade:

    def __init__(self) -> None:
        self.data = Data.Data()
        self.fetcher = Fetcher.Fetcher()
        self.downloader = Downloader.Downloader()

    def printTitle(self):
        self.data.printTitle()

    def fetchContent(self,url:str,index:int=None):
        self.fetcher.fetchContent(self.data,url,index)
    
    def getVideoTitles(self):
        return self.data.getVideoTitles()
    
    def downloadAudio(self,path,selection):
        self.downloader.downloadAudioSelection(self.data,self.fetcher,path,selection)

    def removeVideo(self,indexVideoToRemove):
        self.data.removeVideo(indexVideoToRemove)

    def cancelDownload(self):
        self.downloader.cancelDownload()

    def subscribeToDownloadProgress(self,subscriber:IDownloadProgressSubscriber):
        self.downloader.subscribeToDownloadProgress(subscriber)

    def removeSubscriberToDownloadProgress(self,subscriber:IDownloadProgressSubscriber):
        self.downloader.removeSubscriberToDownloadProgress(subscriber)
