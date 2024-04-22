from Domain.IFetching import IFetching
from pytube import Playlist

class FetchingPlaylist(IFetching):
    def __fetchPlaylist(self,url:str):
        return Playlist(url)

    def fetchContent(self,url):
        fetchedVideos=[]
        playlist = self.__fetchPlaylist(url)
        if playlist:
            for video in playlist.videos :
                fetchedVideos.append(video)
        else:
            raise Exception("Cannot fetch the playlist. \n\nMake sure the playlist is not private or autogenerated.")

        return fetchedVideos
    
