from Domain.IFetching import IFetching
from Domain.FetchingPlaylist import FetchingPlaylist
from Domain.FetchingVideo import FetchingVideo
from Domain.UrlAnalyser import UrlAnalyser
from Domain.Data import Data
from Util.UrlType import UrlType

class Fetcher :
    def __init__(self) -> None:
        self.urlAnalyser=UrlAnalyser()
        self.fetchingStrategy:IFetching
    
    def __setStrategy(self,url:str):
        urlType = self.urlAnalyser.determineType(url)
        if  urlType == UrlType.PLAYLIST:
            self.fetchingStrategy = FetchingPlaylist()
        elif urlType == UrlType.VIDEO:
            self.fetchingStrategy = FetchingVideo()
        else:
            raise Exception("Url is not a video or a playlist")

    def fetchContent(self,data:Data, url:str):
        self.__setStrategy(url)
        data.clearVideoData()
        data.videoData = self.fetchingStrategy.fetchContent(url)


