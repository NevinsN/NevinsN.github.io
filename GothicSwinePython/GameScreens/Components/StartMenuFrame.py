from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import *

import sys

import Database.CreateDBItems as CreateDBItems

class StartMenuFrame(object):
    '''
    Class that handles the initial start menu

    Attributes:
        frame(QFrame): A frame to hold the layouts and enable showing/hiding
        parent(QMainWindow): The parent widget
        layout (QVBoxLayout): The main layout for the window
    '''
    def __init__(self, parent, adminRights):
        # Initialize class variables
        self.frame = QFrame()                
        self.parent = parent
        self.adminRights = adminRights 
        layout = QVBoxLayout()               

        # Game title object
        titleLabel = QLabel("Gothic Swine", self.frame)
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titleLabel.setStyleSheet("QLabel {color: goldenrod; font-family: 'Georgia'; font-weight: bold; font-size: 148pt;}")

        # Logic for all the buttons
        buttonLayout = QHBoxLayout()

        # Button to start the game
        startButton = QPushButton("Start Game")
        startButton.clicked.connect(self.startGame)
        startButton.setStyleSheet(self.ReturnTitleButtonCSS())
        
        # Button to quit the game
        exitButton = QPushButton("Quit")
        exitButton.clicked.connect(sys.exit)
        exitButton.setStyleSheet(self.ReturnTitleButtonCSS())

        # Sets button to buttoLayout
        buttonLayout.addWidget(startButton)
        buttonLayout.addWidget(exitButton)

        # Conditional button based on adminRights.
        # Disabled by default, since it can mess up the database 
        # and takes a fair bit of time to run.
        # A later, more final version will likely have it enable by default
        if adminRights:
            updateItemsButton = QPushButton("Update Items")
            updateItemsButton.clicked.connect(self.updateItemsDatabase)
            updateItemsButton.setStyleSheet(self.ReturnTitleButtonCSS())
            updateItemsButton.setDisabled(True)
            buttonLayout.addWidget(updateItemsButton)

        # Finalize layout
        layout.addWidget(titleLabel)
        layout.addLayout(buttonLayout)
        self.frame.setLayout(layout)

        # Show frame
        self.frame.hide()

    def getParent(self):
        '''
        Getter for parent
        '''
        return self.parent
    
    def getFrame(self):
        '''
        Getter for frame
        '''
        return self.frame

    def startGame(self):
        '''
        Method to start the game, opening MainWindow and closing this one
        Calls to parent to do so
        '''
        self.parent.mainWindow.showMaximized()
        self.parent.mainWindow.runIntroDB()

        self.parent.close()

    def ReturnTitleButtonCSS(self):
         '''
         Returns a string to set the push button CSS
         '''
         return """QPushButton {
                height: 75px; 
                max-width: 250px; 
                background-color: #2f2f2f; 
                color: goldenrod; 
                font-family: 'Georgia'; 
                font-weight: bold; 
                font-size: 24pt; 
                border: 2px solid goldenrod; 
                border-radius: 27px}
                
                QPushButton:disabled {
                color: gray;
                }"""
    
    def updateItemsDatabase(self):
        '''
        Method to update the items database
        Hardcoded for now, but will be made more dynamic eventually
        '''
        dbInit = CreateDBItems.CreateDBItems("Data/gothicSwineDataItems.csv")