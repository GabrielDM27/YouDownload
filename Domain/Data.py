import array as arr
from ast import List
from pytube import YouTube

class Data:
    def __init__(self) -> None:
        self.videoData:List[YouTube]=[]

    def clearVideoData(self):
        self.videoData.clear()
    
    def addVideo(self,video:YouTube, index:int=None):
        if index :
            self.videoData[index] = video
        else:
            self.videoData.append(YouTube)

    def printVideoData(self):
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

       

