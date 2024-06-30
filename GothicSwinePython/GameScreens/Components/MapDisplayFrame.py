from PyQt6.QtWidgets import QFrame, QGridLayout, QLabel
from PyQt6.QtCore import Qt

class MapDisplayFrame(object):
    '''
    A class for the map display frame

    Parameters:
        dataframe (Pandas Dataframe): Dataframe that holds the map

    Attributes:
        dataframe (Pandas Dataframe): Dataframe that holds the map as passed through parameters
        frame (QFrame): A frame to hold the map elements
        layout (QGridLayout): Main layout
        newLabel (QLable): Holds name of room if in map
        cellData (string): Data found in the dataframe cell
    '''
    def __init__(self, dataframe):
        # Initialize class variables
        self.dataframe = dataframe
        self.frame = QFrame()
        layout = QGridLayout()

        # Loop to create the labels for a 5 x 5 grid
        for x in range(5):
            for y in range(5):
                newLabel = QLabel()
                cellData = self.dataframe.iat[x, y]
                # Only prints if a room is found
                if type(cellData) == type(None):
                    cellData = cellData
                else:
                    cellData = cellData.getRoomName()

                newLabel.setText(cellData)
                newLabel.setStyleSheet("""QLabel {
                                    background-color: beige;
                                    color: black;
                                    font-family: 'Georgia';
                                    font-size: 12pt; 
                                    border: 1px solid black;
                                    margin: 0px;
                                    min-height: 75px;
                                    min-width: 200px;}""")
                newLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
                layout.addWidget(newLabel, x, y, 1, 1, Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(0)        

        self.frame.setLayout(layout)

    def getFrame(self):
        '''
        Getter for frame
        '''
        return self.frame