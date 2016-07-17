"""
This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).
"""

from random import randint

a = [1, 1, 2, 3, 5, 8, 13, 21, 12, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [item for item in set(a) if item in b]
print ("First list: ",a)
print ("Second list: ",b)
print ("Common elements",c)


a = [item for item in range(1,randint(1,20))]
a = [item for item in range(1,randint(1,20))]
c = [item for item in a and b if item in a and b]
print ("Random generated lists")
print ("First list: ",a)
print ("Second list: ",b)
print ("Common elements",c)