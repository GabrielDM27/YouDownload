from Domain.Data import Data
from pytube import YouTube

class FetchingVideoInError():
    @staticmethod
    def refetchContent(data:Data,index:int):
        test:YouTube = data.videoData[index]
        url = test.watch_url
        data.videoData[index] = YouTube(url)
    
