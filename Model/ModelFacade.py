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
    
    def downloadVideo(self,path,selection,videoQualityIndex):
        self.downloader.downloadVideoSelection(self.data,self.fetcher,path,selection,videoQualityIndex)

    def removeVideo(self,indexVideoToRemove):
        self.data.removeVideo(indexVideoToRemove)

    def cancelDownload(self):
        self.downloader.cancelDownload()

    def subscribeToDownloadProgress(self,subscriber:IDownloadProgressSubscriber):
        self.downloader.subscribeToDownloadProgress(subscriber)

    def removeSubscriberToDownloadProgress(self,subscriber:IDownloadProgressSubscriber):
        self.downloader.removeSubscriberToDownloadProgress(subscriber)
