from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import *

class DialogBox(object):
    '''
    A class for the standard dialog box

    Parameters:
        message (string): String to put in the messagebox text

    Attributes:
        messageBox (QDialog): MessageBox object for display
        text (string): Text to enter into the text attribute of messageBox
    '''
    def __init__(self, message):
        # Initialize class variables
        self.messageBox = QMessageBox()
        self.text = message

        # Setup messageBox
        self.messageBox.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.messageBox.setText("<p align='center'>" + self.text)
        self.messageBox.addButton("Got it", QMessageBox.ButtonRole.AcceptRole)
        
        # Set style for object
        self.messageBox.setStyleSheet('''QMessageBox {
                                        background-color: #2b2a2a;
                                        font-family: 'Georgia'; 
                                        font-weight: bold; 
                                        font-size: 14pt;
                                        border: 1px solid goldenrod;
                                 }
                                    QDialogButtonBox > QPushButton {
                                        background-color: beige;
                                        color: black;
                                        font-family: 'Georgia'; 
                                        font-weight: bold; 
                                        font-size: 20pt; 
                                        border: 2px solid goldenrod; 
                                        padding: 10px;             
                                 }
                                    QLabel {
                                        background-color: beige;
                                        min-height: 300px;
                                        min-width: 500px;
                                        border: 2px solid goldenrod;
                                 }''')

    def setText(self, text):
        '''
        Setter for text
        '''
        self.text = text

    def getText(self):
        '''
        Getter for text
        '''
        return self.text

    def executeMessageBox(self):
        '''
        Method to open window
        '''
        self.messageBox.exec()

