# -*- coding: utf-8 -*-
from pymongo import MongoClient

class DBAccess(object):
    '''
    A class for the attempt to solve dialog box

    Parameters:
        collection (string): String to determine whiche collection to access
        adminLogin (bool): Determines if user has admin privledges or not

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

    def __init__(self, collection, adminLogin):
        # Initializing the MongoClient. This is hardwired to access the database
        # from within any game client. In future updates, a proper authorizaiton
        # system for unique user access might be implemented.
        #
        # The game system can only read databases in the GothicSwineDB
        # database
        
        #
        # Connection Variables
        #
        DB = "GothicSwineAssets"
        COL = collection
        
        #
        # Initialize Connection
        #
        if adminLogin:
            self.cluster = MongoClient("mongodb+srv://TGNiklaus:H00p3rman@gothicswinedb.xogt6d5.mongodb.net/?retryWrites=true&w=majority&appName=GothicSwineDB")
        else:
            self.cluster = MongoClient("mongodb+srv://playerClient:SlMK9ptcZJcn34oc@gothicswinedb.xogt6d5.mongodb.net/?retryWrites=true&w=majority&appName=GothicSwineDB")
        self.database = self.cluster[DB]
        self.collection = self.database[COL]
        #print("MongoDB database connected")

    # Method to implement the C in CRUD.
    def create(self, data):
        if data: 
            self.collection.insert_one(data)  # data should be dictionary            
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

    # Method to implement the R in CRUD.
    def read(self, data):
        if data:
            result = self.collection.find(data)
            return list(result)
        else:
            result = self.collection.find({})
            return list(result)
            
    # Method to implement the U in CRUD
    def update(self, data, updateData):
        if data and updateData:
            result = self.collection.update_many(data, {"$set": updateData})
            return result
        else:
            return set()
            
    # Method to implement the D in CRUD
    def delete(self, data):
        if data:
            result = self.collection.delete_many(data)
            return result
        else:
            return set()
        
    # Method to get a random document from collection
    def getRandomSamplingOfValue(self, data):
        if data:
            result = self.collection.aggregate(data)
            return list(result)
        else:
            result = self.collection.find({})
            return list(result)
        
    # Method to close database connection
    def closeConnection(self):
        self.cluster.close()

    