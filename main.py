import random as r
import math as m
import os
import time as t



#pos=0, thirst=0, canteens=5
class Protagonist:
    def __init__(self):
        self.pos = 0
        self.thirst = 0
        self.canteens = 5
#tired=0
class Camel:
    def __init__(self):
        self.tired = 0
#pos=-20
class Natives:
    def __init__(self):
        self.pos = -20
#idkkk stuff hapens        
class Room:
    
	def __init__(self, width=5, height=5):
		self.w = width
		self.h = height
		self.two_d = [["   " for i in range(self.w)] for j in range(self.h)]
		self.player_coords = {}
		self.ai_info = {}
		self.border = "+"
		#creates a room border the size of the room
		for i in range(self.w):
			self.border = self.border + "===+"

	def __repr__(self): #called when trying to print the room
		
		
		print(self.border)

		#prints the room with a few extra additions
		for i in range(len(self.two_d)):
			print ("|", end='')
			roomLine = "|".join([str(x) for x in self.two_d[i]])
			print(roomLine, end='')
			print ("|")
			print(self.border)
		#returns bekus program didn't like it w/out return
		return ""

	def add_player(self, player, coords = [-1,-1], ai_check = -1):
		if (coords[0] == -1):
			#if no coords are given, set player at middle left of screen
			coords = (int(self.h/2),0)
		try:
			#adds player to 2d list
			self.two_d[coords[0]][coords[1]] = player
			#adds player to dictionary
			self.player_coords[player] = coords
		except:
			#if location on list doesn't exist return an error
			print("add player error: List index out of range")
			return
		
		if ai_check != -1:
			self.ai_info[player] = ai_check

	def move_player(self, player, deltaX, deltaY):
		try: #check if player exists in dictionary
			current_pos = self.player_coords[player]
		except:
			print("Player doesn't exist check ur spelling (Key Error)")
			return
		#calculates new coords
		new_pos = [current_pos[0] + deltaY, current_pos[1] + deltaX]
		if new_pos[0] < 0 or new_pos[0] > self.h - 1 or new_pos[1] < 0 or new_pos[1] > self.w - 1:
			#print(str(player) + " is trying to escape") 
			#checks if player is moving into the border
			return (str(player) + " is trying to escape") 
		if self.two_d[new_pos[0]][new_pos[1]] != "   ":
			#print(str(player) + " trying to move onto " + str(self.two_d[new_pos[0]][new_pos[1]])) 
			#checks if someting is already in the location the player is moving to
			return [str(player)," trying to move onto ",str(self.two_d[new_pos[0]][new_pos[1]])] 

		#clears the current player coords
		self.two_d[current_pos[0]][current_pos[1]] = "   "
		#puts player in new coords
		self.two_d[new_pos[0]][new_pos[1]] = player
		#changes player location in dictionary
		self.player_coords[player] = new_pos
		return ""

	def ai_path(self, player, coord1, coord2):
		current_loc = self.player_coords[player]

		DeltaX = 0
		DeltaY = 0

		if self.ai_info[player] == 0: #move toward coord1
			if current_loc[1] < coord1[1]: #move right
				#print("move right")
				DeltaX = 1
			elif current_loc[1] > coord1[1]: #move left
				#print("move left")
				DeltaX = -1
			if current_loc[0] < coord1[0]: #move down
				#print("move down")
				DeltaY = 1
			elif current_loc[0] > coord1[0]: #move up
				#print("move up")
				DeltaY = -1

			
			if DeltaX == 0 and DeltaY == 0: #if already at coord1, move to coord2
				self.ai_info[player] = 1
				return

		elif self.ai_info[player] == 1: #move toward coord2
			if current_loc[1] < coord2[1]: #move right
				#print("move right")
				DeltaX = 1
			elif current_loc[1] > coord2[1]: #move left
				#print("move left")
				DeltaX = -1
			if current_loc[0] < coord2[0]: #move down
				#print("move down")
				DeltaY = 1
			elif current_loc[0] > coord2[0]: #move up
				#print("move up")
				DeltaY = -1
			
			
			if DeltaX == 0 and DeltaY == 0: #if already at coord2, move to coord1
				self.ai_info[player] = 0
				return 

		self.move_player(player, DeltaX, DeltaY) #move ai using the given deltaX and deltaY
