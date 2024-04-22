from Domain.IFetching import IFetching
from pytube import YouTube

class FetchingVideo(IFetching):
    def __fetchVideo(self,url:str):
        return YouTube(url)

    def fetchContent(self,url):
        fetchedVideo=[]
        video = self.__fetchVideo(url)
        fetchedVideo.append(video)
            
        return fetchedVideo
    
