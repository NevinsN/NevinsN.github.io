from PyQt6.QtWidgets import QFrame, QVBoxLayout, QPushButton
from PyQt6.QtCore import *

class LoginFrame(object):
    '''
    Class that handles the initial start menu

    Attributes:
        frame(QFrame): A frame to hold the layouts and enable showing/hiding
        parent(QMainWindow): The parent widget
        layout (QVBoxLayout): The main layout for the window
    '''
    def __init__(self, parent):
        # Initialize class variables
        self.frame = QFrame()
        self.parent = parent
        layout = QVBoxLayout()

        # Button to login as user
        userButton = QPushButton("Login as User")
        userButton.clicked.connect(self.switchToStartMenu)
        userButton.setStyleSheet(self.ReturnTitleButtonCSS())

        # Button to login as admin
        adminButton = QPushButton("Login as Admin")
        adminButton.clicked.connect(self.switchToStartMenuAdmin)
        adminButton.setStyleSheet(self.ReturnTitleButtonCSS())

        # Adding to layouts
        layout.addWidget(userButton)
        layout.addWidget(adminButton)
        self.frame.setLayout(layout)

        # Show the frame as active
        self.frame.show()
    
    def getFrame(self):
        '''
        Getter for frame
        '''
        return self.frame

    def switchToStartMenu(self):
        '''
        Deactivates this frame and returns False for adminRights
        '''
        self.frame.hide()
        self.parent.setAdminRights(False)
        self.parent.createAndShowStartMenuFrame() # return for adminRights
    
    def switchToStartMenuAdmin(self):
        '''
        Deactivate this frame and returns True for adminRights
        '''
        self.frame.hide() 
        self.parent.setAdminRights(True)
        self.parent.createAndShowStartMenuFrame() # return for adminRights

    def ReturnTitleButtonCSS(self):
         '''
         Returns a string to set the push button CSS
         '''
         return """QPushButton {
                height: 75px; 
                max-width: 300px; 
                background-color: #2f2f2f; 
                color: goldenrod; 
                font-family: 'Georgia'; 
                font-weight: bold; 
                font-size: 24pt; 
                border: 2px solid goldenrod; 
                border-radius: 27px}"""
