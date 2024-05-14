from tkinter import *
from tkinter import messagebox, filedialog
import Model.ModelFacade as Model
import View.MainWindow as MainWindow
import os
import Util.IDownloadProgressSubscriber as IDownloadProgressSubscriber
from Util.DownloadStatus import DownloadStatus
from Controller.DTO.DownloadProgressDto import DownloadProgressDto
import webbrowser

class MainWindowController(IDownloadProgressSubscriber.IDownloadProgressSubscriber):
    def __init__(self,model:Model.ModelFacade, view:MainWindow.MainWindow,) -> None:
        self.model = model
        self.mainWindow = view

        self.model.subscribeToDownloadProgress(self)

        #bindButtons
        self.__buttonFetchBind()
        self.__removeVideoButtonBind()
        self.__audioDownloadButtonBind()
        self.__audioCancelButtonBind()
        self.__bannerBind()
    
    def __bannerCommand(*args):
        webbrowser.open("https://www.youtube.com/feed/playlists")

    def __bannerBind(self):
        self.mainWindow.banner.tag_bind(self.mainWindow.bannerImage,'<Button-1>',self.__bannerCommand)

    def clearListBox(self,listbox:Listbox):
        if listbox.size() > 0 :
            lastElementIndex = listbox.size()-1
            listbox.delete(0,lastElementIndex)
        self.mainWindow.theMainWindow.update()

    def updateSelectionBox(self):
        self.clearListBox(self.mainWindow.selectionBox)
        videos = self.model.getVideoTitles()
        for video in videos:
            self.mainWindow.selectionBox.insert(END,video)
        self.mainWindow.theMainWindow.update()

    def __buttonFetchCommand(self):
        try:
            self.model.fetchContent(self.mainWindow.urlEntry.get())
            self.updateSelectionBox()
            self.mainWindow.progressBar.configure(value=0)
            self.mainWindow.progressLabel.configure(text="")
            self.mainWindow.theMainWindow.update()
        except Exception as e:
            messagebox.showerror('Error',str(e))
    
    def __buttonFetchBind(self):
        self.mainWindow.buttonFetch.configure(command=self.__buttonFetchCommand)

    def __removeVideoButtonCommand(self):
        self.model.removeVideo(self.mainWindow.selectionBox.curselection())
        self.updateSelectionBox()
        self.mainWindow.progressLabel.configure(text="")
        self.mainWindow.progressBar.configure(value=0)  
        self.mainWindow.theMainWindow.update()    
    
    def __removeVideoButtonBind(self):
        self.mainWindow.removeVideoButton.configure(command=self.__removeVideoButtonCommand)

    def __audioDownloadButtonCommand(self):
        try:
            self.mainWindow.buttonFetch.configure(state='disabled')
            self.mainWindow.removeVideoButton.configure(state='disabled')
            self.mainWindow.audioDownloadButton.configure(state='disabled')
            self.mainWindow.progressBar.configure(value=0,
                                       maximum=100.001,)
            self.mainWindow.theMainWindow.update()

            if self.mainWindow.selectionBox.curselection() : #Download only the selection
                selection:tuple = self.mainWindow.selectionBox.curselection()
            else:   #If nothing is selected download everyting
                selection:tuple = range(0,self.mainWindow.selectionBox.size())

            totalNumberOfDownload=len(selection)
            if(totalNumberOfDownload > 0):
                downloadFolderDestination = filedialog.askdirectory(parent=None,
                                                                    initialdir=f"C:\\Users\\{os.getlogin()}\\Downloads",
                                                                    title="Select a folder")

                self.model.downloadAudio(downloadFolderDestination,selection)

        except Exception as e:
            messagebox.showerror('Error',str(e))

        finally:
            self.mainWindow.buttonFetch.configure(state='active')
            self.mainWindow.removeVideoButton.configure(state='active')
            self.mainWindow.audioDownloadButton.configure(state='active')
            self.mainWindow.theMainWindow.update()

    def __audioDownloadButtonBind(self):
        self.mainWindow.audioDownloadButton.configure(command=self.__audioDownloadButtonCommand)

    def __audioCancelButtonCommand(self):
        self.mainWindow.progressLabel.configure(text="Download Canceled")
        self.mainWindow.progressBar.configure(value=0)
        self.model.cancelDownload()

    def __audioCancelButtonBind(self):
        self.mainWindow.audioCancelButton.configure(command=self.__audioCancelButtonCommand)
    

    def updateDownloadProgress(self):
        downloadProgressDto = DownloadProgressDto(self.model.downloader)
        if(downloadProgressDto.downloadStatus == DownloadStatus.CANCELLED):
            self.mainWindow.progressLabel.configure(text="Download Canceled")
            self.mainWindow.progressBar.configure(value=0)

        if(downloadProgressDto.downloadStatus == DownloadStatus.DOWNLOADING):
            self.mainWindow.progressLabel.configure(text=f"Downloading ({downloadProgressDto.activeNbOfDownload}/{downloadProgressDto.totalNumberOfDownload}) :  {downloadProgressDto.videoTitle}")
            self.mainWindow.theMainWindow.update()
            self.mainWindow.progressBar.step(downloadProgressDto.downloadProgressStep)
        
        if(downloadProgressDto.downloadStatus == DownloadStatus.COMPLETED):
            self.mainWindow.progressLabel.configure(text=f"Download Completed ({downloadProgressDto.activeNbOfDownload}/{downloadProgressDto.totalNumberOfDownload})")
            self.mainWindow.theMainWindow.update()

        if(downloadProgressDto.downloadStatus == DownloadStatus.ERROR):
            self.mainWindow.progressLabel.configure(text=f"Download Failed ({downloadProgressDto.activeNbOfDownload}/{downloadProgressDto.totalNumberOfDownload}):  {downloadProgressDto.activeVideoTitle}")
            self.mainWindow.progressBar.configure(value=0)
            self.mainWindow.theMainWindow.update()