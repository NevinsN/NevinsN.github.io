import random

'''
    A classless one-off module to handle hints generation

    Parameters:
        NPC (NPC): Character to examine for hints 

    Attributes:
        apparel (Item): NPC's apparel
        accessory (Item): NPC's accessory
        flair (Item): NPC's flair
        hints (List): Holds all hints
        villainHints (List): Holds lies told by the villain
        itemHolder (List): Holds the items in a dicitionary format
    ''' 

def generateAndReturnHints(NPC):
    # Initialize variables
    apparel = NPC.getApparel()
    accessory = NPC.getAccessory()
    flair = NPC.getFlair()
    hints = []
    villainHints = []
    itemHolder = [{apparel: []}, {accessory: []}, {flair: []}]

    # Sets values for itemHolda
    for dictionary in itemHolder:
        for item, qualities in dictionary.items():
            qualities.append(item.getColor())
            qualities.append(item.getDesign())
            qualities.append(item.getBaseItem())

    # Initializes all the hints for non-villain characters with string formatting
    randNum = returnRandNum(3)
    hints.append("I could swear I saw the fiend with a {color} {baseItem}!".format(color = list(itemHolder[randNum].values())[0][0], baseItem = list(itemHolder[randNum].values())[0][2]))
    
    choices = returnTwoChoicesByInt(itemHolder, 1, False, NPC)
    hints.append("I'm pretty sure the murderer was sporting some {} or {}.".format(choices[0], choices[1]))
    
    choices = returnTwoChoicesByInt(itemHolder, 2, False, NPC)
    hints.append("I think I saw a {} as the perpetrator fled the scene. Unless it was a {}".format(choices[0], choices[1]))
    
    hints.append("I'm positive it wasn't me!")
    
    choices = returnTwoChoicesByInt(itemHolder, 2, False, NPC)
    hints.append("Shoot, was it a {}, or {}? I know the murderer wore one of those!".format(choices[0], choices[1]))

    hints.append("I don't talk to police. Yes, I know that makes me sound suspicious.")

    hints.append("I could really go for some ice cream.")

    choices = returnTwoChoicesByInt(itemHolder, 2, False, NPC)
    hints.append("Definitely wore a {}. Or maybe a {}.".format(choices[0], choices[1]))

    randNum = returnRandNum(3)
    hints.append("Whoever it is must love {design}!".format(design = list(itemHolder[randNum].values())[0][1]))

    randNum = returnRandNum(3)
    if returnRandNum(2) == 0:
        item = list(itemHolder[randNum].values())[0][2]
    else:
        item = getRandomBaseItem(False, NPC)
    hints.append("Try someone wearing a {}, but I could be wrong.".format(item))

    choices = returnTwoChoicesByInt(itemHolder, 0, False, NPC)
    hints.append("I know I saw a bit of {} or {}.".format(choices[0], choices[1]))

    randNum = returnRandNum(3)
    hints.append("I've never seen such a unique use of {} before.".format(list(itemHolder[randNum].values())[0][1]))

    randNum = returnRandNum(3)
    hints.append("I saw {} everywhere!".format(list(itemHolder[randNum].values())[0][1]))

    randNum = returnRandNum(3)
    hints.append("I wasn't there personally, but I sense the villain makes good use of the color {}.".format(list(itemHolder[randNum].values())[0][0]))

    randNum = returnRandNum(3)
    if returnRandNum(2) == 0:
        itemOne = list(itemHolder[randNum].values())[0][1]
    else:
        itemOne = getRandomDesign(False, NPC)
    if returnRandNum(2) == 0:
        itemTwo = list(itemHolder[randNum].values())[0][2]
    else:
        itemTwo = getRandomBaseItem(False, NPC)
    hints.append("Surely a great detective like you doesn't need me to tell you about the {} {} I saw? I'm sure I'm too smart to be wrong".format(itemOne, itemTwo))

    #These are the statements for the villain. All should be lies.
    villainHints.append("I could swear I saw the fiend with a {color} {baseItem}!".format(color = getRandomColor(True, NPC), baseItem = getRandomBaseItem(True, NPC)))
    
    villainHints.append("I'm pretty sure the murderer was sporting some {}.".format(getRandomDesign(True, NPC)))
    
    villainHints.append("I think I saw a {} as the perpetrator fled the scene.".format(getRandomBaseItem(True, NPC)))
    
    villainHints.append("Shoot, was it a {}, or {}? I know the murderer wore one of those!".format(getRandomBaseItem(True, NPC), getRandomBaseItem(True, NPC)))

    villainHints.append("Definitely wore a {}. Or maybe a {}.".format(getRandomBaseItem(True, NPC), getRandomBaseItem(True, NPC)))

    villainHints.append("Whoever it is must love {}!".format(getRandomDesign(True, NPC)))

    villainHints.append("Try someone wearing a {}, but I could be wrong.".format(getRandomBaseItem(True, NPC)))
    
    villainHints.append("I know I saw a bit of {} or {}.".format(getRandomColor(True, NPC), getRandomColor(True, NPC)))

    villainHints.append("I've never seen such a unique use of {} before.".format(getRandomDesign(True, NPC)))

    villainHints.append("I saw {} everywhere!".format(getRandomDesign(True, NPC)))

    villainHints.append("I wasn't there personally, but I sense the villain makes good use of the color {}.".format(getRandomColor(True, NPC)))

    villainHints.append("Surely a great detective like you doesn't need me to tell you about the {} {} I saw?".format(getRandomDesign(True, NPC), getRandomBaseItem(True, NPC)))

    return [hints, villainHints]

