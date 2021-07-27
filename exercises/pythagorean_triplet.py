"""

Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.

Example: 

Input: arr[] = {3, 1, 4, 6, 5} 
Output: True 
There is a Pythagorean triplet (3, 4, 5).
Input: arr[] = {10, 4, 6, 12, 5} 
Output: False 
There is no Pythagorean triplet. 

"""

def exponent(n):
    return n**2

array = {3, 1, 4, 6, 5}

print(array)
exponent_array = list(map(exponent, array))

# print(list(map(multiply_by2, my_list)))