#creats 3 objects with the varaibles shown above (b4 room class)
char = Protagonist()
cam = Camel()
nat = Natives()
#clears the screen on repl, but doesn't work on code hs D:
def clear():
    pass
    #os.system( 'clear' )
#creates the big 2d list used when the player or natives move
def room_create(player, w, h):
    #looks at user pos
    if player == "<=>":
        loc = char.pos
    else:
        loc = nat.pos
    #creats a list of locations the user can travel to
    increments = []
    for i in range(loc,loc + w):
        if len(str(i)) == 1:
            increments.append(" " + str(i) + " ")
        elif len(str(i)) == 2:
            increments.append(str(i) + " ")
        elif len(str(i)) == 3:
            increments.append(str(i))
    
    #needs space for increments that show light years traveled
    h = h + 2
    #makes an object with the desired width and height
    test = Room(w,h)
    
    #adds the increments, 1 at a time
    for x in range(len(increments)):
        test.add_player(increments[x], [0, x])
        test.add_player("[=]", [1, x])
    #addsthe player at the very left
    test.add_player(player, [5, 0])
    #returns the object so it can be used
    return test
    
def move_player(int1, int2):
    #creats a room with the desired width, height and player
    rm = (room_create("<=>", 21, 7))
    rand = (r.randint(int1, int2))
    #tells player its their turn at the top left of the move section/menu
    rm.add_player(" Y ",(2, 0)) 
    rm.add_player(" O ",(2, 1))
    rm.add_player(" U ",(2, 2))
    rm.add_player(" R ",(2, 3))
    rm.add_player("   ",(2, 4))
    rm.add_player(" T ",(2, 5))
    rm.add_player(" U ",(2, 6))
    rm.add_player(" R ",(2, 7))
    rm.add_player(" N ",(2, 8))
    
    #generates planets randomely
    #chooses spawn locations randomely as well
    ais = r.randint(1, 3)  
    if ais >= 1:
        y1 = r.randint(1,2)
        if y1 == 1:
            y1 = 2
        else:
            y1 = 8
        x1 = r.randint(15,20)
        rm.add_player("!!!", (y1, x1), 0)
    
    if ais >= 2:
       
        if y1 == 2:
            y2 = 7
        else:
            y2 = 3
        x2 = r.randint(12,20)
        #makes sure this planet does not spawn on top of another
        if x2 != x1:
            rm.add_player("! !", (y2, x2), 0)
        else:
            x2 = x2 - 3
            rm.add_player("! !", (y2, x2), 0)
    
    if ais == 3:
        y3 = r.randint(1,2)
        if y3 == 1:
            y3 = 2
        else:
            y3 = 8
        x3 = r.randint(10, 20)
        #makes sure this planet doesnt spawn on top of another
        if x3 != x2 and x3 != x1:
            rm.add_player(" ! ", (y3, x3), 0)
        else:
            while x3 == x2 or x3 == x1:
                x3 = x3 - 1
            rm.add_player(" ! ", (y3, x3), 0)
    #explains to the user how to play        
    print("As you fly your ship, you may land on planets or !!!'s and get items. \nWhen you land at a planet you stay their for the day!")
    print("Your ship is the '<=>' image found on the left of the screen")
    t.sleep(1)
    user_error = ""
    stuff = ""
    #rand > 0 because rand is amount of spaces player can move
    while rand > 0:
        #prints the 2d list the user is in
        print(rm, end = "")
        if user_error != "":
            print(user_error)
        try:
            if stuff != "" and stuff[-1] not in ["!!!", "! !", " ! "]:
                print(stuff)
        except:
            pass
        #prints how many times the player can move
        user_input = input("You can move " + str(rand) + " (more) times. Enter 'w', 'a','s' or 'd' to move! ")
        
        if user_input.lower() == "d": #moves player "forward" and adds one light year
            stuff = rm.move_player("<=>", 1, 0)
            char.pos = char.pos + 1
        elif user_input.lower() == "a": #moves player "backward" and subtracts one light year
            stuff = rm.move_player("<=>", -1, 0)
            if stuff == "":#prevents an error
                char.pos = char.pos - 1
        elif user_input.lower() == "w": #moves player up
            stuff =  rm.move_player("<=>", 0, -1)
        elif user_input.lower() == "s": #moves player down
            stuff =  rm.move_player("<=>", 0, 1)
        else: #if they put a invalid direction dont use a move
            user_error = "Error: Invalid direction"
            continue
        #checks if player is going to a planet
        try:
            if stuff != "" and stuff[-1] not in ["!!!", "! !", " ! "]: #if player runs into a wall dont use a move
                stuff = "Error: You can't move to their D:!"
                continue
            elif stuff[-1] in ["!!!", "! !", " ! "]: #if player runs into a planet
                return game() #star a minigame
        except:
            pass
        #if user is not going to a planet and no errors have occured, set the error = nothing and get rid of one move
        user_error = ""
        rand = rand - 1
        #clear()
        #tries moving the planets, and if an error occurs because they doesn't exist nothing happens
        try:
            rm.ai_path("!!!", (8, x1), (2, x1))
            rm.ai_path("! !", (8, x2), (2, x2))
            rm.ai_path(" ! ", (8, x3), (2, x3))
        except:
            pass
 
    print(rm)
    #print(char.pos)
    t.sleep(1/2) #waits to siginify the users turn is "over"
    user = input("After you move its the natives turn to move! Click the enter key to continue! ")
    return "" #i have no idea why this is here, but it might be important so I'm going to keep it here.
        
