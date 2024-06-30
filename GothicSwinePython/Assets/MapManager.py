import random
import pandas as pd
import numpy as np

import Database.DBAccess as DBAccess, Assets.Room as Room, Assets.NPC as NPC
import Data.Hints as Hints

class MapManager(object):
    '''
    A class for map generation and management 

    Attributes:
        map (DataFrame): Holds the elements of the map
        roomList (List): Holds all Room objects in map
        NPCList (List): Holds all NPC objects in map
        villain (NPC): Holds who the villain is
        currentRoom (Room): Holds the current room
        hintHolder (List): Holds all possible hints in first element, villain hints in second
        hints (List): List of strings with normal hints
        villainHints (List): List of string with villain lie hints
    ''' 
    # Initializes blank map
    map = pd.DataFrame({
        0: [None, None, None, None, None],
        1: [None, None, None, None, None],
        2: [None, None, None, None, None],
        3: [None, None, None, None, None],
        4: [None, None, None, None, None]
    })

    def __init__(self):
        # Initialize class variables
        self.roomList = []
        self.NPCList = []
        self.villain = None
        self.buildRoomList() # Selects random rooms and creates and assigns NPCs
        self.buildMap() # Inits the map
        self.populateConnectedRooms() # Builds room connections
        self.pickVillain() # selects a villain
        self.currentRoom = self.roomList[0] # Sets current room to 0, foyer

        hintHolder = Hints.generateAndReturnHints(self.villain)
        self.hints = hintHolder[0]
        self.villainHints = hintHolder[1]
        self.assignHints() 

    def __del__(self):
        '''
        Destructor
        '''
        print("Map deleted")

    def setCurrentRoom(self, Room):
        '''
        Setter for currentRoom
        '''
        self.currentRoom = Room

    def getCurrentRoom(self):
        '''
        Getter for current Room
        '''
        return self.currentRoom
    
    def setVillain(self, villain):
        '''
        Setter for villain
        '''
        self.villain = villain
    
    def getVillain(self):
        '''
        Getter for villain
        '''
        return self.villain

    def buildRoomList(self):
        '''
        Method to initialize the rooms in the map. Will create an NPC per room as well,
        and put them in the room. Will not assign them to DataFrame yet
        '''
        # Random number of rooms within range
        numRooms = random.randint(9, 13)

        # Pull all rooms from MongoDB Rooms collection and store the list of dicts in roomImportList
        roomDB = DBAccess.DBAccess("Rooms", False)
        roomImportList = roomDB.read({})
        roomDB.closeConnection()

        # Pull all NPCs from MongoDB Characters collection and store the list of dicts in npcImportList
        npcDB = DBAccess.DBAccess("Characters", False)
        ncpImportList = npcDB.read({})
        npcDB.closeConnection()

        # Runs once per room
        for x in range(numRooms):
            # Creates new room from first element. (First run will always be Foyer, default room)
            newRoom = Room.Room(roomImportList[0])
            roomImportList.pop(0) # Removes first element
            
            # Creates new NPC from first element. (First run will always be Constable Eli, default room)
            newNPC = NPC.NPC(ncpImportList[0])
            ncpImportList.pop(0) # Removes first element
            newRoom.addCharacterToRoom(newNPC)

            # Append class lists
            self.roomList.append(newRoom)
            self.NPCList.append(newNPC)

            # Shuffles working lists for randomization
            random.shuffle(ncpImportList)
            random.shuffle(roomImportList)

    def buildMap(self):
        '''
        Method to put rooms from roomList into map
        '''
        # Serves to get possible connections by looking at where the last room could connect
        previousRoom = None

        # Iterates over roomList
        for room in self.roomList:
            # Foyer, the first room, places in a fairly specific place
            if room.getRoomName() == "Foyer": 
                previousRoom = room
                self.map.loc[4, random.randint(2, 3)] = room
                
                room.setCoords([4, random.randint(2, 3)])
                room.setConnectedRooms(self.calculateConnections(room))

                self.currentRoom = room
            else:
                possiblePositions = self.calculateConnections(previousRoom) # possible positions to go
                roomPlaced = False # control for while loop

                # Will run until a room is placed
                while not roomPlaced:
                    # 4 is arbitrary, but keeps it from trying for too long
                    for x in range(4):
                        # In case possiblePosition returns empty (Which happens sometimes), sets it to a random room's connections
                        if not possiblePositions:
                            fixRoom = random.choice(self.roomList)
                            possiblePositions = self.calculateConnections(fixRoom)
                            previousRoom = fixRoom
                            print("error catch ran")
                            continue
                        test = random.choice(possiblePositions) # test is used to pick a position to place and test it
                        if list(test.keys())[0] == "Invalid Location":
                            continue
                        # None is good. It means the space is open to place a room
                        if list(test.keys())[0] == None: 
                            self.map.loc[list(test.values())[0][0], list(test.values())[0][1]] = room
                            room.setConnectedRooms(self.calculateConnections(room))
                            room.setCoords([list(test.values())[0][0], list(test.values())[0][1]])
                            previousRoom = room
                            roomPlaced = True
                            break
 
                    # If the first loop times out, this is a catch in order to try again at a random room's location
                    for connection in possiblePositions:
                        if list(connection.keys())[0] != None:
                            fixRoom = random.choice(self.roomList)
                            possiblePositions = self.calculateConnections(fixRoom)
                            previousRoom = fixRoom

                                                

    def calculateConnections(self, room):
        '''
        Method to calculate room's possible connections
        '''
        connectionsList = []
        cellLoc = self.findCellLocationByValue(room)

        # Run 4 times, the theoretical number of connections
        for x in range(4):
            newCoords = [5, 5] # newCoords will set a room's position. 5,5 is out of range, and denotes a room out of range
            # Error check to ensure that the indices are within range
            if cellLoc[0] < 0 or cellLoc[0] >= 5 or cellLoc[1] < 0 or cellLoc[1] >= 5:
                continue
            # Match case. Determines which direction the room is in, and adds that to connectionsList
            match x:
                case 0: # North
                    if cellLoc[0] - 1 >= 0:
                        newCoords = [cellLoc[0] - 1, cellLoc[1]]
                        connectionsList.append({self.map.loc[newCoords[0], newCoords[1]]: newCoords})
                    else:
                        connectionsList.append({"Invalid Location": newCoords})
                case 1: # East
                    if cellLoc[1] + 1 < 5:
                        newCoords = [cellLoc[0], cellLoc[1] + 1]
                        connectionsList.append({self.map.loc[newCoords[0], newCoords[1]]: newCoords})
                    else:
                        connectionsList.append({"Invalid Location": newCoords})
                case 2: # South
                    if cellLoc[0] + 1 < 5:
                        newCoords = [cellLoc[0] + 1, cellLoc[1]]
                        connectionsList.append({self.map.loc[newCoords[0], newCoords[1]]: newCoords})
                    else:
                        connectionsList.append({"Invalid Location": newCoords})
                case 3: # West
                    if cellLoc[1] - 1 >= 0:
                        newCoords = [cellLoc[0], cellLoc[1] - 1]
                        connectionsList.append({self.map.loc[newCoords[0], newCoords[1]]: newCoords})
                    else:
                        connectionsList.append({"Invalid Location": newCoords})
        
        return connectionsList
    
    def populateConnectedRooms(self):
        '''
        Method to set a room's connected rooms
        '''
        for room in self.roomList:
            room.setConnectedRooms(self.calculateConnections(room))
    
    def findCellLocationByValue(self, room):
        '''
        Method to return a cell's location based on room name
        '''
        for x in range(5):
            for y in range(5):
                if self.map.loc[x, y] == room:
                    return [x, y]
        return [5, 5]
                
    def findValueByCellLocation(self, cellLocation):
        '''
        Method to return a cell's value by coordinates
        '''
        return self.map.iat[cellLocation[0], cellLocation[1]]
    
    # The following 4 methods handle movements in stated directions.
    # Finds which room is in that direction, and sets that room to currentRoom
    def moveNorth(self):
        newRoom = self.currentRoom.getConnectedRoomByDirection('North')
        self.setCurrentRoom(newRoom[0])

    def moveEast(self):
        newRoom = newRoom = self.currentRoom.getConnectedRoomByDirection('East')
        self.setCurrentRoom(newRoom[0])
    
    def moveSouth(self):
        newRoom = newRoom = self.currentRoom.getConnectedRoomByDirection('South')
        self.setCurrentRoom(newRoom[0])

    def moveWest(self):
        newRoom = newRoom = self.currentRoom.getConnectedRoomByDirection('West')
        self.setCurrentRoom(newRoom[0])

    def printMap(self):
        '''
        Method to print the map
        '''
        for col in range(5):
            printString = '| '
            for row in range(5):
                if self.map.loc[col][row] == None:
                    printString += "Empty | "
                else:
                    printString += self.map.loc[col][row].getRoomName() + " | "
            print(printString)
        
    def pickVillain(self):
        '''
        Method to randomly select a villain, excluding the Constable
        '''
        self.villain = random.choice(self.NPCList[1 : len(self.NPCList) - 1])

    def assignHints(self):
        '''
        Method to assign hints to all NPC's in the map
        '''
        newHintsList = [x for x in self.hints]

        random.shuffle(newHintsList)

        for NPC in self.NPCList:
            if NPC.getCharacterName() == self.villain.getCharacterName():
                NPC.setHintToGive(random.choice(self.villainHints))
            else:
                NPC.setHintToGive(newHintsList[0])
                newHintsList.pop(0)