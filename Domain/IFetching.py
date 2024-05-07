from abc import ABC, abstractmethod
from Domain.Data import Data

class IFetching(ABC):
    @abstractmethod
    def fetchContent(self,data:Data,url:str,index:int=None):
        pass