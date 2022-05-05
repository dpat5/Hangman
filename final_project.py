import random
from tkinter import *
from string import ascii_uppercase
from tkinter import messagebox

game_display = Tk()
game_display.geometry('1200x600+150+100')
game_display.configure(bg="cyan")
game_display.title("HANGMAN")


# GUI Design

title = Label(game_display, text = "ENAE 380 HANGMAN", font=('Rockwell', 40, 'bold'), bg = "cyan")
title.place(x = 325, y = 25)

word = Label(game_display, text = "Welcome to ENAE380 Hangman! All words in this game are related to ENAE380!", font=('Rockwell', 20), bg = "cyan")
word.place(x = 100, y = 100) 

word = Label(game_display, text = "Select your topic from below to begin!", font=('Rockwell', 20), bg = "cyan")
word.place(x = 350, y = 150) 

topic1_button = Button(game_display, text = "Python Basics", command = lambda:[Python_Basics(), switch()],  font= ("Rockwell 20"),width=14, bg ="light blue")
topic1_button.place(x = 100, y = 230)

topic2_button = Button(game_display, text = "Sorting", command = lambda:[Sorting(), switch()], font= ("Rockwell 20"),width=14, bg ="light blue")
topic2_button.place(x = 100, y = 305)

topic3_button = Button(game_display, text = "Sensors", command = lambda:[Sensors(),switch()], font= ("Rockwell 20"),width=14, bg ="light blue")
topic3_button.place(x = 100, y = 380)

topic4_button = Button(game_display, text = "Image Processing", command = lambda:[ImgProcessing(), switch()], font= ("Rockwell 20"),width=14, bg ="light blue",)
topic4_button.place(x = 100, y = 455)

exit_button = Button(game_display, text="Exit Game", command=game_display.destroy, font= ("Rockwell 14"),width=10, bg ="light blue")
exit_button.place(x=1065, y=500)


# Code to import images for Hangman, all images are attached to the file
photos = [PhotoImage(file="0.png"), 
		PhotoImage(file="1.png"), 
		PhotoImage(file="2.png"), 
		PhotoImage(file="3.png"),
		PhotoImage(file="4.png"), 
		PhotoImage(file="5.png"), 
		PhotoImage(file="6.png"),
		PhotoImage(file="7.png"), 
		PhotoImage(file="8.png"), 
		PhotoImage(file="9.png"),
		PhotoImage(file="10.png"), 
		PhotoImage(file="11.png")]

# Code to show the images for Hangman
image_display=Label(game_display, borderwidth = 0,highlightthickness = 0)
image_display.grid(row=3, column=3, columnspan=3)
image_display.place(x=920, y=250)

# Code to disable the topics after pressed once. 

def switch():
	if topic1_button["state"] == NORMAL:
		topic1_button["state"] = DISABLED
	else:
		topic1_button["state"] = NORMAL

	if topic2_button["state"] == NORMAL:
		topic2_button["state"] = DISABLED
	else:
		topic2_button["state"] = NORMAL

	if topic3_button["state"] == NORMAL:
		topic3_button["state"] = DISABLED
	else:
		topic3_button["state"] = NORMAL

	if topic4_button["state"] == NORMAL:
		topic4_button["state"] = DISABLED
	else:
		topic4_button["state"] = NORMAL

