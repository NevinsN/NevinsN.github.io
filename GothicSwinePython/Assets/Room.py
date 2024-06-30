class Room(object):
    '''
    A class creating a Room item

    Parameters:
        roomDict (Dictionary): Contains the information for a room as retrieved from MongoDB Collection

    Attributes:
        roomName (string): Contains room's name
        roomDescription (string): Contains description of the room
        charactersInRoom (List): Holds all characters in room. Initialized as empty, because we need to generate the map first
        connectedRooms (Dictionary): Holds connections to other rooms, including empty slots and invalid locaitons. Initialized as empty, because we need to generate the map first
        coords (List): Coordinates of the room on the dataframe. Initialized as empty, because we need to generate the map first
    '''
    def __init__(self, roomDict):
            # Initialize claa variables
            self.roomName = roomDict.get("roomName")
            self.roomDescription = roomDict.get("roomDescription")
            self.charactersInRoom = []
            self.connectedRooms = {}
            self.coords = []

    def getRoomID(self):
        '''
        Getter for roomID
        '''
        return self.roomID
    
    def setRoomName(self, roomName):
        '''
        Setter for roomName
        '''
        self.roomName = roomName
    
    def getRoomName(self):
        '''
        Getter for roomName
        '''
        return self.roomName

    def setRoomDescription(self, roomDescription):
        '''
        Setter for roomDescription
        '''
        self.roomDescription = roomDescription

    def getRoomDescription(self):
        '''
        Getter for roomDescription
        '''
        return self.roomDescription
    
    def setCoords(self, coords):
        '''
        Setter for coords
        '''
        self.coords = coords

    def getCoords(self):
        '''
        Getter for coords
        '''
        return self.coords
    
    def addCharacterToRoom(self, character):
        '''
        Method to add character to a room
        '''
        self.charactersInRoom.append(character)

    def removeCharacterFromRoom(self, character):
        '''
        Method to remove character from a room
        '''
        self.charactersInRoom.remove(character)

    def getCharactersInRoom(self):
        '''
        Getter for charactersInRoom
        '''
        return self.charactersInRoom

    def setConnectedRooms(self, connections):
        '''
        Setter for connected rooms. 
        Takes connections, and iterates through in order 
        to build the connections dictionary
        '''
        connKeys = []
        for conn in connections:
            connKeys.append(list(conn.keys()))
        self.connectedRooms = {
            'North' : connKeys[0],
            'East'  : connKeys[1],
            'South' : connKeys[2],
            'West'  : connKeys[3]
        }

    def getConnectedRooms(self):
        '''
        Getter for connectedRooms
        '''
        return self.connectedRooms

    def getConnectedRoomByDirection(self, direction):
        '''
        Method to get connection in a specific direction
        '''
        return self.connectedRooms.get(direction)

            
