'''
The scoreboard does not display the number of problems in the contest, nor their point values. Using the information available, you would like to 
determine the minimum possible number of problems in the contest.

Constraints

1≤N≤500,000
1≤Si≤1,000,000,000

Sample test case #1
N = 6
S = [1, 2, 3, 4, 5, 6]
Expected Return Value = 4

Sample test case #2
N = 4
S = [4, 3, 3, 4]
Expected Return Value = 3
Sample test case #3
N = 4
S = [2, 4, 6, 8]
Expected Return Value = 4

'''

from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
    minimum_questions = int(max(S)//2)
    print(minimum_questions)
    odds = set([i%2 for i in S])
    print(odds)
    if 1 in odds:
        return minimum_questions + 1
    else:
        return minimum_questions


N = 6
S = [1, 2, 4, 3, 5, 6]

print(getMinProblemCount(N, S))