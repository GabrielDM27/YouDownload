from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Progressbar,Combobox
from turtle import update, width
from Domain.DomainController import DomainController
import os

from Util.FileExtention import FileExtention
from Util.RemoveIllegalCharacter import RemoveIllegalCharacter


class MainWindow:
    theMainWindow = Tk()
    domainController = DomainController()
    #Variables
    choice=StringVar()
    isCancelled=False
    
    # default constructor
    def __init__(self):
        self.theMainWindow.title("YouDownload")
        self.theMainWindow.minsize(1000,700)
        
        #Build Frames
        self.buildTopFrame()
        self.buildFetchFrame()
        self.buildSelectionFrame()
        self.buildDownloadFrame()
       
        
        #Infinite loop
        self.run()

    def buildTopFrame(self):
        self.topFrame = Frame(self.theMainWindow,
                         height=300)
        self.topFrame.pack(side='top')
        
    def buildFetchFrame(self):
        self.fetchFrame = Frame(self.theMainWindow,
                                height=100)
        self.fetchFrame.pack(side='top')
                
        self.urlFetchFrame = Frame(self.fetchFrame)
        self.urlFetchFrame.pack(side='top')
        
        self.urlLabel = Label(self.urlFetchFrame,
                         text = "Video URL : ")
        self.urlLabel.pack(side='left')
        
        self.url=StringVar()
        self.urlEntry = Entry(self.urlFetchFrame,
                         width=125,
                         textvariable=self.url)
        self.urlEntry.pack(side='left')

        self.urlChoiceVideo = Radiobutton(self.urlFetchFrame,
                                     text = 'video',
                                     value='video',
                                     variable=self.choice,
                                     command=self.choiceSelected)
        self.urlChoiceVideo.pack(side='left')
        self.urlChoiceVideo.select()
        
        self.urlChoicePlaylist = Radiobutton(self.urlFetchFrame,
                                        text = 'playlist',
                                        value='playlist',
                                        variable=self.choice,
                                        command=self.choiceSelected)
        self.urlChoicePlaylist.pack(side='left')
        
        self.btnFetchFrame = Frame(self.fetchFrame,
                              height=100)
        self.btnFetchFrame.pack(side='top')
        self.buttonFetch = Button(self.btnFetchFrame,
                            text = "Fetch",
                            command=self.fetchButtonClicked)
        self.buttonFetch.pack(side='left')

    def buildSelectionFrame(self):
        
        self.selectionFrame = Frame(self.theMainWindow)
        self.selectionFrame.pack(side='top')
        self.audioSelectionFrame = Frame(self.selectionFrame,
                                         name = 'audioSelectionFrame')
        self.audioSelectionFrame.pack(side='top')
        
        scrollbar = Scrollbar(self.audioSelectionFrame,orient='vertical')
        scrollbar.pack(side='right',fill='y')

        self.selectionBox = Listbox(self.audioSelectionFrame,selectmode='extended',width=100,height=10)
        self.selectionBox.pack(side='left')

        scrollbar.config(command=self.selectionBox.yview)
        self.selectionBox.config(yscrollcommand=scrollbar.set)

        self.videoQualityFrame = Frame(self.selectionFrame)
        self.videoQualityFrame.pack(side='top',ipadx=100)

        self.videoQualityLabel = Label(self.videoQualityFrame,text='Maximum video quality : ')
        self.videoQualityLabel.pack(side='left')

        self.videoQualityChoice = Combobox(self.videoQualityFrame,state='readonly')
        self.videoQualityChoice.pack(side='left')

        self.removeVideoButton = Button(self.videoQualityFrame,
                                        text = 'Remove Selected Video',
                                        command = self.removeSelectedVideo)
        self.removeVideoButton.pack(side='right')        

    def buildDownloadFrame(self):
        self.downloadFrame = Frame(self.theMainWindow)
        self.downloadFrame.pack(side='bottom',
                            fill='both',
                            expand='true')  
        
        self.audioDownloadFrame = Frame(self.downloadFrame)
        self.audioDownloadFrame.pack(side='top')

        self.audioDownloadButton = Button(self.audioDownloadFrame,
                                          text='Download',
                                          width=10,
                                          command=self.downloadAudio
                                          )
        self.audioDownloadButton.pack(side='left')
        self.audioCancelButton = Button(self.audioDownloadFrame,
                                        text='Cancel',
                                        width=10,
                                        command=self.cancelDownload)
        self.audioCancelButton.pack(side='left',padx=(10,0))
        
        self.progressFrame = Frame(self.downloadFrame)
        self.progressFrame.pack(side='top')

        self.progressLabel=Label(self.progressFrame,
                                 text="")
        self.progressLabel.pack(side='top')

        self.progressBar=Progressbar(self.progressFrame,
                                     length=400,
                                     maximum=100)
        self.progressBar.pack()

          

    def fetchButtonClicked(self):
        try:
            self.domainController.fetchContent(self.urlEntry.get())
            self.updateSelectionBox()
            self.progressBar.configure(value=0)
            self.progressLabel.configure(text="")
            self.theMainWindow.update()
        except Exception as e:
            messagebox.showerror('Error',str(e))

    def downloadAudio(self):
        self.isCancelled=False
        try:
            self.buttonFetch.configure(state='disabled')
            self.removeVideoButton.configure(state='disabled')
            self.audioDownloadButton.configure(state='disabled')
            self.progressBar.configure(value=0,
                                       maximum=100.001,)
            self.theMainWindow.update()


            if self.selectionBox.curselection() : #Download only the selection
                selection:tuple = self.selectionBox.curselection()
            else:   #If nothing is selected download everyting
                selection:tuple = range(0,self.selectionBox.size())

            totalNumberOfDownload=len(selection)
            if(totalNumberOfDownload > 0):
                downloadFolderDestination = filedialog.askdirectory(parent=None,
                                                                    initialdir=f"C:\\Users\\{os.getlogin()}\\Downloads",
                                                                    title="Select a folder")
                progress = 1/totalNumberOfDownload*100
                activeDownloadPosition = 1
                try:
                    for index in selection :
                        if self.isCancelled :
                            break
                        videoTitle = RemoveIllegalCharacter.windowsFileExplorer(self.selectionBox.get(index))
                        self.progressLabel.configure(text=f"Downloading ({activeDownloadPosition}/{totalNumberOfDownload}) :  {videoTitle}")
                        self.theMainWindow.update()
                        self.domainController.downloadAudio(downloadFolderDestination,index)
                        self.progressBar.step(progress)
                        activeDownloadPosition += 1
                except Exception as e:
                    self.progressLabel.configure(str(e))
                    raise Exception(str(e))
                else:
                    self.progressLabel.configure(text="Download completed")
        except Exception as e:
            messagebox.showerror('Error',str(e))
        finally:
            self.buttonFetch.configure(state='active')
            self.removeVideoButton.configure(state='active')
            self.audioDownloadButton.configure(state='active')
            self.theMainWindow.update()
    
    def choiceSelected(self):
        self.urlLabel.configure(text=f"{self.choice.get().capitalize()} URL : ")
        self.buttonFetch.configure(text=f"Fetch {self.choice.get().capitalize()}")
    
    def removeSelectedVideo(self):
        self.domainController.removeVideo(self.selectionBox.curselection())
        self.updateSelectionBox()
        self.progressLabel.configure(text="")
        self.progressBar.configure(value=0)

    def updateSelectionBox(self):

        self.clearListBox(self.selectionBox)

        videos = self.domainController.getVideoTitles()
        for video in videos:
            self.selectionBox.insert(END,video)

    def clearListBox(self,listbox:Listbox):
        if listbox.size() > 0 :
            lastElementIndex = listbox.size()-1
            listbox.delete(0,lastElementIndex)

    def cancelDownload(self):
        self.isCancelled=True
        self.progressLabel.configure(text="Download Canceled")
        self.progressBar.configure(value=0)
        self.domainController.cancelDownload()

    def run(self):
        self.theMainWindow.mainloop() 




