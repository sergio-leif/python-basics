"""
Binary Search is a searching algorithm for finding an element's position in a sorted array.

Binary search can be implemented only on a sorted list of items. If the elements are not sorted already, 
we need to sort them first.
"""

def binary_search(array , num):
    low = 0
    high = len(array)-1

    while low != high-1:
        mid = (low + high)//2
        if array[mid] == num:
            return mid
        if array[mid] < num:
            low = mid
        if array[mid] > num:
            high = mid
        print(f"Mid: {mid}, high: {high}, low: {low}")
    return None


array = [2, 3, 5, 12, 13, 17, 42, 51, 102, 192, 345, 401, 599]
num = 401

print(binary_search(array, num))