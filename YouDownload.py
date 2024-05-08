from xml import dom
import Presentation.MainWindow as MainWindow
import Domain.DomainController as DomainController
import Controller.MainWindowController as MainWindowController

def main():
    model = DomainController.DomainController()
    mainWindow = MainWindow.MainWindow()
    mainWindowController = MainWindowController.MainWindowController(model,mainWindow)

    mainWindow.run()

if __name__ == "__main__":
    main()
