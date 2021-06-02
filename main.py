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
            elif stuff[-1] in ["!!!", "! !", " ! "]:
                return game()
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
    t.sleep(1/2)
    user = input("After you move its the natives turn to move! Click the enter key to continue! ")
    return ""
        
def move_natives():
    rm = (room_create("nav", 21, 7))
    rand = (r.randint(7, 13))
    rm.add_player("NAT",(2, 0)) 
    rm.add_player("IVE",(2, 1))
    rm.add_player("S  ",(2, 2))
    rm.add_player("MOV",(2, 3))
    rm.add_player("E  ",(2, 4))
    distance = char.pos - nat.pos
    if distance <= 20:
        rm.add_player("<=>", (5,distance))
    while rand > 0:
        print(rm, end = "")
        
        stuff = rm.move_player("nav", 1, 0)
        
        t.sleep(1/4)
        if stuff != "": #stuff will only equal somthing if natives are trying to move onto something
            print("Game over: The natives caught up!")
            return True
        nat.pos = nat.pos + 1
        rand = rand - 1
        clear()
    nat.pos = nat.pos - 1 #idk why but the thing was always off by one
    return False

def natives_ahead_check():
    if char.pos < nat.pos:
        return True
    else:
        return False

def game():
    rand = r.randint(1,4)
    if rand == 1:
        print("On the planet their is a unstable powerscource, that could \nfly you an extra 10 miles forward, or backwords. \nDo you want to use it?('Y'/'N')")
        print("Current Pos: {}".format(char.pos))
        while True:
            user = input("")
            if user.lower() not in ("y", "n", "yes", "no"):
                print("Invalid input, please enter 'y' or 'n'")
                continue
            elif user.lower() in ('y', 'yes'):
                dist = r.randint(1,2)
                if dist == 1:
                    print("You put the unstable powerscource on your ship and flew 10 light years forward!")
                    char.pos = char.pos + 10
                    user = input("Click the enter key to continue! ")
                    break
                else:
                    print("You put the unstable powerscource on your ship and were forced 10 light years backwards D:")
                    char.pos = char.pos - 10
                    user = input("Click the enter key to continue! ")
                    break
            elif user.lower() in ('n', 'no'):
                print("You decided not to move and rested for the rest of the day")
                break
        t.sleep(2)
        return natives_ahead_check()
    if rand == 2:
        print("On the planet their was a alien who wanted to, trade water with you by flipping a coin.\nHeads = alien gives you 2 canteens\nTails = you give alien 2 canteens")
        water = r.randint(1,2)
        while True:
            user = input("('y' or 'n')\n")
            if user.lower() not in ('y','n','yes','no'):
                print("Invalid input, please enter 'y' or 'no'")
                continue
            elif user.lower() in ('y', 'yes'):
                print("As the alien flipped the coin in the air, it felt like time slowed down")
                t.sleep(2)
                
                print("The coin landed on...")
                t.sleep(1)
                if water == 1:
                    print("Heads!!")
                    print("The alien gave you 2 water bottle and you rested for the rest of the day")
                    char.canteens = char.canteens + 2
                    user = input("Click the enter key to continue! ")
                    break
                else:
                    print("Tails D:")
                    print("You gave the alien 2 water bottles and rested for the rest of the day")
                    char.canteens = char.canteens - 2
                    user = input("Click the enter key to continue! ")   
                    break
            
            elif user.lower() in ('n','no'):
                print("You decided not to trade with the alien and rested for the rest of the day!")
                user = input("Click the enter key to continue! ")
                break
        t.sleep(2)
            
    if rand == 3:
        print("On the planet you landed on their was a Alien who would only let you stay\nthere if you could beat them at tic tac toe!")
        if tic_tac_toe():
            print("You beat the Alien's challenge and rested for the rest of the day!")
            t.sleep(2)
            user = input("Click the enter key to continue! ")
        else:
            print("You didn't beat the Alien's challenge and were forced to move back 5 light years D:")
            char.pos = char.pos - 5
            t.sleep(2)
            user = input("Click the enter key to continue! ")
            return natives_ahead_check()
		
    if rand == 4:
      print("You found a canteen, and a stash of supplies on the planet which you used to quench your thirst and cool down your spaceship for the day!")
      char.thirst = 0
      cam.tired = 0
      user = input("Click the enter key to continue! ")
            
