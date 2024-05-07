from enum import Enum

class DownloadStatus(Enum):
    DOWNLOADING=1
    COMPLETED=2
    CANCELLED=3
    ERROR=4