from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout
from PyQt6.QtCore import *

import GameScreens.MainWindow as MainWindow
import GameScreens.Components.LoginFrame as LoginFrame
import GameScreens.Components.StartMenuFrame as StartMenuFrame

class StartMenu(QMainWindow):
    '''
    Class that handles the initial start menu

    Attributes:
        layout (QVBoxLayout): The main layout for the window
        mainWindow (MainWindow): Instance of the MainWindow class for navigation
        adminRights (Bool): Checks if user has admin rights
    '''
    # Initialize class variable
    layout = QVBoxLayout()
    mainWindow = MainWindow.MainWindow() 
    adminRights = False

    def __init__(self):
        '''
        Initializes StartMenu

        '''
        super().__init__()
        
        # Removes frame from window
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        # Set styles for app
        self.setStyleSheet("QMainWindow {background-color: black}")
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.setSpacing(25)

        # Frame classes allow to show and hide layouts and keep the menu cleaner
        self.loginFrame = LoginFrame.LoginFrame(self)
        self.startMenuFrame = StartMenuFrame.StartMenuFrame(self, self.adminRights)
        self.layout.addWidget(self.loginFrame.getFrame())
        self.layout.addWidget(self.startMenuFrame.getFrame())


        # sets cursor
        cursor = Qt.CursorShape.PointingHandCursor
        self.setCursor(cursor)

        # widget for the app
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        self.showMaximized()     

    def setAdminRights(self, adminRights):
        '''
        Setter for adminRights

        '''
        self.adminRights = adminRights

    def getAdminRights(self):
        '''
        Getter for adminRights
        '''
        return self.adminRights
    
    def createAndShowStartMenuFrame(self):
        '''
        Method to create and switch to a start menut frame
        '''
        self.startMenuFrame.adminRights = self.adminRights
        self.startMenuFrame.getFrame().show()


    def ReturnTitleButtonCSS(self):
         '''
         Returns a string to set the push button CSS
         '''
         return """QPushButton {
                height: 75px; 
                max-width: 200px; 
                background-color: #2f2f2f; 
                color: goldenrod; 
                font-family: 'Georgia'; 
                font-weight: bold; 
                font-size: 24pt; 
                border: 2px solid goldenrod; 
                border-radius: 27px;
                padding: 15px}"""
    