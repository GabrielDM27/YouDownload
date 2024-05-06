from Domain.Downloader import Downloader
from Domain.Fetcher import Fetcher
from Domain.Data import Data

class DomainController:

    def __init__(self) -> None:
        self.data = Data()
        self.fetcher = Fetcher()
        self.downloader = Downloader()

    def printTitle(self):
        self.data.printTitle()

    def fetchContent(self,url:str):
        self.fetcher.fetchContent(self.data,url)
    
    def getVideoTitles(self):
        return self.data.getVideoTitles()
    
    def downloadAudio(self,path,index):
        self.downloader.downloadAudio(path, self.data, index)


    def removeVideo(self,indexVideoToRemove):
        self.data.removeVideo(indexVideoToRemove)

    def cancelDownload(self):
        self.downloader.cancelDownload()
