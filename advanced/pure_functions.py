# map, filter, zip, and reduce

my_list = [1,2,3]

# Map
def multiply_by2(item):
    return item*2

# print(multiply_by2([1,2,3]))
print(list(map(multiply_by2, my_list)))


# Filter
def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))
