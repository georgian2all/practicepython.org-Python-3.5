"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
"""
from random import randint

def firstlast():
	a = [randint(1,99) for i in range(randint(1,30))]
	print ("First random list: ",a)
	if len(a)==1:
		print ("The list contains one element")
	elif len(a)==2:
		b = a	
	else:
		b = [a[0],a[len(a)-1]]
	print ("First and last element: ",b)
	
firstlast()