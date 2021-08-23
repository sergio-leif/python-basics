from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

# Answer:
def caps(item):
    return item.capitalize()

print(list(map(caps, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

# Answer:
my_numbers.sort()
print(my_numbers)
print(list(zip(my_strings, my_numbers)))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

# Answer:
def pass_over(item):
    return item > 50

print(list(filter(pass_over, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

# Answer:

def combine(comb, item):
    return comb + item

print(reduce(combine, my_numbers + scores, 0))