"""

Problem statement: Given an Amazon reviews paragraph containing several words, find the minimum distance 
between two given words.

Example: Following is a hypothetical paragraph in an amazon review –

“Amazon is the best company to work for. The amazon is a beautiful forest.”

Find the minimum distance between ‘Amazon’ and ‘The’

Given: You are given the position of each word in the paragraph. Meaning, you know that word ‘Amazon’ occurs 
at positions 1 and 10, and ‘The’ occurs at 3 and 9. You do not have to parse the paragraph to gather this info.

Sub questions :
*Which data structure will you use to store the given info?
*Compute the minimum distance in the most efficient way.
*Give a working code for the same.

"""

def calculate_distance(positions1, positions2):
    minimum = 0
    for a in positions1:
        for b in positions2:
            if a > b:
                if minimum > (n := a - b) or minimum == 0:
                    minimum = n
            else:
                if minimum > (n := b - a) or minimum == 0:
                    minimum = n
    return minimum

def get_same_elements(array, element):
    result = []
    counter = 0
    for x in array:
        if x == element:
            result.append(counter)
        counter += 1
    return result

phrase = "Amazon is the best company to work for. The amazon is a beautiful forest.".lower().replace(',','').replace('.','')
word1 = "forest".lower()
word2 = "best".lower()

array_phrase = list(phrase.split())

positions1, positions2 = get_same_elements(array_phrase, word1), get_same_elements(array_phrase, word2)

# print(positions1)
# print(positions2)
print("The minimum distance is " + str(calculate_distance(positions1, positions2)))
