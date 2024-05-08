from typing import List
from Domain.Downloader import Downloader
from Domain.Fetcher import Fetcher
from Domain.Data import Data
from Util.DownloadStatus import DownloadStatus
from Util.IDownloadProgressSubscriber import IDownloadProgressSubscriber


class DomainController:

    def __init__(self) -> None:
        self.data = Data()
        self.fetcher = Fetcher()
        self.downloader = Downloader()
        self.downloadProgressSubscribers:List[IDownloadProgressSubscriber]=[]

    def printTitle(self):
        self.data.printTitle()

    def fetchContent(self,url:str,index:int=None):
        self.fetcher.fetchContent(self.data,url,index)
    
    def getVideoTitles(self):
        return self.data.getVideoTitles()
    
    def downloadAudio(self,path,selection):
        self.downloader.setSelectionDownload(selection)
        for index in selection:
            self.downloader.setActiveDownload(path, self.data.videoData[index])
            self.downloader.activeNbOfDownload+=1
            self.publishDownloadProgress()
            if (self.downloader.downloadStatus == DownloadStatus.CANCELLED):
                break
            maxTry = 4
            for nbOfTry in range(0,maxTry+1):
                self.downloader.downloadAudio()
                if (self.downloader.downloadStatus == DownloadStatus.COMPLETED
                    or self.downloader.downloadStatus == DownloadStatus.CANCELLED) :
                    break
                elif (nbOfTry < maxTry):#Refetch the content that failed downloading for retry
                    self.fetchContent(self.downloader.activeYoutubeVideo.watch_url,index)
                    self.downloader.setActiveDownload(path,self.data.videoData[index])
                else: 
                    raise Exception(f"Error while downloading : \n{self.downloader.activeYoutubeVideo.title}")


    def removeVideo(self,indexVideoToRemove):
        self.data.removeVideo(indexVideoToRemove)

    def cancelDownload(self):
        self.downloader.cancelDownload()

    def subscribeToDownloadProgress(self,subscriber:IDownloadProgressSubscriber):
        self.downloadProgressSubscribers.append(subscriber)

    def removeSubscriberToDownloadProgress(self,subscriber:IDownloadProgressSubscriber):
        self.downloadProgressSubscribers.remove(subscriber)

    def publishDownloadProgress(self):
        for subscriber in self.downloadProgressSubscribers:
            subscriber.updateDownloadProgress()

    def refetchVideo(self):
        self.fetchContent(self.downloader.activeYoutubeVideo.watch_url, self.downloader.activeNbOfDownload-1)
        self.downloader.activeYoutubeVideo = self.data.videoData[self.downloader.activeNbOfDownload-1]
