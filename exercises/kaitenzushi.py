"""
There are NN dishes in a row on a kaiten belt, with the iith dish being of type Di. Some dishes may be of the same type as one another.

You're very hungry, but you'd also like to keep things interesting. The NN dishes will arrive in front of you, one after another in order, and for each one you'll eat it as long as it isn't the same type as any of the previous KK dishes you've eaten. You eat very fast, so you can consume a dish before the next one gets to you. Any dishes you choose not to eat as they pass will be eaten by others.
Determine how many dishes you'll end up eating.

Constraints

1≤N≤500,000
1≤K≤N
1≤Di≤1,000,000

Sample test case #1
N = 6
D = [1, 2, 3, 3, 2, 1]
K = 1
Expected Return Value = 5

Sample test case #2
N = 6
D = [1, 2, 3, 3, 2, 1]
K = 2
Expected Return Value = 4

Sample test case #3
N = 7
D = [1, 2, 1, 2, 1, 2, 1]
K = 2
Expected Return Value = 2

Sample Explanation
In the first case, the dishes have types of [1, 2, 3, 3, 2, 1][1,2,3,3,2,1], so you'll eat the first 33 dishes, skip the next one as it's another type-33 dish, and then eat the last 22.
In the second case, you won't eat a dish if it has the same type as either of the previous 22 dishes you've eaten. After eating the first, second, and third dishes, you'll skip the fourth and fifth dishes as they're the same type as the last 22 dishes that you've eaten. You'll then eat the last dish, consuming 44 dishes total.
In the third case, once you eat the first two dishes you won't eat any of the remaining dishes.
"""

from typing import List
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    recents = []
    eaten = 0
    for dish in D:
        if dish not in recents:
            eaten+=1
            recents.append(dish)
        if len(recents) > K:
            recents.pop(0)
    return eaten

N = 7
D = [1, 2, 1, 2, 1, 2, 1]
K = 2

print(getMaximumEatenDishCount(N, D, K))