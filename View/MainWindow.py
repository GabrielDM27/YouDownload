from tkinter import *
from tkinter.ttk import Progressbar,Combobox
from PIL import Image, ImageTk

from Util.VideoQuality import VideoQuality

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
        self.image =ImageTk.PhotoImage(Image.open("Image\\YoutubePlaylist.jpg").resize((400,200)))
        self.banner = Canvas(self.topFrame ,width=400,height=200)
        self.bannerImage = self.banner.create_image(0,0,image=self.image,anchor=NW)
        self.banner.pack(side='top',pady=(10,0))
        
    def buildFetchFrame(self):
        self.fetchFrame = Frame(self.theMainWindow,
                                height=100)
        self.fetchFrame.pack(side='top')
                
        self.urlFetchFrame = Frame(self.fetchFrame)
        self.urlFetchFrame.pack(side='top',pady=10)
        
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
                            text = "Fetch",
                            width=20
                            )
        self.buttonFetch.pack(side='left')

    def buildSelectionFrame(self):
        
        self.selectionFrame = Frame(self.theMainWindow)
        self.selectionFrame.pack(side='top')
        self.videoSelectionFrame = Frame(self.selectionFrame)
        self.videoSelectionFrame.pack(side='top',ipady=10)
        
        scrollbar = Scrollbar(self.videoSelectionFrame,orient='vertical')
        scrollbar.pack(side='right',fill='y')

        self.selectionBox = Listbox(self.videoSelectionFrame,selectmode='extended',width=100,height=10)
        self.selectionBox.pack(side='left')

        scrollbar.config(command=self.selectionBox.yview)
        self.selectionBox.config(yscrollcommand=scrollbar.set)

        self.videoQualityFrame = Frame(self.selectionFrame)
        self.videoQualityFrame.pack(side='top',ipadx=100)

        self.videoQualityLabel = Label(self.videoQualityFrame,text='Maximum video quality : ')
        self.videoQualityLabel.pack(side='left')

        self.videoQualityChoice = Combobox(self.videoQualityFrame,state='readonly')
        self.videoQualityChoice['values'] = VideoQuality.getVideoQualityList()
        self.videoQualityChoice.current(0)  #Audio Only by default
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
        
        self.videoDownloadFrame = Frame(self.downloadFrame)
        self.videoDownloadFrame.pack(side='top',pady=(20,0))

        self.videoDownloadButton = Button(self.videoDownloadFrame,
                                          text='Download',
                                          width=10,
                                          )
        self.videoDownloadButton.pack(side='left')
        self.videoCancelButton = Button(self.videoDownloadFrame,
                                        text='Cancel',
                                        width=10,
                                        )
        self.videoCancelButton.pack(side='left',padx=(10,0))
        
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




