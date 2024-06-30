import pandas as pd

import Database.DBAccess as DBAccess

class CreateDBItems(object):
    '''
    A class to update teh Items collection

    Parameters:
        dataCSV (string): Name of csv file to upload

    Attributes:
        _df (Pandas DataFrame): DataFrame to hold CSV data
        _Categories (List): List of category names
    '''
    
    _df = pd.DataFrame()
    _Categories = []

    def __init__(self, dataCSV):
        # Initialize class variables
        self._df = pd.read_csv(dataCSV)
        self._Categories = self._df.columns.values

        self.buildDBEntries()

    def buildDBSchema(self, type, color, design, baseItem):
        '''
        Method to build the DB query
        '''
        query = {
            "type": type,
            "color": color,
            "design": design,
            "baseItem": baseItem
        }

        return query
    
    def buildDBEntries(self):
        '''
        Method to submit requests to the database
        '''
        # Initializes the database
        db = DBAccess.DBAccess("Items", True)
        db.delete({})

        # Builds a list for accessory, apparel, and flair to upload
        accessoryList = self.buildSchemasForType("accessory")
        apparelList = self.buildSchemasForType("apparel")
        flairList = self.buildSchemasForType("flair")

        # Upload accessories
        for x in accessoryList:
            db.create(x)

        # Upload apparel
        for x in apparelList:
            db.create(x)

        # Upload flair
        for x in flairList:
            db.create(x)

        print("DB Loading finished")
        db.closeConnection()

    def buildSchemasForType(self, type):
        '''
        Method to set suspectSelection
        '''
        # List to output
        outputList = []

        # Gets baseItem, color, and design from _df and stores in unique variables
        baseItemInit = self._df.loc[:, type]
        colorInit = self._df.loc[:, "color"]
        designInit = self._df.loc[:, "design"]

        # Loops through baseItemInit and appends a db schema for the complete item to outputList
        for x in baseItemInit:
            if pd.isna(x):
                continue
            else:
                for y in colorInit:
                    if pd.isna(y):
                        continue
                    else:
                        for z in designInit:
                            if pd.isna(z):
                                continue
                            else:
                                outputList.append(self.buildDBSchema(type, y, z, x))

        return outputList