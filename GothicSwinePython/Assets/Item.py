import Database.DBAccess as DBAccess

class Item(object):  
    '''
    A class creating an Item item

    Parameters:
        type (string): Denotes what type of item to generate (Apparel, Accessory, or Flair)

    Attributes:
        type (string): The type of item to create
        color (string): The color of the item
        design (string): The design of the item
        baseItem (string): The baseItem the item is built upon
    '''
    def __init__(self, type):
        # Initialize class variables
        self.type = type
        self.color = None
        self.design = None
        self.baseItem = None

        # runs to populate based off of type
        self.initializeItem()

    def setType(self, type):
        '''
        Setter for type
        '''
        self.type = type

    def getType(self):
        '''
        Getter for type
        '''
        return self.type

    def setColor(self, color):
        '''
        Setter for color
        '''
        self.color = color

    def getColor(self):
        '''
        getter for color
        '''
        return self.color
    
    def setDesign(self, design):
        '''
        Setter for design
        '''
        self.design = design
    
    def getDesign(self):
        '''
        Getter for design
        '''
        return self.design
    
    def setBaseItem(self, baseItem):
        '''
        Setter for baseItem
        '''
        self.baseItem = baseItem

    def getBaseItem(self):
        '''
        Getter for baseItem
        '''
        return self.baseItem
    
    def getWholeItem(self):
        '''
        Getter for a whole item string
        '''
        return self.getColor() + " " + self.getDesign() + " " + self.getBaseItem()
        
    def initializeItem(self):
        '''
        Method to initialize an item's variables
        '''
        # Calls MongoDB database for Items collection
        itemDB = DBAccess.DBAccess("Items", False)
        
        # Extracts a random document by type
        itemData = itemDB.getRandomSamplingOfValue([
            {'$match': {'type': self.getType()}},
            {'$sample': {'size': 1}}
        ])
        itemDB.closeConnection()

        # Sets item variables
        self.setColor(itemData[0].get('color'))
        self.setDesign(itemData[0].get('design'))
        self.setBaseItem(itemData[0].get('baseItem'))
        
        

