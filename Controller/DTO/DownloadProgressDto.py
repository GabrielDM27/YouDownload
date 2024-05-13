import Model.Downloader as Downloader

class DownloadProgressDto :
    def __init__(self,downloader:Downloader.Downloader) -> None:
        if downloader.activeYoutubeVideo:
            self.videoTitle = downloader.activeYoutubeVideo.title
        self.downloadStatus = downloader.downloadStatus
        self.downloadProgressStep = downloader.downloadProgressStep
        self.activeNbOfDownload = downloader.activeNbOfDownload
        self.totalNumberOfDownload = downloader.totalNumberOfDownload