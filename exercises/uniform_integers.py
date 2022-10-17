"""
A positive integer is considered uniform if all of its digits are equal. For example, 222222 is uniform, while 223223 is not.
Given two positive integers AA and BB, determine the number of uniform integers between AA and BB, inclusive.
Please take care to write a solution which runs within the time limit.

Constraints
1≤A≤B≤10^12
 
Sample test case #1
A = 75
B = 300
Expected Return Value = 5
Sample test case #2
A = 1
B = 9
Expected Return Value = 9
Sample test case #3
A = 999999999999
B = 999999999999
Expected Return Value = 1
Sample Explanation
In the first case, the uniform integers between 7575 and 300300 are 7777, 8888, 9999, 111111, and 222222.
In the second case, all 99 single-digit integers between 11 and 99 (inclusive) are uniform.
In the third case, the single integer under consideration (999{,}999{,}999{,}999999,999,999,999) is uniform.
"""
# Solution 1, not ideal as it consums a lot of time
def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    counter = 0
    for number in range(A,B+1):
        if len(set(str(number))) == 1:
            counter+=1
    return counter

# Solution 2, ideal solution: less time consumption
def getIdealUniformIntegerCountInInterval(A: int, B: int) -> int:
    counter = 0
    maxDigits = len(str(B))
    minDigits = len(str(A))
    basics = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    uniform = []
    for digit in range (minDigits, maxDigits+1):
        position = 0
        for position in range (len(basics)):
            uniform.append(basics[position]*digit)
            position+=1
    for number in uniform:
            if int(number) >= A and int(number) <= B:
                counter+=1
    return counter

A = 3
B = 9999

print(getUniformIntegerCountInInterval(A, B))
print(getIdealUniformIntegerCountInInterval(A, B))