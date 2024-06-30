import sys

from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGridLayout
from PyQt6.QtCore import *

import Assets.MapManager as MapManager
import GameScreens.Components.MapDisplayFrame as MapDisplay
import GameScreens.Components.DialogBox as DiBx
import GameScreens.Components.SolveDialogBox as SolvBx
import Assets.PlayerCharacter as PC
import GameScreens.Components.WinLossScreen as WinLoss

class MainWindow(QMainWindow):
    '''
    A class for the main gameplay window

    Attributes:
        layout (QVBoxLayout): The main window layout
        submittedSuspect (bool): Detects if the submit button has been pressed
        introText (string): Holds introduction text
        map (MapManager): Manages all things map for the gameplay
        currentRoom (Room): Stores the current room from map
        player (PlayerCharacter): The object that controls the player character
        roomNameLabel (QLabel): Label that show the room's name on the screen
        gameplayLayout (QHBoxLayout): Holds the top two elements of the screen
        mainScreenLayout (QGridLayout): Holds layout for the main game screen
        goNorthButton (QPushButton): Button for going North
        goWestButton (QPushButton): Button for going West
        goEastButton (QPushButton): Button for going East
        goSouthButton (QPushButton): Button for going South
        gameplayLabel (QLabel): gameplayLabel presents the player with the information about the current room
        background (QWidget): A background for menuLayout
        menuLayout (QVBoxLayout): menuLayout holds menu buttons vertically
        notepadButton (QPushButton): Button to display player's collected notes
        examineNPCButton (QPushBUtton): Button to see what NPC is wearing
        questionNPCButton (QPushButton): Button to get a hint from the NPC
        solveButton (QPushButton): Button to attempt to solve the murder
        quitButton (QPushButton): Button to quit the game
    '''
    layout = QVBoxLayout()
    submittedSuspect = False

    introText = '''You're finally here! My name is Constable Eli. Late last night, the world-renowned singer Abigail Piper
                   was murdered at her own dinner party in her gothic manor house! She asked everyone to come in their 
                   favorite attire, so we had some bizzare looks! Maybe that will help you narrow down a suspect. <br><br> 
                   I've sequestered each guest in a seperate room, so question them soon as you can. I'm sure the guilty 
                   party will lie, and some of the guests might not be as reliable as we would like. Remember, as a law
                   enforcement officer, I'll always be honest, though I can't promise to be helpful. <br><br>
                   Once you think you know who the fiend is, come back here and let me know! Good luck, detective!<br><br>
                   Oh, and be careful or you might be next!'''

    def __init__(self):
        '''
        Initializes main window
        '''
        super().__init__()

        # Initialize class variables
        self.map = MapManager.MapManager()
        self.currentRoom = self.map.getCurrentRoom()
        self.player = PC.PlayerCharacter()
        
        # removes window frame
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("Gothic Swine")

        # Sets style
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("QMainWindow {background-color: black}")

        # sets roomNameLabel and style
        self.roomNameLabel = QLabel(self.currentRoom.getRoomName())
        self.roomNameLabel.setStyleSheet("""QLabel {
                                    color: goldenrod;
                                    font-family: 'Georgia';
                                    font-size: 40pt;
                                    font-weight: bold
                                    }
                                    """)
        
        # Initialize layouts 
        gameplayLayout = QHBoxLayout()
        mainScreenLayout = QGridLayout()

        # goNorthButton Initialization and setup
        self.goNorthButton = QPushButton("Go North")
        self.goNorthButton.setDisabled(True) # Begins disabled to be activated later if a room has a door in that direction
        self.goNorthButton.clicked.connect(self.goNorth)
        self.goNorthButton.setStyleSheet(self.ReturnScreenButtonCSS())

        # add roomNameLabel and goNorthButton to first two rows
        mainScreenLayout.addWidget(self.roomNameLabel, 0, 1, 1, 1, Qt.AlignmentFlag.AlignCenter)
        mainScreenLayout.addWidget(self.goNorthButton, 1, 1, 1, 1, Qt.AlignmentFlag.AlignCenter)

        # goWestButton Initialization and setup
        self.goWestButton = QPushButton("Go West")
        self.goWestButton.setDisabled(True) # Begins disabled to be activated later if a room has a door in that direction
        self.goWestButton.clicked.connect(self.goWest)
        self.goWestButton.setStyleSheet(self.ReturnScreenButtonCSS())

        # gameplayLabel Initialization and setup
        self.gameplayLabel = QLabel()
        self.buildRoomText()
        self.gameplayLabel.setStyleSheet("""QLabel {
                                    background-color: beige;
                                    color: black;
                                    font-family: 'Georgia';
                                    font-size: 14pt;
                                    border: 2px solid goldenrod; 
                                    border-radius: 27px; 
                                    min-height: 400px;
                                    min-width: 500px;}""")
        self.gameplayLabel.setWordWrap(True)
        self.gameplayLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # goEastButton Initialization and setup
        self.goEastButton = QPushButton("Go East")
        self.goEastButton.setDisabled(True) # Begins disabled to be activated later if a room has a door in that direction
        self.goEastButton.clicked.connect(self.goEast)
        self.goEastButton.setStyleSheet(self.ReturnScreenButtonCSS())

        # adds center row widgets to mainScreenLayout
        mainScreenLayout.addWidget(self.goWestButton, 2, 0, 1, 1, Qt.AlignmentFlag.AlignCenter)
        mainScreenLayout.addWidget(self.gameplayLabel, 2, 1, 1, 1, Qt.AlignmentFlag.AlignCenter)
        mainScreenLayout.addWidget(self.goEastButton, 2, 2, 1, 1, Qt.AlignmentFlag.AlignCenter)

        # goSouthButton Initialization and setup
        self.goSouthButton = QPushButton("Go South")
        self.goSouthButton.setDisabled(True) # Begins disabled to be activated later if a room has a door in that direction
        self.goSouthButton.clicked.connect(self.goSouth)
        self.goSouthButton.setStyleSheet(self.ReturnScreenButtonCSS())

        # add goSouthButton to layout
        mainScreenLayout.addWidget(self.goSouthButton, 3, 1, 1, 1, Qt.AlignmentFlag.AlignCenter)
        
        # Initializes direction button disabled status
        self.initRoomButtons()

        # Adds mainScreenLayout to gamePlayLayout
        gameplayLayout.addLayout(mainScreenLayout)

        # Initialize background
        background = QWidget()
        background.setStyleSheet("""QWidget {
                                 background-color: beige;
                                 max-height: 600px;
                                 border: 2px solid goldenrod; 
                                 border-radius: 27px
                                 }
                                 """)
        
        # Initializes menuLayout
        menuLayout = QVBoxLayout(background)
        menuLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Initialize and setup notepadButton
        self.notepadButton = QPushButton("Notes")
        self.notepadButton.clicked.connect(self.checkNotepad)
        self.notepadButton.setStyleSheet(self.ReturnScreenButtonCSS())
        self.notepadButton.setDisabled(True)

        # Initialize and setup examineNPCButton
        examineNPCButton = QPushButton("Examine Person")
        examineNPCButton.clicked.connect(self.examineCharacterInRoom)
        examineNPCButton.setStyleSheet(self.ReturnScreenButtonCSS())

        # Initialize and setup questionNPCButton
        questionNPCButton = QPushButton("Question Person")
        questionNPCButton.clicked.connect(self.questionCharacter)
        questionNPCButton.setStyleSheet(self.ReturnScreenButtonCSS())

        # Initialize and setup solveButton
        self.solveButton = QPushButton("Attempt to Solve")
        self.solveButton.clicked.connect(self.attemptToSolveGame)
        self.solveButton.setStyleSheet(self.ReturnScreenButtonCSS())
        self.solveButton.setDisabled(True)

        # Initialize and setup quitButton
        quitButton = QPushButton("Quit")
        quitButton.clicked.connect(sys.exit)
        quitButton.setStyleSheet(self.ReturnScreenButtonCSS())

        # Add Buttons to menuLayout
        menuLayout.addWidget(self.notepadButton)
        menuLayout.addWidget(examineNPCButton)
        menuLayout.addWidget(questionNPCButton)
        menuLayout.addWidget(self.solveButton)
        menuLayout.addWidget(quitButton)

        gameplayLayout.addWidget(background)

        # sets cursor
        cursor = Qt.CursorShape.PointingHandCursor
        self.setCursor(cursor)

        # Prints a commandline map for debugging
        mapDisplay = MapDisplay.MapDisplayFrame(self.map.map)
        mapFrame = mapDisplay.getFrame()

        # finalizes layout and app display
        self.layout.addLayout(gameplayLayout)
        self.layout.addWidget(mapFrame)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def setSubmittedSuspect(self, submittedSuspect):
        self.submittedSuspect - submittedSuspect

    def getSubmittedSuspect(self):
        return self.submittedSuspect

    def ReturnScreenButtonCSS(self):
        '''
        Method to return CSS for the QPushButtons
        '''
        return """QPushButton {
                min-height: 40px; 
                min-width: 125px; 
                background-color: #2f2f2f; 
                color: goldenrod; 
                font-family: 'Georgia'; 
                font-weight: bold; 
                font-size: 16pt; 
                border: 2px solid goldenrod; 
                border-radius: 27px;
                padding: 5px}
                
                QPushButton:disabled {
                color: gray;
                }"""
    
    def buildRoomText(self):
         '''
         Method to build the text for the gameplayLabel
         '''
         # Sets roomNameLabel with currRoom's roomName
         self.roomNameLabel.setText(self.currentRoom.getRoomName())
         
         # textToReturn is a running string that will fill gameplayLabel
         textToReturn = self.currentRoom.getRoomDescription() # Pulls description
         textToReturn += "\n\nOther people in the room: "     
         for char in self.currentRoom.getCharactersInRoom():  # Goes through all characters and adds their name to string
             textToReturn += char.getCharacterName()
 
         # Sets gameplayLabel
         self.gameplayLabel.setText(textToReturn)
    
    def initRoomButtons(self): 
        '''
        Method to initialize the direction buttons
        '''
        # Begins by disabling all four buttons
        self.goSouthButton.setDisabled(True)
        self.goNorthButton.setDisabled(True)
        self.goEastButton.setDisabled(True)
        self.goWestButton.setDisabled(True)
   
        # Gets dictionary from connectedRooms from currentRoom
        # Iterates through dictionary with key (direction) and value (room)
        for direction, room in self.currentRoom.getConnectedRooms().items():
            if room == ["Invalid Location"]: # "Invalid Location" means it's outside the map grid
                continue # Nothing occurs and it moves to next connection
            elif room == [None]:             # Room of type None means that there is no room at that connection
                continue # Nothing occurs and it moves to next connection
            else:                            # A valid Room item is found
                # Match statement looks at direction, and sets the proper button to enabled
                match direction:
                    case 'North':
                        self.goNorthButton.setDisabled(False)
                    case 'East':
                        self.goEastButton.setDisabled(False)
                    case 'South':
                        self.goSouthButton.setDisabled(False)
                    case 'West':
                        self.goWestButton.setDisabled(False)                      

    def goNorth(self):
        '''
        Method to move the player north
        '''
        self.map.moveNorth() 
        self.currentRoom = self.map.getCurrentRoom()
        
        # Resets room text and button values
        self.buildRoomText()
        self.initRoomButtons()

        # solveButton is only valid in the foyer, where the constable is. 
        # This ensures it is only active when in the foyer
        if self.currentRoom.getRoomName() == 'Foyer':
            self.solveButton.setDisabled(False)
        else:
            self.solveButton.setDisabled(True)

        # Console output for movement
        print("Moved to the " + str(self.currentRoom.getRoomName()))

    def goEast(self):
        '''
        Method to move the player east
        '''
        self.map.moveEast()
        self.currentRoom = self.map.getCurrentRoom()

        # Resets room text and button values
        self.buildRoomText()
        self.initRoomButtons()

        # solveButton is only valid in the foyer, where the constable is. 
        # This ensures it is only active when in the foyer
        if self.currentRoom.getRoomName() == 'Foyer':
            self.solveButton.setDisabled(False)
        else:
            self.solveButton.setDisabled(True)
        
        # Console output for movement
        print("Moved to the " + str(self.currentRoom.getRoomName()))

    def goSouth(self):
        '''
        Method to move the player south
        '''
        self.map.moveSouth()
        self.currentRoom = self.map.getCurrentRoom()

        # Resets room text and button values
        self.buildRoomText()
        self.initRoomButtons()

        # solveButton is only valid in the foyer, where the constable is. 
        # This ensures it is only active when in the foyer
        if self.currentRoom.getRoomName() == 'Foyer':
            self.solveButton.setDisabled(False)
        else:
            self.solveButton.setDisabled(True)
        
        # Console output for movement
        print("Moved to the " + str(self.currentRoom.getRoomName()))

    def goWest(self):
        '''
        Method to move the player west
        '''
        self.map.moveWest()
        self.currentRoom = self.map.getCurrentRoom()

        # Resets room text and button values
        self.buildRoomText()
        self.initRoomButtons()

        # solveButton is only valid in the foyer, where the constable is. 
        # This ensures it is only active when in the foyer
        if self.currentRoom.getRoomName() == 'Foyer':
            self.solveButton.setDisabled(False)
        else:
            self.solveButton.setDisabled(True)
        
        # Console output for movement
        print("Moved to the " + str(self.currentRoom.getRoomName()))

    def examineCharacterInRoom(self):
        '''
        Method to examine a character. 
        dialogBox is called and the present character is passed to populate text
        '''
        dialogBox = DiBx.DialogBox(self.player.examineCharacter(self.currentRoom.getCharactersInRoom()[0]))
        dialogBox.executeMessageBox()

    def questionCharacter(self):
        '''
        Method to question a character. 
        dialogBox is called and the present character is passed to populate text
        player questionCharacter(NPC) method is then called
        '''
        dialogBox = DiBx.DialogBox(self.currentRoom.getCharactersInRoom()[0].getHintToGive())
        self.player.questionCharacter(self.currentRoom.getCharactersInRoom()[0])
        dialogBox.executeMessageBox()

        self.notepadButton.setDisabled(False)

    def checkNotepad(self): 
        '''
        Method to check the notepad. 
        notepad string is constructed from player.getNotes(),
        dialogBox is called and the notes are printed
        '''       
        notes = self.player.getNotes()
        notepadString = ''
        for charNPC, hint in notes.items():
            notepadString += charNPC.getCharacterName() + ": " + hint + "<br>"

        dialogBox = DiBx.DialogBox(notepadString)
        dialogBox.executeMessageBox()

    def attemptToSolveGame(self):
        '''
        Method to solve game. 
        dialogBox is called and winLoss is called and populated with the player's guess
        '''
        slvBox = SolvBx.SolveDialogBox(self ,self.map.NPCList)
        slvBox.executeMessageBox()
        
        print(self.submittedSuspect)

        if self.getSubmittedSuspect():
            playerAccusation = slvBox.getSuspectSelection()
            slvBox.closeWindow()
            if playerAccusation == self.map.getVillain().getCharacterName():
                print("You won!")
                winLoss = WinLoss.WinLossScreen(self, True, playerAccusation)

            else:
                print("You lost!")
                winLoss = WinLoss.WinLossScreen(self, False, playerAccusation)

    def runIntroDB(self):
        '''
        Method to play the intro dialog box
        '''
        introDB = DiBx.DialogBox(self.introText)
        introDB.executeMessageBox()