
class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

class Wizard(User): #Inheritance
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power {self.power}')

wizard1 = Wizard('Merlin', 50, 'merlin@email.com')

print(wizard1.email)
