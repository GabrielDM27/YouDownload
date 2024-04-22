from abc import ABC, abstractmethod

class IFetching(ABC):
    @abstractmethod
    def fetchContent(self,url):
        pass