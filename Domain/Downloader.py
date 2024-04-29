from pytube import YouTube
from Util.RemoveIllegalCharacter import RemoveIllegalCharacter

class Downloader:
    def __init__(self) -> None:
        pass

    def downloadAudio(self,path,videoData:list[YouTube]):
        for video in videoData :
            stream = video.streams
            validName = RemoveIllegalCharacter.windowsFileExplorer(video.title)
            
            stream.get_audio_only().download(output_path= path,filename= validName +".mp3",skip_existing=False)

