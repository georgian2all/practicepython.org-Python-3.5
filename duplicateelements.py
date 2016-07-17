"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

    Write two different functions to do this - one using a loop and constructing a list, and another using sets.
    Go back and do Exercise 5 using sets, and write the solution for that in a different function.

"""
a = ["Mar","Tigru","Cires","Mar","Coriandru","Cires"]

def uniqueelements(alist):
	b = []
	for i in range(0,len(alist)):
		if alist[i] not in b:
			b.append(alist[i])
	return b

def setuniqueelements(alist):
	alist = list(set(alist))
	return alist
	

print ("Unique elemnts using a function to return a list")
print (a)
print (uniqueelements(a))

print ("Unique elemnts using  sets  ")
print (a)
print (setuniqueelements(a))