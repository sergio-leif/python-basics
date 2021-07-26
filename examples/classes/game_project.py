
class PlayerCharacter:
    membership = True
    def __init__(self, name='anonymous', age=0): #By default, values are anonymous and 0
        if (PlayerCharacter.membership):
            self.name = name
            self.age = age

    def run(self):
      print('run')
      return 'done'

player1 = PlayerCharacter("Sergio", 28)
player2 = PlayerCharacter("Tommy", 32)
player3 = PlayerCharacter()

player2.attack = 50
print(player1.name)
print(player1.run())
print(player2.age)
print(player2.attack)
print(player3.name)