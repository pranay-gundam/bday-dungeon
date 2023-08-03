#

class Room:
    def __init__(self, name):
        self.name = name


class Character:
    def __init__(self, name, hitbox, hp, inven_space):
        self.name = name

        # hit points
        self.hp = hp

        # dictionary of the length and width of the rectangular hitbox
        self.hitbox = hitbox

        # Any equipable that a character can use
        self.items = {"head":, "chest":, "l_arm":, "r_arm":, "pants":, "boots":, "inventory":[]}

        # The number of slots that a character is able to hold
        self.inven_space = inven_space

    def inventory_check(self):
        return len(self.items["inventory"]) <= self.inven_space

    def add_item(self, item, slot):
        match slot:
            case "head":
                pass
            case "chest":
                pass
            case "l_arm":
                pass
            case "r_arm":
                pass
            case "pants":
                pass
            case "boots":
                pass
            case "inventory":
                pass



class Player:
    def __init__(self, name):
        self.name = name


class NPC(Character):
    def __init__(self, name, hp, hitbox):
        super().__init__(name, hp, hitbox)

class Enemy(NPC):
    def __init__(self, name, hp, hitbox):
        super().__init__(name, hp, hitbox)

class Boss_Enemy(Enemy):
    def __init__(self, name):
        hp = 100
        hitbox = {l:50, w:50}
        super().__init__(name, hp, hitbox)


class Melee_Enemy(Enemy):
    def __init__(self, name):
        hp = 20
        hitbox = {l: 20, 10}
        super().__init__(name, hp)


class Ranged_Enemy(Enemy):
    def __init__(self, name):
        hp = 10
        hitbox = {l: 20, 10}
        super().__init__(name, hp)
