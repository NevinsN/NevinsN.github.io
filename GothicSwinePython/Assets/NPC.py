import Assets.Item as Item

class NPC(object):
    '''
    A class creating an NPC item

    Parameters:
        npcDict (Dictionary): Contains the information for a room as retrieved from MongoDB Collection

    Attributes:
        apparel (Item): Contains NPC's apparel item
        accessory (Item): Contains NPC's accessory item
        flair (Item): Contains NPC's flair item
        hintToGive (string): Contains the hint a character gives the player, initialized as empty, because we need to generate the map first 
        characterName (string): Coordinates of the room on the dataframe. Initialized as empty, because we need to generate the map first
    '''
    def __init__(self, npcDict):
        # Initialize class variables
        self.apparel = Item.Item("apparel")
        self.accessory = Item.Item("accessory")
        self.flair = Item.Item("flair")
        self.hintToGive = ''
        self.characterName = npcDict.get('name')

    def setCharacterName(self, characterName):
        '''
        Setter for characeterName
        '''
        self.characterName = characterName

    def getCharacterName(self):
        '''
        Getter for characterName
        '''
        return self.characterName
    
    def setApparel(self, apparel):
        '''
        Setter for apparel
        '''
        self.apparel = apparel

    def getApparel(self):
        '''
        Getter for apparel
        '''
        return self.apparel
    
    def setAccessory(self, accessory):
        '''
        Setter for accessory
        '''
        self.accessory= accessory

    def getAccessory(self):
        '''
        Getter for accessory
        '''
        return self.accessory
    
    def setFlair(self, flair):
        '''
        Setter for flair
        '''
        self.flair = flair

    def getFlair(self):
        '''
        Getter for flair
        '''
        return self.flair
    
    def setHintToGive(self, hintToGive):
        '''
        Setter for hintToGive
        '''
        self.hintToGive = hintToGive

    def getHintToGive(self):
        '''
        Getter for hintToGive
        '''
        return self.hintToGive
    
    def printCharacterData(self):
        '''
        Method to print character's information, mostly for testing
        '''
        print(self.getCharacterName()) 
        print(self.getAccessory().getWholeItem()) 
        print(self.getApparel().getWholeItem()) 
        print(self.getFlair().getWholeItem())
        print(self.getHintToGive())
        print(self.getGuiltyHintList())