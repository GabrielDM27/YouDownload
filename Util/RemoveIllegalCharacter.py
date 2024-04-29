class RemoveIllegalCharacter():
    @staticmethod
    def windowsFileExplorer(fileName:str):

        for ch in [ '\\' ,'/', '"',':', '*','?', "'", '|','.'] :
            fileName = fileName.replace(ch,"")
        return fileName