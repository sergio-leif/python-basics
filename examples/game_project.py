
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
      print('run')
      return 'done'

player1 = PlayerCharacter("Sergio", 28)
player2 = PlayerCharacter("Tommy", 32)

print(player1.name)
print(player1.run())
print(player2.age)