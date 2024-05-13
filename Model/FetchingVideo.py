from Model.IFetching import IFetching
from Model.Data import Data
from pytube import YouTube

class FetchingVideo(IFetching):
    def __fetchVideo(self,url:str):
        return YouTube(url)

    def fetchContent(self,data:Data,url:str,index:int=None):
        video = self.__fetchVideo(url)
        if index :
            data.videoData[index] = video
        else:
            data.clearVideoData()
            data.videoData.append(video)
            
    
