class Hero:
    Head = 1
    Ability = True
    def __init__(self, name, nickname, hp, damage):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage
    def heal(self):
        print(self.hp + 100)
    def two_damage(self):
        print(self.damage * 2)
    def greeting(self):
        print(f'my name is {self.name}')
    def brand_phrase(self):
        print('good will win')
h1 = Hero(name = 'Elprimo', nickname = 'Primas', hp = 810, damage = 200 )
h2 = Hero(name = 'Edgar', nickname = 'Nefor',hp = 450, damage = 120 )
h3 = Hero(name = 'Mortis', nickname = 'Matras', hp = 540, damage = 102)
h4 = Hero(name = 'Frank', nickname = 'Zombie', hp = 945, damage = 167)

h1.heal()
h2.two_damage()
h3.greeting()
h4.brand_phrase()

