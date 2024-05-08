from tkinter import *
from tkinter.ttk import Progressbar,Combobox

class MainWindow:
    def __init__(self):
        self.theMainWindow = Tk()
        self.theMainWindow.title("YouDownload")
        self.theMainWindow.minsize(1000,700)
        
        #Build Frames
        self.buildTopFrame()
        self.buildFetchFrame()
        self.buildSelectionFrame()
        self.buildDownloadFrame()


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
        
        self.btnFetchFrame = Frame(self.fetchFrame,
                              height=100)
        self.btnFetchFrame.pack(side='top')
        self.buttonFetch = Button(self.btnFetchFrame,
                            text = "Fetch"
                            )
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
                                        text = 'Remove Selected Video'
                                        )
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
                                          )
        self.audioDownloadButton.pack(side='left')
        self.audioCancelButton = Button(self.audioDownloadFrame,
                                        text='Cancel',
                                        width=10,
                                        )
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
    
    def run(self):
        self.theMainWindow.mainloop() 




