import View.MainWindow as MainWindow
import Model.ModelFacade as Model
import Controller.MainWindowController as MainWindowController

def main():
    model = Model.ModelFacade()
    mainWindow = MainWindow.MainWindow()
    mainWindowController = MainWindowController.MainWindowController(model,mainWindow)

    mainWindow.run()

if __name__ == "__main__":
    main()
