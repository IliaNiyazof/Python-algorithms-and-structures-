from pympler import asizeof
class Person:

    def __init__(self, name, health, armor, damage):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage

    def calculate_damage(self, enemy):
        return self.damage / enemy.armor

    def attack(self, enemy):
        enemy.health -= self.calculate_damage(enemy)


class Player(Person):
    pass


class Enemy(Person):
    pass


class Game:

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        last_attacker = self.player
        while self.player.health > 0 and self.enemy.health > 0:
            if last_attacker == self.player:
                self.enemy.attack(self.player)
                last_attacker = self.enemy
            else:
                self.player.attack(self.enemy)
                last_attacker = self.player
        if player.health > 0:
            print('Игрок победил.')
        else:
            print('Враг победил.')


class Person_slot:
    __slots__ = ['name', 'health', 'armor', 'damage']
    def __init__(self, name, health, armor, damage):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage

    def calculate_damage(self, enemy):
        return self.damage / enemy.armor

    def attack(self, enemy):
        enemy.health -= self.calculate_damage(enemy)

player = Player('Ivan', 100, 1.0, 10)
print(player.__dict__)
print(asizeof.asizeof(player))
player2 = Person_slot('Ivan', 100, 1.0, 10)
print(asizeof.asizeof(player2))
enemy = Enemy('Ilia', 100, 1.1, 10)
game = Game(player, enemy)

game.start()

#обычный занимает 312 памяти, слот занимает 120 памяти, меньше чем обычный список,
# чуть больше в половину.