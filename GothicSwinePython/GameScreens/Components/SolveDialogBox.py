from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton
from PyQt6.QtCore import *
from functools import partial

class SolveDialogBox(object):
    '''
    A class for the attempt to solve dialog box

    Parameters:
        charList (List): List of characters in the map

    Attributes:
        messageBox (QDialog): MessageBox object for display
        suspectSelection (string): holds the name of the suspect currently selected in radio buttons
        layout (QVBoxLayout): Main layout
        textLabel (QLabel): Holds the prompt for display
        selectorLayout (OVBoxLayout): Layout for radio buttons
        buttonLayout (QHBoxLayout): Layout for selection buttons
        solveButton (QPushButton): Button to attempt ot solve
        cancelButton (QPushButton): Button to cancel attempt
    '''
    parent = None

    def __init__(self, parent, charList):
        # Initialize class variables
        self.parent = parent
        self.messageBox = QDialog()
        self.messageBox.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.suspectSelection = ''
        layout = QVBoxLayout()
        buttonLayout = QHBoxLayout()
        self.textLabel = QLabel("Accuse your suspect, but be careful! You only get one guess.")
        selectorLayout = QVBoxLayout()

        # Iterates over charList and creates a radio button per character
        for char in charList:
            newRadio = QRadioButton()
            charName = char.getCharacterName()
            newRadio.setText(charName)
            newRadio.toggled.connect(partial(self.changeSuspectSelection, charName)) # Connecting the partial allows for storing of character name
            selectorLayout.addWidget(newRadio)

        # Initialize and setup solveButton
        solveButton = QPushButton("They did it!")
        solveButton.clicked.connect(self.submitAccusation)

        # Initialize and setup cancelButton
        cancelButton = QPushButton("On second thought...")        
        cancelButton.clicked.connect(self.messageBox.close)

        # Attach widgets and layouts
        buttonLayout.addWidget(solveButton)
        buttonLayout.addWidget(cancelButton)
        layout.addWidget(self.textLabel)
        layout.addLayout(selectorLayout)
        layout.addLayout(buttonLayout)

        # Sets style for object
        self.messageBox.setStyleSheet('''QDialog {
                                        background-color: #2b2a2a;
                                        font-family: 'Georgia'; 
                                        font-weight: bold; 
                                        font-size: 14pt;
                                        border: 1px solid goldenrod;
                                 }
                                    QPushButton {
                                        background-color: beige;
                                        color: black;
                                        font-family: 'Georgia'; 
                                        font-weight: bold; 
                                        font-size: 20pt; 
                                        border: 2px solid goldenrod; 
                                        padding: 10px;             
                                 }
                                    QRadioButton {
                                        background-color: beige;
                                        min-height: 30px;
                                        min-width: 50px;
                                        font-family: 'Georgia'; 
                                        font-weight: bold; 
                                        font-size: 12pt;
                                        border: 2px solid goldenrod;
                                 }
                                    QLabel {
                                        background-color: beige;
                                        min-height: 30px;
                                        min-width: 50px;
                                        font-family: 'Georgia'; 
                                        font-weight: bold; 
                                        font-size: 16pt;
                                        border: 2px solid goldenrod;
                                 }''')
        
        self.messageBox.setLayout(layout)

    def changeSuspectSelection(self, suspect):
        '''
        Method to set suspectSelection
        '''
        self.suspectSelection = suspect
        print("Player selecting " + self.suspectSelection)

    def getSuspectSelection(self):
        '''
        Getter for suspectSelection
        '''
        return self.suspectSelection

    def submitAccusation(self):
        '''
        Method to submit accusation
        '''
        if self.suspectSelection == '':
            self.textLabel.setText("You must make a seclection to submit!")
        else:
            self.parent.submittedSuspect = True
            self.messageBox.hide()

    def closeWindow(self):
        '''
        Method to close window
        '''
        self.suspectSelection = ''
        self.messageBox.close()

    def executeMessageBox(self):
        '''
        Method to open window
        '''
        self.messageBox.exec()