def move_natives():
    #creats a room, but this time with a nav charater at the left side of the screen instead of a "<=>"
    rm = (room_create("nav", 21, 7))
    #picks number of tiles the natives will move
    rand = (r.randint(7, 13))
    #explains to the user that its the natives turn now
    rm.add_player("NAT",(2, 0)) 
    rm.add_player("IVE",(2, 1))
    rm.add_player("S  ",(2, 2))
    rm.add_player("MOV",(2, 3))
    rm.add_player("E  ",(2, 4))
    #if the user is less than 20 light years away, then the program will ad them to the 2d list
    distance = char.pos - nat.pos
    if distance <= 20:
        rm.add_player("<=>", (5,distance))
    #while loop for as many moves as the natives have
    while rand > 0:
        #prints 2d list object
        print(rm, end = "")
        #moves the player 1 spot to the right
        stuff = rm.move_player("nav", 1, 0)
        
        t.sleep(1/4)
        if stuff != "": #stuff will only equal somthing if natives are trying to move onto something (the only thing they could move on would be the player)
            print("Game over: The natives caught up!")
            return True
        #increases the pos every time the natives move
        nat.pos = nat.pos + 1
        #get rid of one move
        rand = rand - 1
        #clear()
    nat.pos = nat.pos - 1 #idk why but the thing was always off by one
    return False #if the natives don't catch up with the player return flase to keep done as false
#this func is necessary due to a few features in game that can cause hte player to move backwards, and in rare scenarios behind the natives.
def natives_ahead_check():
    if char.pos < nat.pos:
        return True
    else:
        return False
