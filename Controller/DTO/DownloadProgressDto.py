from Domain.Downloader import Downloader

class DownloadProgressDto :
    def __init__(self,downloader:Downloader) -> None:
        self.videoTitle = downloader.activeYoutubeVideo.title
        self.downloadStatus = downloader.downloadStatus
        self.downloadProgressStep = downloader.downloadProgressStep
        self.activeNbOfDownload = downloader.activeNbOfDownload
        self.totalNumberOfDownload = downloader.totalNumberOfDownload