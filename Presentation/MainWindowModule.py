# Python tkinter hello world program 


from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar, Treeview

class MainWindow:
    theMainWindow = Tk()
   
    #Variables
    choice=StringVar()
    
    # default constructor
    def __init__(self):
        self.theMainWindow.title("YouDownload")
        #self.theMainWindow.geometry("480x270")
        self.theMainWindow.state('zoomed')
        self.theMainWindow.minsize(1000,700)
        
        #Build Frames
        self.buildTopFrame()
        self.buildFetchFrame()
        self.buildSelectionFrame()
       
        
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
        
        self.urlEntry = Entry(self.urlFetchFrame,
                         width=125)
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
                            command=self.buttonTestClicked)
        self.buttonFetch.pack(side='left')

    def buildSelectionFrame(self):
        
        self.selectionFrame = Frame(self.theMainWindow)
        self.selectionFrame.pack(side='bottom',
                            fill='both',
                            expand='true')
        self.audioSelectionFrame = Frame(self.selectionFrame,
                                         name = 'audioSelectionFrame')
        self.audioSelectionFrame.pack(side='top')

        self.audioSelectionBox = Treeview(self.audioSelectionFrame,
                                          columns=('c1','c2','c3'),
                                          show='headings',
                                          height=10
                                          )
        self.audioSelectionBox.pack(side='left')
        self.audioSelectionBox.heading(0,text='Column1')
        self.audioSelectionBox.heading(1,text='Column2')
        self.audioSelectionBox.heading(2,text='Column3')

        scrollbar = Scrollbar(self.audioSelectionFrame,orient='vertical')
        scrollbar.config(command=self.audioSelectionBox.yview)
        scrollbar.pack(side='right',fill='y')
        
        self.audioSelectionBox.config(yscrollcommand=scrollbar.set)
        
        self.audioInfoFrame = Frame(self.selectionFrame)
        self.audioInfoFrame.pack(side='top')
        
        self.audioInfoNbOfFileLabel = Label(self.audioInfoFrame,
                                            text='Number of file : ')
        self.audioInfoNbOfFileLabel.pack(side='left')
        self.audioInfoNbOfFileResultLabel = Label(self.audioInfoFrame,
                                            text='0')
        self.audioInfoNbOfFileResultLabel.pack(side='left')


        self.audioInfoTotalDownloadResultLabel = Label(self.audioInfoFrame,
                                            text='0')
        self.audioInfoTotalDownloadResultLabel.pack(side='right')
        self.audioInfoTotalDownloadLabel = Label(self.audioInfoFrame,
                                            text='Number of file : ')
        self.audioInfoTotalDownloadLabel.pack(side='right')
        
        self.audioDownloadFrame = Frame(self.selectionFrame)
        self.audioDownloadFrame.pack(side='top')
        self.audioDownloadButton = Button(self.audioDownloadFrame,
                                          text='Download',
                                          width=10
                                          )
        self.audioDownloadButton.pack(side='left')
        self.audioCancelButton = Button(self.audioDownloadFrame,
                                        text='Cancel',
                                        width=10)
        self.audioCancelButton.pack(side='left',padx=(10,0))
        
        self.progressFrame = Frame(self.selectionFrame)
        self.progressFrame.pack(side='top')
        self.progressBar=Progressbar(self.progressFrame,length=400)
        self.progressBar.pack()
        

    def buttonTestClicked(self):
        #self.theMainWindow.children['middleFrame'].children['labelPlaylist'].configure(text = "Got clicked!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        result = messagebox.askquestion(None,"Do tou want to continue")
        
        if(result == 'yes'):
            print(result)
        else:
            self.theMainWindow.destroy()
            
    def choiceSelected(self):
        (self.theMainWindow 
            .children['fetchFrame'] 
            .children['urlFetchFrame'] 
            .children['urlLabel'] 
            .configure(text=f"{self.choice.get().capitalize()} URL : ")
        )
        (self.theMainWindow
         .children['fetchFrame']
         .children['btnFetchFrame']
         .children['buttonFetch']
         .configure(text=f"Fetch {self.choice.get().capitalize()}")
        )

    def run(self):
        self.theMainWindow.mainloop() 




