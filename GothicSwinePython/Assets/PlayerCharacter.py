
class PlayerCharacter(object):
    '''
    A class creating a PlayerCharacter item

    Attributes:
        notes (Dicitonary): Contains notes collected by player

    More funcitonality could be built here. Very simple for now
    '''
    def __init__(self):
        # Initialize class variables
        self.notes = {}

    def appendToNotes(self, noteDictionary):
        '''
        Appends new note to notes
        '''
        self.notes.update(noteDictionary)

    def getNotes(self):
        '''
        Getter for notes
        '''
        return self.notes
    
    def examineCharacter(self, npc):
        '''
        Method to examine a character (npc)
        '''
        # textToReturn is a string that is built on and returned
        textToReturn = npc.getCharacterName() # character name
        
        # Build line for an apparel item
        # For gramatical formating. if plural, else if a vowel, else
        if npc.getApparel().getWholeItem()[len(npc.getApparel().getWholeItem()) - 1:] == 's':
            textToReturn += " is wearing "
        elif self.isVowel(npc.getApparel().getWholeItem()[0]):
            textToReturn += " is wearing an "
        else:
            textToReturn += " is wearing a "
        textToReturn += npc.getApparel().getWholeItem()
        
        # Build line for an accessory item
        # For gramatical formating. if plural, else if a vowel, else
        if npc.getAccessory().getWholeItem()[len(npc.getAccessory().getWholeItem()) - 1:] == 's':
            textToReturn += ", "
        elif self.isVowel(npc.getAccessory().getWholeItem()[0]):
            textToReturn += ", an "
        else:
            textToReturn += ", a "
        textToReturn += npc.getAccessory().getWholeItem()

        # Build line for a flair item
        # For gramatical formating. if plural, else if a vowel, else
        if npc.getFlair().getWholeItem()[len(npc.getFlair().getWholeItem()) - 1:] == 's':
            textToReturn += ", and "
        elif self.isVowel(npc.getFlair().getWholeItem()[0]):
            textToReturn += ", and an "
        else:
            textToReturn += ", and a "
        textToReturn += npc.getFlair().getWholeItem()     

        return textToReturn

    def questionCharacter(self, npc):
        '''
        Method to add npc's hint to notes
        '''
        self.appendToNotes({npc: npc.getHintToGive()})

    def isVowel(self, character):
        '''
        Method to check if a character is a vowel
        '''
        match character:
            case 'a':
                return True
            case 'e':
                return True
            case 'i':
                return True
            case 'o':
                return True
            case 'u':
                return True
            case _:
                return False