def tic_tac_toe():
    board = [
    ["   ","   ","   "],
    ["   ","   ","   "],
    ["   ","   ","   "]
    ]
    print("TIC TAC TOE!")
    rng = r.randint(1, 2)
    if rng == 1:
        print("You are O, and are trying to win. \nWhat is the best spot to choose?")
        #O trying to win
        board[1][1] = " X "
        board[0][0] = " X "
        board[0][2] = " O " 
        board[2][0] = " O "
        answer = ('5')
        options = ('1', '2', '3', '4', '5')
        reasoning = "As O, if you want to win you must block of X from winning. (aka spot 5) \nIn addition to this going in that specific spot would give you\n2 different spots to win!"
    elif rng == 2:
        print("You are O, and trying to loose.\nIf X is choosing moves randomely what is the most optimal spot to choose?")
        #if x is just choosing moves randomely and ur trying to loose
        #what is the most optimal spot to loose as O
        board[0][0] = " X "
        answer = ('5','7')
        options = ('1','2','3','4','5','6','7','8')
        reasoning = "Spots 2,4,6, and 8 would block off huge sections of the board, which may cause x to loose. \nSpots 1 and 3 block of the quickests routes for X to win, so they are not the most optimal. \nOn the other hand 5, 7 would be farthest away from X and most likely not block any spots that may cause x to loose"
        #2, 4, 6, 8 would block off huge sections of the board, and may cause x to loose
        #1, 3 would block off quickest routes for x to win
        #5, 7 would be farthest away from X and most likely not block any spots that may cause x to loose
        
    
    
    f = 1
    for i in range(len(board)):
        for x in range(len(board)):
            if board[i][x] == "   ":
                board[i][x] = "<" + str(f) + ">"
                f = f + 1
        print("-"*11)
        print("|".join([str(x) for x in board[i]]))
        
    print("-"*11)
    while True:
        user = (input(""))
        try:
            user = int(user)
            if str(user) not in options:
                print("Invalid input: please enter an actual spot on the board!")
                continue
            else:
                break
                
        except:
            print("Invalid input: please enter a integer!")
            continue
    if str(user) in answer:
        print("Correct!")
        user = input("Click the enter key to continue! ")
        return True
    else:
        print(reasoning)
        user = input("Click the enter key to continue! ")
        return False

def canteen_game():
    #hang man
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
    for i in range(len(word)):
            word_2 = word_2 + str("_ ")
    
    while incorrect_guesses > 0:
        print("\nIncorrect guesses availible: {}".format(incorrect_guesses-1))
        print(str(word_2) + '\n')
        
        for i in range(len(letters)):
            if i < 13:
                print(str(letters[i]) + " ", end='')
            elif i == 13:
                print('\n')
                print(' ', end='')
            else:
                print(str(letters[i]) + " ", end='')
        print('\n')
        
        try:
            user = str(input("Enter a guess: "))
        except:
            print("Invalid Input: Enter a string")
            continue
        
        if len(user) != 1:
            print("Invalid Input: Enter only 1 character")
            continue
        
        elif user.lower() not in let:
            print("Invalid Input: Enter a character in the alphabet")
            continue

        elif user.lower() not in letters:
            print("Invalid input: Enter a character that you haven't already guessed")

        else:
            letters[ord(user.lower()) - 97] = "_"
            
            if user.lower() in word:
                print("Correct!")
                for i in range(5):
                    place = word.find(user.lower())
                    if place != -1:
                        word_2 = str(word_2[:place * 2]) + str(user.lower()) + str(word_2[place*2 + 1:])
                        word = word[:place] + "_" + word[place+1:]
            else:
                print("Incorrect")
                incorrect_guesses -=1
            
        if word_2.replace(" ","") == check:
            print(check)
            print("You opened the canteen!")
            user = input("Click the enter key to continue! ")
            return True
        
    user = input("Click the enter key to continue! ")
    return False

