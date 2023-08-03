#

class Room:
    def __init__(self, name):
        self.name = name


class Player:
    def __init__(self, name):
        self.name = name


class NPC:
    def __init__(self, name):
        self.name = name

class Enemy(NPC):
    def __init__(self, name, hp):
        super().__init__(name)
        self.hp = hp
        self.hitbox = {}



class Melee_Enemy(Enemy):
    def __init__(self, name):
        hp = 20
        super().__init__(name, hp)