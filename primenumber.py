"""
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to [Exercise 4](/exercise/2014/02/26/04-divisors.html to help you. Take this opportunity to practice using functions, described below.
Discussion

Concepts for this week:

    Functions
    Reusable functions
    Default arguments
"""



def checkprime(number):
	a = 0
	firstprimenumbers = [2,3]
	if number in firstprimenumbers:
		return True
	elif number == 1 or number == 0:
		return False
	for i in range(2,number - 1):
		if number%i == 0:
			a += 1
	if a == 0 :
		return True
	else :
		return False

def validateinput(number):
	if number == "exit":
		print ("Exit to console !")
		raise SystemExit		
	elif not number.isnumeric():
		print("Please enter a valid integer number!")
		number = input("Number to check: ").lower()
		return validateinput(number)
	else:		
		return int(number)


while True == True:
	number = input("Number to check: ").lower()
	if checkprime(validateinput(number)) is True:
		print (number," is prime!")
	else:
		print (number," is not prime!")
	