def camel_game():
    print("You find some extra parts that can be used to repair your ship, but they have \na lock on them that requires you to solve a trivia question?\n")
    #print("These trivia questions are def not plagirused from \nhttps://www.scarymommy.com/best-trivia-questions-answers/ \n:sweat_smile: *I don't know what ur talking about*")
    questions ={
        ("white", "black") : "Who starts first in chess? ('white' or 'black'): ",
        ("pacific", "atlantic", "indian") : "What is the world’s largest ocean? ('atlantic', 'indian', 'pacific'): ",
        ("3", "2", "1") : "Which of Newton’s Laws states that ‘for every action, there is an equal and opposite reaction? ('1', '2', '3'): ",
        ("solids", "liquids", "gases") : "In what type of matter are atoms most tightly packed? ('solids', 'liquids', or 'gases'): ",
    }  
    questions = list(questions.items())
    questions = r.choice(questions)
    while True:
        try:
            user = str(input(questions[1]))
        except:
            print("Enter a string pls\n")
            continue
        if (user.lower()).strip() not in questions[0]:
            print("Invalid input: Enter a valid answer pls! \n")
            continue
        if (user.lower()).strip() == questions[0][0].lower():
            print("Correct!")
            user = input("Click the enter key to continue! ")
            return True
        else:
            print("Incorrect, the correct answer was {}".format(questions[0][0]))
            user = input("Click the enter key to continue! ")
            return False
    


done = False
days = 0
#main func
print("After stealing the legendary golden nugget from a planet \nfar away from your home town, you are on the run from the natives of that planet.\nThe natives did who are after you did not bring much fuel,\nso if you can get 200 light years ahead of them you can escape scott free!\n")

while not done:
    print("Day {}".format(str(days)))
    print("Would you like to... \n○ A: Full speed ahead\n○ B: Normal speed\n○ C: Rest\n○ D: Drink\n○ E: Status\n○ X: Exit")
    user = input("")
    #i forgot was strip was, and im too lazy to change it (removes spaces)
    user = user.replace(" ", "")
    #to prevent confusing the user with invalid inputs when they didnt input anything
    if user.lower() == "":
        continue
    if user.lower() not in ('rest', 'drink', 'fullspeedahead', 'normalspeed','status', 'x', 'a', 'b', 'c', 'd','e'):
        print("Invalid input")
        continue
    
    if user.lower() == "x":
        done = True
        print("Exited the game!")
    
        
    elif user.lower() == "fullspeedahead" or user.lower() == "a":
        move_player(10, 20)
        if natives_ahead_check():
            done = True
            print("The natives caught up to you!")
            break
        done = move_natives()
        if done == True:
            break
        char.thirst = char.thirst + (r.randint(1,2))
        cam.tired = cam.tired + (r.randint(1,3))
        
    
    elif user.lower() == "normalspeed" or user.lower() == "b":
        move_player(5,12)
        if natives_ahead_check():
            done = True
            print("The natives caught up to you!")
            break
        done = move_natives()
        if done == True:
            break
        char.thirst = char.thirst + 1
        cam.tired = cam.tired + 1
        
        
    #sets cam tired to 0
    elif user.lower() == "rest" or user.lower() == "c":
        print("You rested for the day, and your ship cooled down!")
        cam.tired = 0
        t.sleep(3)
        done = move_natives()
    
    #sets char thirst to 0 if u canteens are availible, else you play a minigame for more
    elif user.lower() == "drink" or user.lower() == "d":
        if char.canteens > 0:
            print("You drank water, and quenched your thirst!")
            char.thirst = 0  
            char.canteens = char.canteens - 1
        elif char.canteens == 0:
            if canteen_game():
                print("You drank water, and quenched your thirst!")
                char.thirst = 0 
                char.canteens = 2 #it says 3, but you drink one automatically so you only get 2
            else:
                print("You were out of canteens, but you lost the minigame and were not rewared with any more canteens D:")
                char.thirst = char.thirst + 1
        t.sleep(3)
        #done = move_natives()
        continue
    
    elif user.lower() == "status" or user.lower() == "e":
        print("====== \nPos: {} \nNatives pos: {} \n\nCanteens: {} \n\nDistance from natives: {} \n======".format((str(char.pos)), (str(nat.pos)), (str(char.canteens)), str(char.pos - nat.pos)))
        t.sleep(1)
        continue
    days += 1
    
    if char.thirst >= 4 and char.thirst <= 6 and done == False:
        print("You are feeling a thirsty, type 'd' to drink water!")
    elif char.thirst > 6 and done == False:
        print("You died of thirst D:!")
        done = True
    if done == False and cam.tired >= 5 and cam.tired <= 8:
        print("Your ship is over heating, type 'c' to rest!")
    elif done == False and cam.tired > 8:
        if camel_game():
          print("You mananged to save your ship, and your life as well by solving the puzzle!")
        else:
          print("You didn't solve the puzzle and lost D:")
          done = True
          break
    if natives_ahead_check() and done == False:
        done = True
        print("the natives caught up!")
        break
    
    if done == False and char.pos >= 200:
        print("You WON!")
        done = True
