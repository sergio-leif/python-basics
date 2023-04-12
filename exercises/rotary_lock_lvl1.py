'''
You're trying to open a lock. The lock comes with a wheel which has the integers from 1 to N arranged in a circle in order around it (with integers 1 
and N adjacent to one another). The wheel is initially pointing at 1.

It takes 1 second to rotate the wheel by 1 unit to an adjacent integer in either direction, and it takes no time to select an integer once the wheel is pointing at it.
The lock will open if you enter a certain code. The code consists of a sequence of M integers, the ith of which is C i. Determine the minimum number of seconds 
required to select all M of the code's integers in order.

Constraints

3≤N≤50,000,000
1≤M≤1,000
1≤Ci≤N

Sample test case #1

N = 3
M = 3
C = [1, 2, 3]
Expected Return Value = 2

Sample test case #2

N = 10
M = 4
C = [9, 4, 4, 8]
Expected Return Value = 11
'''

from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  max_rotation = N//2
  if N%2 == 1:
    max_rotation += 1

  locker_side1 = list(range(1, N+1))
  current_position = 1
  seconds = 0

  for number in C:
    distance = abs(locker_side1.index(current_position)-locker_side1.index(number))
    if distance > max_rotation:
        distance = N - distance
    seconds += distance
    current_position=number
  return seconds

N = 10
M = 4
C = [9, 4, 4, 8]

getMinCodeEntryTime(N, M, C)