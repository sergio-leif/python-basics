#MRO - Method Resolution Order
class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

print(D.mro()) #It says the order to get the info in the super classes.