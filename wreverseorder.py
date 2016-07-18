"""
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.

"""
sentence = input("Type your sentence to be reversed: ")
words = sentence.split()
reversesentence = words[::-1]
reversesentencev2 = " ".join(reversesentence)
nospacessentence = "".join(sentence.split("e"))

print (sentence)
print (reversesentence)
print (reversesentencev2)
print (nospacessentence)