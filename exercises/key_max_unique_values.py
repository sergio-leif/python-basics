"""
Given a dictionary with a values list, extract the key whose value has the most unique values.

Input : test_dict = {"Gfg" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]} 
Output : "Gfg" 
Explanation : "Gfg" having max unique elements i.e 5. 
"""
def get_key(test_dict):
    values = []
    max_uniques = 0
    max_key = ""

    for k,v in test_dict.items():
        if len(set(v)) > max_uniques:
            max_uniques = len(set(v))
            max_key = k
    return max_key


test_dict = {"Gfg" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}
print(get_key(test_dict))