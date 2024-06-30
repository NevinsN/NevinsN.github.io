# allows use of today's date
from datetime import date
# from title_screen import print_title
import time

# function that checks if a year is a leap year
def leap_year_check(year):
    # initializes variable
    leap_year_status = 0
    
    # checks if the year is an even hundred such as 1800 then tests if it's divisible by 400
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year_status = 1
        else:
            leap_year_status = 0
    
    # checks if the year is divisible by 4
    elif year % 4 == 0:
        leap_year_status = 1
 
    else:
        leap_year_status = 0
        
    return leap_year_status             
            
# function that calculates a date from another formatted as YYYY-MM-DD
def find_new_date(first_date, modifier):
    # establishes pertinent variables
    month_holder = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    month_end = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    new_date = ''
    leap_check = ''
   
   # divides the inserted date into a container and converts the day and month into numbers
    date_str = str(first_date)
    date_holder = date_str.split('-')
    date_holder[2] = int(date_holder[2]) + modifier
    date_holder[1] = int(date_holder[1])
    date_holder[0] = int(date_holder[0])

    # a while loop that handles subtracting days
    while date_holder[2] < 1:
        date_holder[2] += month_end[date_holder[1] - 1]
        date_holder[1] -= 1
        
        if date_holder[1] < 1:
            date_holder[1] = 12
            date_holder[0] -= 1
            
            leap_check = leap_year_check(date_holder[0])
            if leap_check == 1:
                month_end[1] = 29
            else:
                month_end[1] = 28
    
    # a while loop that handles adding days        
    while date_holder[2] > month_end[date_holder[1] - 1]:
        date_holder[2] -= month_end[date_holder[1] - 1]
        date_holder[1] += 1
        
        if date_holder[1] > 12:
            date_holder[1] = 1
            date_holder[0] += 1
            
            leap_check = leap_year_check(date_holder[0])
            if leap_check == 1:
                month_end[1] = 29
            else:
                month_end[1] = 28
  
    # builds the correct month and day into a 'January 01, 2022' format
    new_date = month_holder[date_holder[1] - 1] + ' ' + str(date_holder[2]) + ' ' + str(date_holder[0])
   
    return new_date

# in place so 1) players can appreciate my start screen and 2) players can have an option to quit
def title_screen_input():
    start_input = input('        Press Enter to Play or Type C to Quit: ')

    if start_input == '':
        time.sleep(1)
    elif start_input == 'C':
        quit()
    else:
        print('Invalid Entry.')
        title_screen_input()

# simply prints the title screen, will display at start up and game over
def title_screen_generate():
    print_title()
    time.sleep(3)
    title_screen_input()

# just a little something to save on typing and keep the game easy to follow visually
def separator():
    separator = '\n*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n'
    print(separator)
    time.sleep(1)

def move_room(location, move_input):
	
	'''
	possible_moves is set to all possible moves from each room by hand. Since there are only 9
	rooms, that means that 0-8 will cover each room, while 9 represents an invalid move.
	This is rigid for this specific map configuration, in the order of North, East, South, West.
	'''
	possible_moves = {0: 3291, 
					  1: 9099, 
					  2: 9990,
					  3: 6804,
					  4: 5399,
					  5: 9649,
					  6: 9735,
					  7: 9986,
					  8: 7993,
					  }

	# directions are reversed, since the numbers that make up a room's possible moves will be 
	# reversed once they are divided in a later step
	direction_test = ['West', 'South', 'East', 'North']

	# irrelevant if it goes right the first time, but necessary if an invalid input or direction 
	# is entered and the function has to call again
	if move_input not in direction_test:
			print('Invalid entry. Try again.')
			return player_location
	else:
		# move_holder will hold each possible move for each room as an individual integer
		move_holder = []
		move_test = possible_moves[location]
		
		# this loop will chop up move_test and store it in move_holder in reverse order as individual ints
		while move_test > 0:
			move_temp = [move_test % 10]
			move_holder += move_temp
			move_test = move_test // 10
		
		direction_check = direction_test.index(move_input)

		'''
		direction_check is essential, because it gets an index number to feed into move_holder,
		essentially selecting which room will be moved to. Since 9 is the code for no room,
		we use this if statement to make sure the new room exists. If it is an invalid move,
		the else statement gets new input and starts the function over.
		'''
		if move_holder[direction_check] != 9:
			location = move_holder[direction_check]
			return location
		else:
			print('There is no room in that direction. Try again.')
			return location
              
def get_item(player_inventory, location, evidence_list, character_list):
    if evidence_list[location] == 1:
        temp = '{}\'s statement'.format(character_list[location])
        print('Picked up', temp, end='!\n')
        player_inventory += [temp]
        evidence_list[location] = 0
        print(temp)
        return player_inventory
    else:
        print('No witness statement to collect!')
        return player_inventory

def intro_para():
    title_screen_generate()

    # grabs the player's name
    separator()
    player_name = input('Please enter your name: ')
    while player_name == '':
        player_name = input('Please enter a valid name: ')

    separator()
    print('\n' + player_name + ', I\'m glad you\'ve come.\n', 
          '\nLast night, the evening of', mystery_date + ',', 
          'the world-renowned \nsinger Abigail Piper went missing from a small gathering \nat her gothic manor house!\n')

    print('I\'ve detained all the guests in separate rooms to await \ninvestigators.\n', 
          '\nSince the police sent you ahead, gather all of the six \npieces of evidence and await the arrival of the constables.\n')

    print('But be careful! One of the guests is surely responsible, \nand if you try to confront the culprit without all the \nevidence, you might be next!')
    print('\nGood luck,', player_name + '!')
    input('\nPress Enter to Begin: ')

    separator()

