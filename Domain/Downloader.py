from pytube import YouTube
from Util.RemoveIllegalCharacter import RemoveIllegalCharacter

class Downloader:
    def __init__(self) -> None:
        self.activeDownload=0
        self.totalDownload=0

    def downloadAudio(self, path, video:YouTube):
        stream = video.streams
        validName = RemoveIllegalCharacter.windowsFileExplorer(video.title)
        stream.get_audio_only().download(output_path= path,filename= validName +".mp3",skip_existing=False)

    def updateProgress(self):
        pass