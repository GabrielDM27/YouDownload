# Python tkinter hello world program 


from tkinter import *
from tkinter import messagebox

class MainWindow:
    theMainWindow = Tk() 
    
    # default constructor
    def __init__(self):
        
        self.theMainWindow.title("YouDownload")
        self.theMainWindow.geometry("480x270")
        self.theMainWindow.state('zoomed')

        self.theMainWindow.grid_rowconfigure(0,weight=1)
        self.theMainWindow.grid_rowconfigure(2,weight=1)
        self.theMainWindow.grid_columnconfigure(0,weight=1)
        
        topFrame = Frame(self.theMainWindow, bg = 'red')
        topFrame.grid(row=0,sticky='nwse')
        
        
        #Midlle frame config
        
        middleFrame = Frame(self.theMainWindow,name='middleFrame',height=100 ,bg = 'blue')
        middleFrame.grid(row=1,sticky='nwse')
        middleFrame.grid_columnconfigure(0,weight=1)
        middleFrame.grid_columnconfigure(3,weight=1)
        
        labelPlaylist = Label(middleFrame,name = "labelPlaylist",text = "Playlist ID : ")
        labelPlaylist.grid(column=1, row=0, sticky='e',padx=10)
        
        entry = Entry(middleFrame,width=200)
        entry.grid(column=2,row=0,sticky='w')
        

        #Bottom frame config
        bottomFrame = Frame(self.theMainWindow,bg = 'yellow')
        bottomFrame.grid(row=2,sticky='nwse')
        bottomFrame.grid_columnconfigure(0,weight=1)
        bottomFrame.grid_rowconfigure(0,pad=10)

        buttonTest = Button(bottomFrame, text = "Click me", command=self.buttonTestClicked)
        buttonTest.grid(column=0, row=0)


        

    def buttonTestClicked(self):
        #self.theMainWindow.children['middleFrame'].children['labelPlaylist'].configure(text = "Got clicked!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        result = messagebox.askquestion(None,"Do tou want to continue")
        
        if(result == 'yes'):
            print(result)
        else:
            self.theMainWindow.destroy()
            

    def run(self):
        self.theMainWindow.mainloop() 





