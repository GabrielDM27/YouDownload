from Domain.Fetcher import Fetcher
from Domain.Data import Data
from Domain.Context import Context

class DomainController:
    data = Data()
    context = Context()
    fetcher = Fetcher()

    def printTitle(self):
        self.data.printTitle()

    def fetchContent(self,url:str):
        self.data.clearVideoData()
        self.fetcher.fetchContent(self.data,url)
        self.data.printVideoData()
