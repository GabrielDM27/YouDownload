import array as arr
from pytube import YouTube
class Data:
    def __init__(self) -> None:
        self.videoData = []

    def clearVideoData(self):
        self.videoData.clear()

    def printVideoData(self):
        for video in self.videoData :
            print(video.title)
    
    def getVideoTitles(self):
        videoTitles = []
        for video in self.videoData :
            videoTitles.append(video.title)
        return videoTitles

