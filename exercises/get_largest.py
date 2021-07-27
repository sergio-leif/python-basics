
"""
Write an efficient program for printing k largest elements in an array. Elements in array can be in any order.
For example, if given array is [1, 23, 12, 9, 30, 2, 50] and you are asked for the largest 3 elements i.e., k = 3 
then your program should print 50, 30, and 23.

"""

def get_largest(k):
    b = a
    result = []
    for x in range(k):
        result.append(max(b))
        b.remove(max(b))
    return result

a = [1, 23, 12, 9, 30, 2, 50]
k = int(input("Elements to get? "))

print(get_largest(k))
