from pytube import Youtube
from abc import ABC, abstractmethod

class Downloader:
    @abstractmethod
    def download(self):
        pass