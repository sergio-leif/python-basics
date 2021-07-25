
"""

Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. For example, say I 
type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.

"""

def reverse_phrase(phrase):
    splited_phrase = phrase.split(" ")
    reverse_list = splited_phrase[::-1]
    result = " ".join(reverse_list)
    print(result)

phrase = input("Write the phrase to reverse:\n")

reverse_phrase(phrase)