#func for when player lands on a planet
def game():
    #generates a random number for which game the user is going to play
    rand = r.randint(1,4)
    if rand == 1:
        #explains to the user they have a chance to move forward or backwards
        print("On the planet their is a unstable powerscource, that could \nfly you an extra 10 miles forward, or backwords. \nDo you want to use it?('Y'/'N')")
        print("Current Pos: {}".format(char.pos)) #prints the players current pos so they know where they are
        while True:
            #user input on a dif line so it doesn't overlap the current pos line
            user = input("")
            #makes sure users input is not invalid
            if user.lower() not in ("y", "n", "yes", "no"):
                print("Invalid input, please enter 'y' or 'n'")
                continue
            #if users input isn't invalid and is yes then a coin is flipped
            elif user.lower() in ('y', 'yes'):
                dist = r.randint(1,2)
                #if heads than they go forward
                if dist == 1:
                    print("You put the unstable powerscource on your ship and flew 10 light years forward!")
                    char.pos = char.pos + 10
                    user = input("Click the enter key to continue! ")
                    break
                else:# if tails they go backward
                    print("You put the unstable powerscource on your ship and were forced 10 light years backwards D:")
                    char.pos = char.pos - 10
                    user = input("Click the enter key to continue! ")
                    break
            #if users input isn't invalid and they decid not to take the risk nothing happenes
            elif user.lower() in ('n', 'no'):
                print("You decided not to move and rested for the rest of the day")
                break
        t.sleep(2)
        #incase they move backwards
        return natives_ahead_check()
    if rand == 2:
        #explains to user their in another coin flip scenario
        print("On the planet their was a alien who wanted to, trade water with you by flipping a coin.\nHeads = alien gives you 2 canteens\nTails = you give alien 2 canteens")
        water = r.randint(1,2) #calculates who will win b4 the user even says yes (idk why just is)
        while True:
            #asks user 4 input
            user = input("('y' or 'n')\n")
            #if user input is invalid asks for another input
            if user.lower() not in ('y','n','yes','no'):
                print("Invalid input, please enter 'y' or 'no'")
                continue
            #if user input is valid and is yes shows user output of coinflip
            elif user.lower() in ('y', 'yes'):
                print("As the alien flipped the coin in the air, it felt like time slowed down")
                t.sleep(2)
                
                print("The coin landed on...")
                t.sleep(1)
                #if heads then give user 2 waterbottles
                if water == 1:
                    print("Heads!!")
                    print("The alien gave you 2 water bottle and you rested for the rest of the day")
                    char.canteens = char.canteens + 2
                    user = input("Click the enter key to continue! ")
                    break
                #else (tails) take away 2 canteens
                else:
                    print("Tails D:")
                    print("You gave the alien 2 water bottles and rested for the rest of the day")
                    char.canteens = char.canteens - 2
                    #prevent user from getting negative canteens
                    if char.canteens < 0:
                        char.canteens = 0
                    user = input("Click the enter key to continue! ")   
                    break
            #if user input is valid and they say no, just break
            elif user.lower() in ('n','no'):
                print("You decided not to trade with the alien and rested for the rest of the day!")
                user = input("Click the enter key to continue! ")
                break
        t.sleep(2)
    
    if rand == 3:
        #explains to the user they must solve a puzzle to stay on the island or they will be kicked off
        print("On the planet you landed on their was a Alien who would only let you stay\nthere if you could beat them at tic tac toe!")
        if tic_tac_toe():#tic tac toe puzzle is played and returns true or false depending on whether the user solved it correctly
            #if passed let user stay on island
            print("You beat the Alien's challenge and rested for the rest of the day!")
            t.sleep(2)
            user = input("Click the enter key to continue! ")
        else:
            #if failed move user back 5 light years
            print("You didn't beat the Alien's challenge and were forced to move back 5 light years D:")
            char.pos = char.pos - 5
            t.sleep(2)
            user = input("Click the enter key to continue! ")
            return natives_ahead_check() #returns ahead check just incase the user was moved behind the natives
	
    if rand == 4:
        #explains to user they found an oasis, and their status effects are taken away
        print("You found a canteen, and a stash of supplies on the planet which you used to quench your thirst and cool down your spaceship for the day! (oasis)")
        char.thirst = 0
        cam.tired = 0
        user = input("Click the enter key to continue! ")
            
