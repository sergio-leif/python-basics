# lambda expressions

# Lambda expressions is used to functions are used just once
# lambda param: action(param)

from functools import reduce

my_list = [1,2,3]

# def multiply_by2(item):
#     return item*2

print(list(map(lambda item: item*2, my_list)))

# def only_odd(item):
#     return item % 2 != 0

print(list(filter(lambda item: item % 2 != 0, my_list)))

# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item

print(reduce(lambda acc,item: acc+item, my_list))