# -*- coding: utf-8 -*-
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, *args):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        
        if len(args) < 1:
            USER = 'aacuser'
            PASS = 'userpass'
        else:
            USER = args[0]
            PASS = args[1]
        
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31057
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connectio
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]             

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data: 
            self.database.animals.insert_one(data)  # data should be dictionary            
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD.
    def read(self, data):
        if data:
            result = self.database.animals.find(data)
            return list(result)
        else:
            result = self.database.animals.find({})
            return list(result)
        
# Create method to implement the U in CRUD
    def update(self, data, updateData):
        if data and updateData:
            result = self.database.animals.update_many(data, {"$set": updateData})
            return result
        else:
            return set()
        
# Create method to implement the D in CRUD
    def delete(self, data):
        if data:
            result = self.database.animals.delete_many(data)
            return result
        else:
            return set()
        
        
        
            
        