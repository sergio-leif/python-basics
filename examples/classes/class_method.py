
class PlayerCharacter:
    membership = True
    def __init__(self, name='anonymous', age=0): #By default, values are anonymous and 0
        if (PlayerCharacter.membership):
            self.name = name
            self.age = age

    @classmethod
    def adding_things(cls, num1, num2): # It can be called without instanciate first
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(cls, num1, num2): # It doesn't have access to the class
        return num1 + num2

    def _private_method(self): # Private method that is just used inside the class
        self._private_variable = 'Private' # Private variable that is just used inside the class and can not be overwrite
        print('Private method')

# print(PlayerCharacter.adding_things(2, 3))
player1 = PlayerCharacter.adding_things(2, 3)
print(player1)