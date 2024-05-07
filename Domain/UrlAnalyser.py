from Util.UrlType import UrlType

class UrlAnalyser :
    def determineType(self,url):
        if 'list=' in url:
            return UrlType.PLAYLIST
        elif 'watch?v=' in url :
            return UrlType.VIDEO
        elif 'redo=' in url :
            return UrlType.REFETCH