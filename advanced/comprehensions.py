# More examples in: https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/loops/list-comprehensions

# list, set, dictionary

#my_list = [param for param in iterable]

my_list = [char for char in 'hello']

# for char in 'hello':
#     my_list.append(char)

my_set = {num for num in range(100)}
my_list3 = [num**2 for num in range(100)]
my_list4 = [num**2 for num in range(100) if num % 2 == 0]

# print(my_list)
# print(my_set)
# print(my_list3)
# print(my_list4)

# Dictionaries
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key:value**2 for key,value in simple_dict.items() if value%2==0}
my_dict2 = {num:num*2 for num in [1,2,3]}
print(my_dict)
print(my_dict2)