
class UrlAnalyser :
    def determineType(self,url):
        if 'list=' in url:
            return "Playlist"
        elif 'watch?v=' in url :
            return "Video"