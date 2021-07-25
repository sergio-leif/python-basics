
"""
Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

- 1 Instantiate the Cat object with 3 cats
- 2 Create a function that finds the oldest cat
- 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
"""

def find_oldest(*args):
    return max(cat1.age, cat2.age, cat3.age)

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Jeff", 4)
cat2 = Cat("Miau", 7)
cat3 = Cat("Bichi", 2)

print("The oldest cat is " + str(find_oldest()) + " years old.")