def print_title():
    
    print('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')
    print('*          /\\                                               *')
    print('*         /  \\                                              *')
    print('*        /    \\                                             *')
    print('*       /      \\                                            *')
    print('*      /   /\\   \\                                           *')
    print('*      |  |  |__|                                           *')
    print('*      |  |              __   __      _                     *')
    print('*      |  | ____   ___  _| |_ | |    / \\  ___               *')
    print('*      |  |  \\  | /   \\ \\_  _\\| |__  \\_/ /   \\              *')
    print('*      \\  \\  |  /|  |  | | |  |  _ \\ | ||  /\\/              *')
    print('*       \\  \\/  / |  |  | | |  | | \\ \\| ||  \\/\\              *')
    print('*        \\    /   \\___/  \\_/  |_| |_||_| \\___/              *')
    print('*         \\  /                                              *')
    print('*          \\/    /\\                                         *')
    print('*               /  \\                                        *')
    print('*              /    \\                                       *')
    print('*             /   |  \\                                      *')
    print('*             |   |  |                                      *')
    print('*             |   |  /                                      *')
    print('*              \\   \\/               _                       *')
    print('*               \\   \\ ___      ___ / \\ __       ___         *')
    print('*              / \\|  |\\  \\    /  / \\_/ | \\___  / _ \\        *')
    print('*             |   |  | \\  \\/\\/  /  | | | __  \\|  __/        *')   
    print('*             \\   |  /  \\  /\\  /   | | | | | ||  \\/\\        *')
    print('*              \\    /    \\/  \\/    |_| |_| |_| \\___/        *')
    print('*               \\  /                                        *')
    print('*                \\/                                         *')
    print('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n')

def instructions():
    print('As you explore the manor, you will have two commands.\n',
          'Move commands: go North, go South, go East, or go West\n',
          'Get command: get statement\n\n Good luck!')
    separator()

room_description = {0: 'Foyer:a painting of a laughing pig in \nVictorian clothing looking up, titled \"The Fool\"',
                    1: 'Sitting Room:a portrait of a finely dressed sow \nsmiling to her right, titled \"Tre Amore\"',
                    2: 'Longue:a watercolor of three piglets \nin a field, titled \"The Trilling\"',
                    3: 'Hall:a dire portrait of a pig in emperor\'s \nattire facing the right, titled \"En Tyrant\"',
                    4: 'Gallery:a watercolor of a pair of smiling pigs \nin fine gothic suits staring right, titled \"Tvillinger\"',
                    5: 'Greenhouse:a statue of a two pigs in a tight \nembrace, titled \"Elskere\"',
                    6: 'Study:a clay pot with the mural of a pig \nleaping right over another clay pot, titled \"Par Boil\"',
                    7: 'Kitchen:an ominous picture of a demonic pig \nstaring straight down, titled \"The Harbinger\"',
                    8: 'Dining Room:a grotesque mural of a pig in full armor \nstanding atop a pile of corpses, titled \"The Conquerer\"'
                   }

# retrieves today's date and finds yesterdy's with the find_new_date function
mystery_date = find_new_date(date.today(), -1)
# mystery_date removes the last 5 characters because I don't want the year for this use,
# but wanted to keep the year functionality in place for modulability for later use.
mystery_date = mystery_date[0 : -5]
character_list = ['No one', 'Isabel', 'Pietro', 'Annabel', 'Jonas', 'Kellen', 'Leonardo', 'Pamela', 'Justin']
evidence_list = {0: 0,
                 1: 1,
                 2: 1,
                 3: 1,
                 4: 1,
                 5: 1,
                 6: 1,
                 7: 1,
                 8: 0
                }
player_inventory = []
player_location = 0

# replay_state simply is used to tell if the game needs to restart on loss or not
replay_state = 0

while replay_state == 0:
    # win_state will be used to keep the game running. Once it's set to a win (1) or a loss (2), the loop exits
    win_state = 0
    intro_para()
    instructions()
    while win_state == 0:
        # room_state(player_location, room_description, character_list, evidence_list)
        temp_room = room_description[player_location].split(':')
        current_room = temp_room[0]
        current_decor = temp_room[1]
        print('You are in the {}.\n Upon the wall hangs {}'.format(temp_room[0], temp_room[1]))
        print('\nYour Evidence: {}'.format(player_inventory))
        if evidence_list[player_location] == 1:
            print('\n{} is here: Statement can be collected\n'.format(character_list[player_location]))
        else:
            print('\n{} is here: There are no statements to collect\n'.format(character_list[player_location]))
        player_command = input('Enter your next move: ').split(' ')
        if player_command[0] == 'go':
            player_location = move_room(player_location, player_command[1])
        elif player_command[0] == 'get':
            player_inventory = get_item(player_inventory, player_location, evidence_list, character_list)
        else:
            # FIXME
            print('')
        print(player_inventory)
        print(player_location)
        
        separator()