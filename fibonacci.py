"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

def fibonacci(numbers):
	if numbers == 0 :
		fibo = []
		return fibo
	elif numbers == 1:
		fibo = [1]
		return fibo
	elif numbers == 2:
		fibo = [1,1]
		return fibo
	else:
		numbers = numbers-2
		fibo = [1,1]
		while numbers != 0:
			fibo.append(fibo[-1]+fibo[-2])
			numbers -= 1
		return fibo

def validate(number):
	if not number.isnumeric():
		number = input("Please type an integer number: ")
		validate(number)	
	else:
		return int(number)

number = input("Please type an integer number: ")
print (fibonacci(validate(number)))
