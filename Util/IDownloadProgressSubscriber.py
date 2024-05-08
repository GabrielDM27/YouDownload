from abc import ABC, abstractmethod

class IDownloadProgressSubscriber(ABC):
    @abstractmethod
    def updateDownloadProgress(self):
        pass
