from pytube import Playlist,YouTube

from Domain.UrlAnalyser import UrlAnalyser
from Domain.Data import Data

class Fetcher :
    def __fetchVideo(self,url:str):
        return YouTube(url)

    def __fetchPlaylist(self,url:str):
        return Playlist(url)

    def fetchContent(self,data:Data, url:str):
        urlType = UrlAnalyser().determineType(url)

        if  urlType == "Playlist":

            playlist = self.__fetchPlaylist(url)
            if playlist:
                for video in playlist.videos :
                    data.videoData.append(video)
            else:
                print("Error")
        elif urlType == "Video":

            data.videoData.append(self.__fetchVideo(url))
        else:
            print("Error url is not a video or a playlist")

