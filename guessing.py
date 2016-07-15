#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python 3.5
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random
guesses = 0
gamescore = 0
def checknumber(number):
	global guesses
	global gamescore
	if number == "exit":
		print ("Game OVER ")
		print ("Your score is: ", gamescore, "|"," Attempts: ", guesses)		
		raise SystemExit
	elif not number.isnumeric() :
		print ("Error !\n Only numbers between 1 and 9 are accepted or Exit command!")
		number = input("Your number: ")
		return checknumber(number)
	elif (int(number)<1) or (int(number)>9) :
		print ("Error !\n Only numbers between 1 and 9 are accepted or Exit command!")
		number = input("Your number: ")
		return checknumber(number)	
	else:
		return int(number)

def makescore(number):	
	gscore = 0
	score = {0 : 8,
			 1 : 7,
			 2 : 6,
			 3 : 5,
			 4 : 4,
			 5 : 3,
			 6 : 2,
			 7 : 1,
			 8 : 0
			}	
	rnumber = random.randint(1,9)
	number = int(number)
	gscore += score[abs(rnumber - number)]
	if rnumber == number:
		print ("You guessed exactly right!")
	elif rnumber > number:
		print ("You guessed too low !", "Our number (",rnumber,")")
	else :
		print ("You guessed to high !", "Our number (",rnumber,")")
		
	print ("This round score: ", score[abs(rnumber - number)])
	return gscore

while True :
	guessnumber = checknumber(input("Your number: ").lower())
	gamescore +=  makescore(guessnumber)
	guesses += 1 
	print ("Your score is: ", gamescore, "|"," Attempts: ", guesses)
	
	
		