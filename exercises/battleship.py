from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  print("Value of G: " + str(str(G).count('1')))
  return str(G).count('1')/(R*C)

R = 2
C = 3
G = [[ 0 , 0 , 1], [1, 1, 0]]
print(getHitProbability(R, C, G))