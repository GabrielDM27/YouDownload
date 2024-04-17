# Python tkinter hello world program 


from tkinter import *
from tkinter import messagebox

class MainWindow:
    theMainWindow = Tk()
    #Variables
    choice=StringVar()
    
    # default constructor
    def __init__(self):
        self.theMainWindow.title("YouDownload")
        self.theMainWindow.geometry("480x270")
        self.theMainWindow.state('zoomed')
        
        #Build Frames
        self.buildTopFrame()
        self.buildFetchFrame()
        self.buildSelectionFrame()
        
        #Infinite loop
        self.run()

    def buildTopFrame(self):
        self.topFrame = Frame(self.theMainWindow ,
                         name='topFrame',
                         height=300 ,
                         bg = 'red')
        self.topFrame.pack(side='top')
        
    def buildFetchFrame(self):
        self.fetchFrame = Frame(self.theMainWindow,
                                name='fetchFrame',
                                height=100,bg = 'blue')
        self.fetchFrame.pack(side='top')
                
        self.urlFetchFrame = Frame(self.fetchFrame,
                              name='urlFetchFrame',
                              bg='black')
        self.urlFetchFrame.pack(side='top')
        
        self.urlLabel = Label(self.urlFetchFrame,
                         name = "urlLabel",
                         text = "Video URL : ")
        self.urlLabel.pack(side='left')
        
        self.urlEntry = Entry(self.urlFetchFrame,
                         width=125)
        self.urlEntry.pack(side='left')

        self.urlChoiceVideo = Radiobutton(self.urlFetchFrame,
                                     name = "urlChoiceVideo",
                                     text = 'video',
                                     value='video',
                                     variable=self.choice,
                                     command=self.choiceSelected)
        self.urlChoiceVideo.pack(side='left')
        self.urlChoiceVideo.select()
        
        self.urlChoicePlaylist = Radiobutton(self.urlFetchFrame,
                                        name = "urlChoicePlaylist",
                                        text = 'playlist',
                                        value='playlist',
                                        variable=self.choice,
                                        command=self.choiceSelected)
        self.urlChoicePlaylist.pack(side='left')
        
        self.btnFetchFrame = Frame(self.fetchFrame,
                              name='btnFetchFrame',
                              height=100,
                              bg='white')
        self.btnFetchFrame.pack(side='top')
        self.buttonFetch = Button(self.btnFetchFrame,
                            name = 'buttonFetch',
                            text = "Fetch",
                            command=self.buttonTestClicked)
        self.buttonFetch.pack(side='left')

    def buildSelectionFrame(self):
        
        self.selectionFrame = Frame(self.theMainWindow,
                               name='selectionFrame',
                               bg = 'yellow')
        self.selectionFrame.pack(side='bottom',
                            fill='both',
                            expand='true')
        
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