# TOPIC 1 - Python Basics
def Python_Basics():

	# Code for implementing the Keyboard on screen -------------------------------------------------------------------------------------------------------------
	"""
	Wanted to implement the alphabets on the game screen, rather than having the user typing it in.
	I found this code from https://www.youtube.com/watch?v=esHcFbNlNqQ
	I made changes to it to for my program
	"""

	# Code to print keyboard to screen ----------------------------------------------------------------------------------------------------------------------
	n = 0 
	xvar = 15
	yvar = 550
	for c in ascii_uppercase:
		keyboard = Button(game_display, text=c, command= lambda c=c: guess(c), activebackground="blue", font= ("Rockwell 16"),width=3, bg ="light blue")
		keyboard.grid(row=1+n//9, column=n%9)
		keyboard.place(x=xvar, y=yvar)
		keyboard = Button(command=switch)
		n+=1
		xvar+=45

	# Code to get the word from data file ----------------------------------------------------------------------------------------------------------------------
	wordList = []
	with open('topic_1_words.dat','r') as file:
		# reading each line    
		for line in file:
			# reading each word        
			for word in line.split():
				wordList.append(word)

	wordIndex = random.randint(0, len(wordList) - 1)

	# Showing user what topic they chose
	title = Label(game_display, text = "You chose: Python Basics", font=('Rockwell', 25, 'bold'), bg = "cyan")
	title.place(x = 400, y = 200)

	# Code to display the number of letters of the word -------------------------------------------------------------------------------------------------------
	game_word = (wordList[wordIndex])																	# Main Game Word
	blank_word = ["_" for i in game_word]																# Game Word in Blanks
	guess_word = Label(game_display, text = blank_word, font=('Rockwell',33, 'bold'), bg = "cyan")
	guess_word.place(x = 480, y = 300)


	"""
	I created two lists here. list_of_game_word creates a list of the gameword. list_of_blank_word is a list of the blanks.
	If the letter inputed by the user is in the list_of_game_word, it all that letter at that index into the list_of_blank_word

	It would look like this if run through the terminal.
						
	game_word 			- computer
	blank_word 			- ________
	list_of_game_word 	- ['C', 'O', 'M', 'P', 'U', 'T', 'E', 'R']
	list_of_blank_word	- ['_', '_', '_', '_', '_', '_', '_', '_']

	If user guessed P

	list_of_game_word 	- ['C', 'O', 'M', 'P', 'U', 'T', 'E', 'R']
	list_of_blank_word	- ['_', '_', '_', 'P', '_', '_', '_', '_']

	Swap will happen until all letters match in both list
	"""

	list_of_game_word = list(game_word.upper())
	list_of_blank_word = list(blank_word)

	# List to store the letters that are not part of the word, also to keep count of the total number of attempts
	attempts = []

	# Function calls get letter from keyboard
	def guess(letter):
		game(letter)
		
	# Main game function
	def game(letter):

		# Code for Correct Guess ---------------------------------------------------------------------------------
		if letter in list_of_game_word:

			# Code to find all index
			indx = [] 														# to store index values of letters
			for i in range(len(list_of_game_word)):							
				if(list_of_game_word[i] == letter):							# list indx contains the index of the letter in the word
					indx.append(i)
			# Code to swap index
			for i in range(len(indx)):
				for i in indx:
					list_of_blank_word[i] = list_of_game_word[i]			# Switching the letter and blank at the same index

			# Prints guess to board
			print_new_word = Label(game_display, text = list_of_blank_word, font=('Rockwell',35), bg = "cyan")
			print_new_word.place(x = 480, y = 300)

		# Code if User Guesses Max number of Attempts allowed. ---------------------------------------------------
		if len(attempts) == 11:
			revealword = ("The Word Was: "+ wordList[wordIndex])
			reveal_word = Label(game_display,text = revealword.upper(), font=('Rockwell',25, 'bold'), bg = "cyan")
			reveal_word.place(x = 400, y = 400)

			messagebox.showinfo("HANGMAN","You ran out of Guesses. You Lost.")
			game_display.destroy()

		# Code for Incorrect Guess -------------------------------------------------------------------------------
		# With every incorrect guess, game prints out an image of hangman and the incorrect letter to the game display

		if letter not in list_of_game_word:
			attempts.append(letter)
			if len(attempts) != 12:
				image_display.config(image=photos[len(attempts)])
				print_new_word = Label(game_display, text = attempts, font=('Rockwell',35), fg = "red", bg = "cyan")
				print_new_word.place(x = 400, y = 475)

		# Win condition code ----------------------------------------------------------------------------------
		if list_of_game_word == list_of_blank_word:
			messagebox.showinfo("HANGMAN","You guessed them all! YOU WIN!")
			game_display.destroy()

# TOPIC 2 - Sorting
def Sorting():
	# Code for implementing the Keyboard on screen -------------------------------------------------------------------------------------------------------------
	"""
	Wanted to implement the alphabets on the game screen, rather than having the user typing it in.
	I found this code from https://www.youtube.com/watch?v=esHcFbNlNqQ
	I made changes to it to for my program
	"""

	# Code to print keyboard to screen ----------------------------------------------------------------------------------------------------------------------
	n = 0 
	xvar = 15
	yvar = 550
	for c in ascii_uppercase:
		keyboard = Button(game_display, text=c, command= lambda c=c: guess(c), activebackground="blue", font= ("Rockwell 16"),width=3, bg ="light blue")
		keyboard.grid(row=1+n//9, column=n%9)
		keyboard.place(x=xvar, y=yvar)
		keyboard = Button(command=switch)
		n+=1
		xvar+=45

	# Code to get the word from data file ----------------------------------------------------------------------------------------------------------------------
	wordList = []
	with open('topic_2_words.dat','r') as file:
		# reading each line    
		for line in file:
			# reading each word        
			for word in line.split():
				wordList.append(word)

	wordIndex = random.randint(0, len(wordList) - 1)

	# Showing user what topic they chose
	title = Label(game_display, text = "You chose: Sorting", font=('Rockwell', 25, 'bold'), bg = "cyan")
	title.place(x = 400, y = 200)

	# Code to display the number of letters of the word -------------------------------------------------------------------------------------------------------
	game_word = (wordList[wordIndex])																	# Main Game Word
	blank_word = ["_" for i in game_word]																# Game Word in Blanks
	guess_word = Label(game_display, text = blank_word, font=('Rockwell',33, 'bold'), bg = "cyan")
	guess_word.place(x = 480, y = 300)


	"""
	I created two lists here. list_of_game_word creates a list of the gameword. list_of_blank_word is a list of the blanks.
	If the letter inputed by the user is in the list_of_game_word, it all that letter at that index into the list_of_blank_word

	It would look like this if run through the terminal.
						
	game_word 			- computer
	blank_word 			- ________
	list_of_game_word 	- ['C', 'O', 'M', 'P', 'U', 'T', 'E', 'R']
	list_of_blank_word	- ['_', '_', '_', '_', '_', '_', '_', '_']

	If user guessed P

	list_of_game_word 	- ['C', 'O', 'M', 'P', 'U', 'T', 'E', 'R']
	list_of_blank_word	- ['_', '_', '_', 'P', '_', '_', '_', '_']

	Swap will happen until all letters match in both list
	"""

	list_of_game_word = list(game_word.upper())
	list_of_blank_word = list(blank_word)

	# List to store the letters that are not part of the word, also to keep count of the total number of attempts
	attempts = []

	# Function calls get letter from keyboard
	def guess(letter):
		game(letter)
		
	# Main game function
	def game(letter):

		# Code for Correct Guess ---------------------------------------------------------------------------------
		if letter in list_of_game_word:

			# Code to find all index
			indx = [] 														# to store index values of letters
			for i in range(len(list_of_game_word)):							
				if(list_of_game_word[i] == letter):							# list indx contains the index of the letter in the word
					indx.append(i)
			# Code to swap index
			for i in range(len(indx)):
				for i in indx:
					list_of_blank_word[i] = list_of_game_word[i]			# Switching the letter and blank at the same index

			# Prints guess to board
			print_new_word = Label(game_display, text = list_of_blank_word, font=('Rockwell',35), bg = "cyan")
			print_new_word.place(x = 480, y = 300)

		# Code if User Guesses Max number of Attempts allowed. ---------------------------------------------------
		if len(attempts) == 11:
			revealword = ("The Word Was: "+ wordList[wordIndex])
			reveal_word = Label(game_display,text = revealword.upper(), font=('Rockwell',25, 'bold'), bg = "cyan")
			reveal_word.place(x = 400, y = 400)

			messagebox.showinfo("HANGMAN","You ran out of Guesses. You Lost.")
			game_display.destroy()

		# Code for Incorrect Guess -------------------------------------------------------------------------------
		# With every incorrect guess, game prints out an image of hangman and the incorrect letter to the game display

		if letter not in list_of_game_word:
			attempts.append(letter)
			if len(attempts) != 12:
				image_display.config(image=photos[len(attempts)])
				print_new_word = Label(game_display, text = attempts, font=('Rockwell',35), fg = "red", bg = "cyan")
				print_new_word.place(x = 400, y = 475)

		# Win condition code ----------------------------------------------------------------------------------
		if list_of_game_word == list_of_blank_word:
			messagebox.showinfo("HANGMAN","You guessed them all! YOU WIN!")
			game_display.destroy()

# TOPIC 3 - Sensors
def Sensors():

	# Code for implementing the Keyboard on screen -------------------------------------------------------------------------------------------------------------
	"""
	Wanted to implement the alphabets on the game screen, rather than having the user typing it in.
	I found this code from https://www.youtube.com/watch?v=esHcFbNlNqQ
	I made changes to it to for my program
	"""

	# Code to print keyboard to screen ----------------------------------------------------------------------------------------------------------------------
	n = 0 
	xvar = 15
	yvar = 550
	for c in ascii_uppercase:
		keyboard = Button(game_display, text=c, command= lambda c=c: guess(c), activebackground="blue", font= ("Rockwell 16"),width=3, bg ="light blue")
		keyboard.grid(row=1+n//9, column=n%9)
		keyboard.place(x=xvar, y=yvar)
		keyboard = Button(command=switch)
		n+=1
		xvar+=45

	# Code to get the word from data file ----------------------------------------------------------------------------------------------------------------------
	wordList = []
	with open('topic_3_words.dat','r') as file:
		# reading each line    
		for line in file:
			# reading each word        
			for word in line.split():
				wordList.append(word)

	wordIndex = random.randint(0, len(wordList) - 1)

	# Showing user what topic they chose
	title = Label(game_display, text = "You chose: Sensors", font=('Rockwell', 25, 'bold'), bg = "cyan")
	title.place(x = 400, y = 200)

	# Code to display the number of letters of the word -------------------------------------------------------------------------------------------------------
	game_word = (wordList[wordIndex])																	# Main Game Word
	blank_word = ["_" for i in game_word]																# Game Word in Blanks
	guess_word = Label(game_display, text = blank_word, font=('Rockwell',33, 'bold'), bg = "cyan")
	guess_word.place(x = 480, y = 300)


	"""
	I created two lists here. list_of_game_word creates a list of the gameword. list_of_blank_word is a list of the blanks.
	If the letter inputed by the user is in the list_of_game_word, it all that letter at that index into the list_of_blank_word

	It would look like this if run through the terminal.
						
	game_word 			- computer
	blank_word 			- ________
	list_of_game_word 	- ['C', 'O', 'M', 'P', 'U', 'T', 'E', 'R']
	list_of_blank_word	- ['_', '_', '_', '_', '_', '_', '_', '_']

	If user guessed P

	list_of_game_word 	- ['C', 'O', 'M', 'P', 'U', 'T', 'E', 'R']
	list_of_blank_word	- ['_', '_', '_', 'P', '_', '_', '_', '_']

	Swap will happen until all letters match in both list
	"""

	list_of_game_word = list(game_word.upper())
	list_of_blank_word = list(blank_word)

	# List to store the letters that are not part of the word, also to keep count of the total number of attempts
	attempts = []

	# Function calls get letter from keyboard
	def guess(letter):
		game(letter)
		
	# Main game function
	def game(letter):

		# Code for Correct Guess ---------------------------------------------------------------------------------
		if letter in list_of_game_word:

			# Code to find all index
			indx = [] 														# to store index values of letters
			for i in range(len(list_of_game_word)):							
				if(list_of_game_word[i] == letter):							# list indx contains the index of the letter in the word
					indx.append(i)
			# Code to swap index
			for i in range(len(indx)):
				for i in indx:
					list_of_blank_word[i] = list_of_game_word[i]			# Switching the letter and blank at the same index

			# Prints guess to board
			print_new_word = Label(game_display, text = list_of_blank_word, font=('Rockwell',35), bg = "cyan")
			print_new_word.place(x = 480, y = 300)

		# Code if User Guesses Max number of Attempts allowed. ---------------------------------------------------
		if len(attempts) == 11:
			revealword = ("The Word Was: "+ wordList[wordIndex])
			reveal_word = Label(game_display,text = revealword.upper(), font=('Rockwell',25, 'bold'), bg = "cyan")
			reveal_word.place(x = 400, y = 400)

			messagebox.showinfo("HANGMAN","You ran out of Guesses. You Lost.")
			game_display.destroy()

		# Code for Incorrect Guess -------------------------------------------------------------------------------
		# With every incorrect guess, game prints out an image of hangman and the incorrect letter to the game display

		if letter not in list_of_game_word:
			attempts.append(letter)
			if len(attempts) != 12:
				image_display.config(image=photos[len(attempts)])
				print_new_word = Label(game_display, text = attempts, font=('Rockwell',35), fg = "red", bg = "cyan")
				print_new_word.place(x = 400, y = 475)

		# Win condition code ----------------------------------------------------------------------------------
		if list_of_game_word == list_of_blank_word:
			messagebox.showinfo("HANGMAN","You guessed them all! YOU WIN!")
			game_display.destroy()

# TOPIC 4 - Image Processing
def ImgProcessing():
	# Code for implementing the Keyboard on screen -------------------------------------------------------------------------------------------------------------
	"""
	Wanted to implement the alphabets on the game screen, rather than having the user typing it in.
	I found this code from https://www.youtube.com/watch?v=esHcFbNlNqQ
	I made changes to it to for my program
	"""

	# Code to print keyboard to screen ----------------------------------------------------------------------------------------------------------------------
	n = 0 
	xvar = 15
	yvar = 550
	for c in ascii_uppercase:
		keyboard = Button(game_display, text=c, command= lambda c=c: guess(c), activebackground="blue", font= ("Rockwell 16"),width=3, bg ="light blue")
		keyboard.grid(row=1+n//9, column=n%9)
		keyboard.place(x=xvar, y=yvar)
		keyboard = Button(command=switch)
		n+=1
		xvar+=45

	# Code to get the word from data file ----------------------------------------------------------------------------------------------------------------------
	wordList = []
	with open('topic_4_words.dat','r') as file:
		# reading each line    
		for line in file:
			# reading each word        
			for word in line.split():
				wordList.append(word)

	wordIndex = random.randint(0, len(wordList) - 1)

	# Showing user what topic they chose
	title = Label(game_display, text = "You chose: Image Processing", font=('Rockwell', 25, 'bold'), bg = "cyan")
	title.place(x = 400, y = 200)

	# Code to display the number of letters of the word -------------------------------------------------------------------------------------------------------
	game_word = (wordList[wordIndex])																	# Main Game Word
	blank_word = ["_" for i in game_word]																# Game Word in Blanks
	guess_word = Label(game_display, text = blank_word, font=('Rockwell',33, 'bold'), bg = "cyan")
	guess_word.place(x = 480, y = 300)


	"""
	I created two lists here. list_of_game_word creates a list of the gameword. list_of_blank_word is a list of the blanks.
	If the letter inputed by the user is in the list_of_game_word, it all that letter at that index into the list_of_blank_word

	It would look like this if run through the terminal.
						
	game_word 			- computer
	blank_word 			- ________
	list_of_game_word 	- ['C', 'O', 'M', 'P', 'U', 'T', 'E', 'R']
	list_of_blank_word	- ['_', '_', '_', '_', '_', '_', '_', '_']

	If user guessed P

	list_of_game_word 	- ['C', 'O', 'M', 'P', 'U', 'T', 'E', 'R']
	list_of_blank_word	- ['_', '_', '_', 'P', '_', '_', '_', '_']

	Swap will happen until all letters match in both list
	"""

	list_of_game_word = list(game_word.upper())
	list_of_blank_word = list(blank_word)

	# List to store the letters that are not part of the word, also to keep count of the total number of attempts
	attempts = []

	# Function calls get letter from keyboard
	def guess(letter):
		game(letter)
		
	# Main game function
	def game(letter):

		# Code for Correct Guess ---------------------------------------------------------------------------------
		if letter in list_of_game_word:

			# Code to find all index
			indx = [] 														# to store index values of letters
			for i in range(len(list_of_game_word)):							
				if(list_of_game_word[i] == letter):							# list indx contains the index of the letter in the word
					indx.append(i)
			# Code to swap index
			for i in range(len(indx)):
				for i in indx:
					list_of_blank_word[i] = list_of_game_word[i]			# Switching the letter and blank at the same index

			# Prints guess to board
			print_new_word = Label(game_display, text = list_of_blank_word, font=('Rockwell',35), bg = "cyan")
			print_new_word.place(x = 480, y = 300)

		# Code if User Guesses Max number of Attempts allowed. ---------------------------------------------------
		if len(attempts) == 11:
			revealword = ("The Word Was: "+ wordList[wordIndex])
			reveal_word = Label(game_display,text = revealword.upper(), font=('Rockwell',25, 'bold'), bg = "cyan")
			reveal_word.place(x = 400, y = 400)

			messagebox.showinfo("HANGMAN","You ran out of Guesses. You Lost.")
			game_display.destroy()

		# Code for Incorrect Guess -------------------------------------------------------------------------------
		# With every incorrect guess, game prints out an image of hangman and the incorrect letter to the game display

		if letter not in list_of_game_word:
			attempts.append(letter)
			if len(attempts) != 12:
				image_display.config(image=photos[len(attempts)])
				print_new_word = Label(game_display, text = attempts, font=('Rockwell',35), fg = "red", bg = "cyan")
				print_new_word.place(x = 400, y = 475)

		# Win condition code ----------------------------------------------------------------------------------
		if list_of_game_word == list_of_blank_word:
			messagebox.showinfo("HANGMAN","You guessed them all! YOU WIN!")
			game_display.destroy()

game_display.mainloop()
