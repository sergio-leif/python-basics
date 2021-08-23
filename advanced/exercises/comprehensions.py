
# Get the duplicate chars in the next list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

result_list = list(set([char for char in some_list if some_list.count(char) > 1]))
print(result_list)