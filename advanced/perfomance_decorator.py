#performance decorator.
from time import time
def performance(fn):
  def wrapper(*args, **kwargs):
    t1 = time()
    result = fn(*args, **kwargs)
    t2 = time()
    print("took {} s").format(t2-t1)
    return result
  return wrapper

@performance
def long_time():
    for i in range(100000):
        i*5

long_time()