def returnTwoChoicesByInt(itemHolder, indexNum, isVillain, villain):
    '''
    Method to return one true item and one random item. 
    It checks to ensure they are different, and shuffles them
    so the true item in the hint is not always in the same position
    '''
    randNum = returnRandNum(3)
    if returnRandNum(2) == 0:
        one = list(itemHolder[randNum].values())[0][indexNum]
        match indexNum:
            case 0:
                two = getRandomColor(isVillain, villain)
                while two == one:
                    two = getRandomColor(isVillain, villain)
            case 1:
                two = getRandomDesign(isVillain, villain)
                while two == one:
                    two = getRandomDesign(isVillain, villain)
            case 2:
                two = getRandomBaseItem(isVillain, villain)
                while two == one:
                    two = getRandomBaseItem(isVillain, villain)
    else:
        two = list(itemHolder[randNum].values())[0][indexNum]
        match indexNum:
            case 0:
                one = getRandomColor(isVillain, villain)
                while one == two:
                    one = getRandomColor(isVillain, villain)
            case 1:
                one = getRandomDesign(isVillain, villain)
                while one == two:
                    one = getRandomDesign(isVillain, villain)
            case 2:
                one = getRandomBaseItem(isVillain, villain)  
                while one == two: 
                    one = getRandomBaseItem(isVillain, villain)       

    return [one, two]

def returnRandNum(numChoices):
    '''
    Method to return random number in a range
    numChoices is the total number of choices. It subtracts 1 for use as an index
    '''
    return random.randint(0, numChoices - 1)

def getRandomColor(isVillain, villain):
    '''
    Method to return a random color from list
        isVillain tells if this is being generated for the villain
        villain is an NPC object to grab items
        Villain will not select own color
    '''
    color = [
            "black",
            "blue",
            "crimson",
            "gold",
            "green",
            "ivory",
            "maroon",
            "orange",
            "pink",
            "purple",
            "red",
            "silver",
            "teal",
            "white",
            "yellow"
    ]

    if isVillain:
        for test in color:
           if test == villain.getApparel().getColor():
               color.remove(test)
        for test in color:
           if test == villain.getAccessory().getColor():
               color.remove(test)
        for test in color:
           if test == villain.getFlair().getColor():
               color.remove(test)           

    return random.choice(color)

def getRandomDesign(isVillain, villain):
    '''
    Method to return a random design from list
        isVillain tells if this is being generated for the villain
        villain is an NPC object to grab items
        Villain will not select own design
    '''
    design = [
        "floral",
        "houndstooth",
        "damask",
        "striped",
        "buffalo check",
        "plaid",
        "pin striped",
        "harringbone",
        "paisley",
        "gingham",
        "polka dot",
        "twill",
        "checkered",
        "argyle",
        "celtic knot",
    ]

    if isVillain:
        for test in design:
           if test == villain.getApparel().getDesign():
               design.remove(test)
        for test in design:
           if test == villain.getAccessory().getDesign():
               design.remove(test)
        for test in design:
           if test == villain.getFlair().getDesign():
               design.remove(test)

    return random.choice(design)

def getRandomBaseItem(isVillain, villain):
    '''
    Method to return a random baseItem from list
        isVillain tells if this is being generated for the villain
        villain is an NPC object to grab items
        Villain will not select own baseItem
    '''
    baseItems = [
        "cardigan",	
        "bolo tie",	
        "beret",
        "gown",	
        "bowtie",	
        "bonnet",
        "kilt",	
        "bracelet",	
        "cane",
        "cowboy boots",	
        "brooch",
        "fanny pack",
        "leggings",	
        "eyeglasses",	
        "fedora",
        "poncho",	
        "fascinator",	
        "headband",
        "cloak",	
        "handkerchief",	
        "panama hat",
        "sundress",
        "lapel pin",	
        "parasol",
        "riding boots",
        "pendant", 
        "sash",
        "slippers",	
        "pocket square",	
        "shawl",
        "overalls",	
        "pocket watch",	
        "umbrella",
        "sweater",	
        "tiara",	
        "veil",
        "sweater vest",	
        "boutonniere",	
        "waistcoat",
        "hoodie",	
        "fan",	
        "cap",
        "windbreaker",	
        "boa",	
        "walking stick"
        ]
    
    if isVillain:
        for test in baseItems:
           if test == villain.getApparel().getBaseItem():
               baseItems.remove(test)
        for test in baseItems:
           if test == villain.getAccessory().getBaseItem():
               baseItems.remove(test)
        for test in baseItems:
           if test == villain.getFlair().getBaseItem():
               baseItems.remove(test)
    
    return random.choice(baseItems)