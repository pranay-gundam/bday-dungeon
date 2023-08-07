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
        self.items = {"head":[], "chest":[], "l_arm":[], "r_arm":[], "pants":[], "boots":[], "inventory":[]}

        # The number of slots that a character is able to hold
        self.inven_space = inven_space

    def item_check(self, slot):
        match slot:
            case "head":
                return len(self.items["head"]) == 0
            case "chest":
                return len(self.items["chest"]) == 0
            case "l_arm":
                return len(self.items["l_arm"]) == 0
            case "r_arm":
                return len(self.items["r_arm"]) == 0
            case "pants":
                return len(self.items["pants"]) == 0
            case "boots":
                return len(self.items["boots"]) == 0
            case "inventory":
                return len(self.items["inventory"]) <= self.inven_space

    def add_item(self, item, slot):
        if self.item_check(slot):
            self.item_check[slot].append(item)
        else:
            print(f"{slot} slot is full")



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
        hitbox = {"l":50,"w": 50}
        super().__init__(name, hp, hitbox)


class Melee_Enemy(Enemy):
    def __init__(self, name):
        hp = 20
        hitbox = {"l": 20,"w": 10}
        super().__init__(name, hp)


class Ranged_Enemy(Enemy):
    def __init__(self, name):
        hp = 10
        hitbox = {"l": 20,"w": 10}
        super().__init__(name, hp)
