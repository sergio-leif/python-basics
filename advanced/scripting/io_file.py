# my_file = open('test.txt')

# print(my_file.read()) # Read function let the cursor at the end of the file, so in case we want read again, it will not show anything because there is nothing new.
# my_file.seek(0) # Change the position of the cursor to the indicated index
# # print(my_file.read())

# print(my_file.readline())

# my_file.close()

# Correct way to do it:
try:
    with open('./files/test.txt', mode='a') as my_file: #r: read, a: append, w: write, r+: read & write
        text = my_file.write('Hey it\'s me!')
        # print(my_file.readlines())
        print(text)
except FileNotFoundError as err:
    print('File does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise err