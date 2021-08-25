
# iterable
# iterate
# generators are good for big loops, avoding use of memory

def generator_function(num):
    for i in range(num):
        yield i

g = generator_function(100)
next(g)
next(g)
print(next(g))