
"""

Given two numbers represented by two lists, write a function that returns the sum list. The sum list 
is a list representation of the addition of two input numbers.

Example:

Input: 
List1: 5->6->3 // represents number 563 
List2: 8->4->2 // represents number 842 
Output: 
Resultant list: 1->4->0->5 // represents number 1405 
Explanation: 563 + 842 = 1405
Input: 
List1: 7->5->9->4->6 // represents number 75946
List2: 8->4 // represents number 84
Output: 
Resultant list: 7->6->0->3->0// represents number 76030
Explanation: 75946+84=76030

"""

list1 = [7, 5, 9, 4, 6]
list2 = [8, 4]

def get_number(array):
    return int(str(array).replace(', ', '').replace('[','').replace(']',''))

def sum(array1, array2):
    list3 = [array1 + array2]
    return list3

print(sum(get_number(list1), get_number(list2)))