
# Error handling

# https://docs.python.org/3/library/exceptions.html

while True:
    try:
        age = int(input('What is your age? '))
        10/age
        # raise ValueError('Hey cut it out')
    except ValueError:
        print('Please enter a number')
        continue
    except ZeroDivisionError:
        print('Please enter age higher than 0')
    else:
        print('Thank you!')
        break
    finally:
        print('ok, I am finally free')

# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(err)

# print(sum(1,'2'))