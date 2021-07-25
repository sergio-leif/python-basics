
"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list 
of only the first and last elements of the given list. For practice, write this code inside a function.

"""

def list_ends(number_list):
    result = [number_list.pop(0), number_list.pop(len(number_list)-1)]
    print(result)


a = [5, 10, 15, 20, 25]
list_ends(a)