def tic_tac_toe(): #tic tac toe for 3rd game in game() func
    #creats a 3 by 3 2d list
    board = [
    ["   ","   ","   "],
    ["   ","   ","   "],
    ["   ","   ","   "]
    ]
    print("TIC TAC TOE!") #explains to user they are playing tic tac toe
    rng = r.randint(1, 2) #generates a rand int for which puzzle the user will solve
    if rng == 1:
        #explains the user a puzzle
        print("You are O, and are trying to win. \nWhat is the best spot to choose?")
        #O trying to win
        board[1][1] = " X "
        board[0][0] = " X "
        board[0][2] = " O " 
        board[2][0] = " O "
        #defines lots of variables answer is tehe answer, options is the valid inputs the user can use, and reasoning is what is printed if user gets the problem wrong
        answer = ('5')
        options = ('1', '2', '3', '4', '5')
        reasoning = "As O, if you want to win you must block of X from winning. (aka spot 5) \nIn addition to this going in that specific spot would give you\n2 different spots to win!"
        
    elif rng == 2:
        print("You are O, and trying to loose.\nIf X is choosing moves randomely what is the most optimal spot to choose?")
        #if x is just choosing moves randomely and ur trying to loose
        #what is the most optimal spot to loose as O
        board[0][0] = " X "
        #defines lots of variables answer is tehe answer, options is the valid inputs the user can use, and reasoning is what is printed if user gets the problem wrong
        answer = ('5','7')
        options = ('1','2','3','4','5','6','7','8')
        reasoning = "Spots 2,4,6, and 8 would block off huge sections of the board, which may cause x to loose. \nSpots 1 and 3 block of the quickests routes for X to win, so they are not the most optimal. \nOn the other hand 5, 7 would be farthest away from X and most likely not block any spots that may cause x to loose"
        #2, 4, 6, 8 would block off huge sections of the board, and may cause x to loose
        #1, 3 would block off quickest routes for x to win
        #5, 7 would be farthest away from X and most likely not block any spots that may cause x to loose
        
    
    #in any spots that are not already filled in, add f
    f = 1
    for i in range(len(board)):
        for x in range(len(board)):
            if board[i][x] == "   ":
                board[i][x] = "<" + str(f) + ">"
                f = f + 1
        #prints the board
        print("-"*11)
        print("|".join([str(x) for x in board[i]]))
        
    print("-"*11)
    while True:
        #asks user 4 an input
        user = (input(""))
        try:
            #makes sure users input is an int
            user = int(user)
            #if an int, then make it a string cause you can only do use in w/ strings 4 some reason
            if str(user) not in options:
                #if not a valid input ask user for another input
                print("Invalid input: please enter an actual spot on the board!")
                continue
            else:
                #if is a valid input then leave the while loop
                break
                
        except:
            print("Invalid input: please enter a integer!")
            continue
    #if the users input is correct explain to the user they are correct
    if str(user) in answer:
        print("Correct!")
        user = input("Click the enter key to continue! ")
        #return True for game() func
        return True
    else: #if users input is incorrect
        print(reasoning) #explain why
        user = input("Click the enter key to continue! ")
        #return False for game() func
        return False
