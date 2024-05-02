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
    
    def downloadAudio(self,path,selection):
        self.downloader.downloadAudio(path, selection, self.data.videoData)

    def removeVideo(self,indexVideoToRemove):
        self.data.removeVideo(indexVideoToRemove)
