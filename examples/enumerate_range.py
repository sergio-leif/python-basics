# Enumerate

for i, char in enumerate(list(range(100))):
    print(i, char)
    if char == 50:
        print(f'index of 50 is: {i}')


# Range
# range(initial, final, each number)

for _ in range(10, 0, -1):
    print(_)