# map, filter, zip, and reduce

from functools import reduce

my_list = [1,2,3]

# Map
def multiply_by2(item):
    return item*2

# print(multiply_by2([1,2,3]))
# print(list(map(multiply_by2, my_list)))


# Filter
def only_odd(item):
    return item % 2 != 0

# print(list(filter(only_odd, my_list)))

# Reduce
def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))