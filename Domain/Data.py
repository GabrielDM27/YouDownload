import array as arr
from numpy import append
from pytube import YouTube
class Data:
    def __init__(self) -> None:
        self.videoData = []

    def clearVideoData(self):
        self.videoData.clear()

    def printVideoData(self):
        #TODO
        for video in self.videoData :
            print(video.title)
    
    def getVideoTitles(self):
        videoTitles=[]
        for video in self.videoData :
            videoTitles.append(video.title)

        return videoTitles
        
    def removeVideo(self,indexes:tuple):
        
        sortedIndexes = list(indexes)
        sortedIndexes.sort(reverse=True)
        for index in sortedIndexes:
            self.videoData.pop(index)

       