#if user runs out of canteens this game is played
def canteen_game():
    #explains ot user they are playing hange man
    print("You find a small canteen hidden on your ship, but it is locked. \nYou must play Hang man to unlock the canteen and get more water!")
    #possible words    
    word = ('orange', 'python','string', 'castle')
    #chooses a random word from availible words
    word = r.choice(word)
    check = word
    #availible letters!
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    let = ('a', 'b', 'c', 'd', 'e', 'f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    incorrect_guesses = 6
    word_2 = ""
    #creats a new var with _'s instead of lettes
    for i in range(len(word)):
            word_2 = word_2 + str("_ ")
    #while the user hasn't run out of incorrect_guesses (aka hangman hasnt been fully drawn)
    while incorrect_guesses > 0:
        #tell user how many incorrect gueses they have and print how much of the word they have solved
        print("\nIncorrect guesses availible: {}".format(incorrect_guesses-1))
        print(str(word_2) + '\n')
        #print out availible letters in a neat format
        for i in range(len(letters)):
            if i < 13:
                print(str(letters[i]) + " ", end='')
            elif i == 13:
                print('\n')
                print(' ', end='')
            else:
                print(str(letters[i]) + " ", end='')
        print('\n')
        #asks user for input
        try:
            user = str(input("Enter a guess: "))
            #i think its impossible for the input to not be a str, but just incase
        except:
            print("Invalid Input: Enter a string")
            continue
        
        if len(user) != 1:
            #if the user input more than 1 char in their input then ask for another input
            print("Invalid Input: Enter only 1 character")
            continue
        
        elif user.lower() not in let:
            #if the users input is not in the alphabet ask for an input in the alphabet
            print("Invalid Input: Enter a character in the alphabet")
            continue

        elif user.lower() not in letters:
            #else if it is in the alphabet, but not in the characters they have used, then ask user for a char they haved already used
            print("Invalid input: Enter a character that you haven't already guessed")
            continue

        else:
            #converts letter to a number using ord 
            letters[ord(user.lower()) - 97] = "_"
            #if users input is in the word
            if user.lower() in word:
                #tell the user it is in it
                print("Correct!")
                #go through the word and replace the letter
                for i in range(6): #length of each word
                    place = word.find(user.lower())
                    if place != -1:
                        #place wwill only be -1 if the program hasn't found the input, so if it isn't then that char has been found
                        #add letter to word_2 or the word the user can see
                        word_2 = str(word_2[:place * 2]) + str(user.lower()) + str(word_2[place*2 + 1:])
                        #remoev letter from word or the word the user can't see
                        word = word[:place] + "_" + word[place+1:]
            else:
                #if their guess isnt in the word print incorrect
                print("Incorrect")
                #and remove a guess
                incorrect_guesses -=1
        #if visible word without spaces ='s the actual word explain to the user they solved the proglem    
        if word_2.replace(" ","") == check:
            #print full word for user
            print(check)
            #'open the canteen'
            print("You opened the canteen!")
            user = input("Click the enter key to continue! ")
            return True #return true for main func
         
    user = input("Click the enter key to continue! ")
    return False #if user runs out of guessses then return false

def camel_game():#runs if users 'camel dies' / (ship is overheating)
    print("As your ship is overheating, you find some extra parts that can be used to cool down your ship, but they have \na lock on them that requires you to solve a trivia question?\n")
    #dict of availible questions in the format of a tuple and then a string with the quesiton
    #the first thing in the tuple is the answer, the other things are the availible options
    questions ={
        ("white", "black") : "Who starts first in chess? ('white' or 'black'): ",
        ("pacific", "atlantic", "indian") : "What is the world’s largest ocean? ('atlantic', 'indian', 'pacific'): ",
        ("3", "2", "1") : "Which of Newton’s Laws states that ‘for every action, there is an equal and opposite reaction? ('1', '2', '3'): ",
        ("solids", "liquids", "gases") : "In what type of matter are atoms most tightly packed? ('solids', 'liquids', or 'gases'): ",
    }  
    #get a random thing from the dict
    questions = list(questions.items())
    questions = r.choice(questions)
    
    while True:
        #ask user for an input
        try:
            user = str(input(questions[1]))
            #i think this is inpossible, but if user's input isnt a str then ask user for str
        except:
            print("Invalid input: Enter a string pls\n")
            continue
        #checks if user's input is not an option, and if it isn't then asks for an option
        if (user.lower()).strip() not in questions[0]:
            print("Invalid input: Enter a valid answer pls! \n")
            continue
        #if users input is an option and is correct, this explains that to the user
        if (user.lower()).strip() == questions[0][0].lower():
            print("Correct!")
            user = input("Click the enter key to continue! ")
            return True #and returns true for the main func()
        else:#if user's input is incorrect, this explains that to the user
            print("Incorrect, the correct answer was {}".format(questions[0][0]))
            user = input("Click the enter key to continue! ")
            return False #and returns false for main func()
    

#sets a few varaibles that will be used in main func
done = False
days = 0
#main func
#explains lore to the user
print("After stealing the legendary golden nugget from a planet \nfar away from your home town, you are on the run from the natives of that planet.\nDue to the natives rushing after your ship they did not have time to pack much fuel\nso if you can get 200 light years away from them you win!")

while not done:
    #print day
    print("Day {}".format(str(days)))
    #explains to user their availible options
    print("Would you like to... \n○ A: Full speed ahead\n○ B: Normal speed\n○ C: Rest\n○ D: Drink\n○ E: Status\n○ X: Exit")
    user = input("")
    #i forgot wat strip was, and im too lazy to change it (removes spaces)
    user = user.replace(" ", "") #i didn't do the same thing with .lower because I had already done it everywhere it is used
    #to prevent confusing the user with invalid inputs when they didnt input anything
    if user.lower() == "":
        continue
    #if user input isnt an actual option, asks user for an actual option
    if user.lower() not in ('rest', 'drink', 'fullspeedahead', 'normalspeed','status','exit', 'x', 'a', 'b', 'c', 'd','e'):
        print("Invalid input")
        continue
    #if user wants to exit the program, exit the program
    if user.lower() == "x" or user.lower() == "exit":
        done = True
        print("Exited the game!")
    
    #else if user wants to move ahead at full speed    
    elif user.lower() == "fullspeedahead" or user.lower() == "a":
        #starts move func
        move_player(10, 20)
        #incase all other checks fail, this checks if natives are ahead
        if natives_ahead_check():
            done = True
            print("The natives caught up to you!")
            break
        #moves natives using move_native() func which returns ifthe natives caught up w/ the player
        done = move_natives()
        if done == True:
            break
        #adds thirst to the player
        char.thirst = char.thirst + (r.randint(1,2))
        #adds tiredness to the camel / increases spaceship heat
        cam.tired = cam.tired + (r.randint(1,3))
        
    #if user wants to move ahead at a normal speed
    elif user.lower() == "normalspeed" or user.lower() == "b":
        #starts move func
        move_player(5,12)
        #if all other checks fail, this checks if natives are ahead
        if natives_ahead_check():
            done = True
            print("The natives caught up to you!")
            break
        #moves natives using move_native() func which returns ifthe natives caught up w/ the player
        done = move_natives()
        if done == True:
            break
        
        #adds thirst to player
        char.thirst = char.thirst + 1
        #adds tiredness to camel / increases spaceship heat
        cam.tired = cam.tired + 1
        
        
    #if user wants to rest sets cam's tiredness / spaceships heat to 0  and then moves natives
    elif user.lower() == "rest" or user.lower() == "c":
        print("You rested for the day, and your ship cooled down!")
        cam.tired = 0
        t.sleep(3)
        done = move_natives()
    
    #if user wants to drink sets char thirst to 0 if u canteens are availible, else you play a minigame for more
    elif user.lower() == "drink" or user.lower() == "d":
        if char.canteens > 0: #checks how many canteens user has
            print("You drank water, and quenched your thirst!")
            char.thirst = 0   #if user has one drinks it and removes it
            char.canteens = char.canteens - 1
        elif char.canteens == 0:
            if canteen_game(): #if user doesn't have one they play a minigame for more
                print("You drank water, and quenched your thirst!")
                char.thirst = 0 
                char.canteens = 2 #it says 3, but you drink one automatically so you only get 2
            else:
                print("You were out of canteens, but you lost the minigame and were not rewared with any more canteens D:")
                char.thirst = char.thirst + 1
        t.sleep(3)
        #done = move_natives() #i decided to remove this because it made the game a lot harder during play testing
        continue
    #if user wants to know their status, prints their status using .format to make it easier to do in 1 print statement
    elif user.lower() == "status" or user.lower() == "e":
        print("====== \nPos: {} \nNatives pos: {} \n\nCanteens: {} \n\nDistance from natives: {} \n======".format((str(char.pos)), (str(nat.pos)), (str(char.canteens)), str(char.pos - nat.pos)))
        t.sleep(1)
        continue
    #adds 1 day to day counter
    days += 1
    #if player is feeling thirsty and the game isn't over
    if char.thirst >= 4 and char.thirst <= 6 and done == False:
        #tells the user they are feeling thirsty
        print("Notice: You are feeling a thirsty, type 'd' to drink water!")
    elif char.thirst > 6 and done == False:
        #else if the user is not feeling thirst, but is died of thirst and game isnt over, tells the user they died of thirst
        print("You died of thirst D:!")
        done = True
        break
    #if game isnt over and ship is overheating / camel is tired
    if done == False and cam.tired >= 5 and cam.tired <= 8:
        #prints the ship is over heating
        print("Notice: Your ship is over heating, type 'c' to rest!")
    elif done == False and cam.tired > 8: #if ship is overheating, the user plays a minigame
        if camel_game(): #if they pass their overheating is reset, and the user is notified
          print("You mananged to save your ship, and your life as well by solving the puzzle!")
          cam.tired = 0
        else: #if they don't pass the user is notified, and the game ends
          print("You didn't solve the puzzle and lost D:")
          done = True
          break
    #if all other checks fail, one last check if the natives are ahead is done if the game isnt over
    if natives_ahead_check() and done == False:
        done = True #if they are the game ends
        print("the natives caught up!")
        break
    #if game isn't over and user moves 200 light years the user is notified and the game ends
    if done == False and char.pos >= 200:
        print("You WON!")
        done = True
