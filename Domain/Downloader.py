from pytube import YouTube
from Util.RemoveIllegalCharacter import RemoveIllegalCharacter

class Downloader:
    def __init__(self) -> None:
        pass

    def getSelection(self,selection:tuple,videoData:list[YouTube]):
        videoToDownload=[]
        if selection:
            for index in selection :
                videoToDownload.append(videoData[index])
        else:
            videoToDownload=videoData

        return videoToDownload

    def downloadAudio(self, path, selection:tuple, videoData:list[YouTube]):
        videosToDownload = self.getSelection(selection, videoData)
        for video in videosToDownload :
            stream = video.streams
            validName = RemoveIllegalCharacter.windowsFileExplorer(video.title)
            
            stream.get_audio_only().download(output_path= path,filename= validName +".mp3",skip_existing=False)
