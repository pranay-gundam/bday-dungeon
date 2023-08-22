class Item:
    def __init__(self, name, slot, hp, ap, weapon_type = None, ispace = None):
        self.name = name
        self.slot = slot

        # Hit Points
        self.hp = hp


        # Attack Power
        self.ap = ap

        # For weapons there are both ranged and melee types
        self.weapon_type = weapon_type

        # How much space this item takes up in an inventory pack
        self.ispace = ispace


    def slot_check(self, slot):
        return slot == self.slot

    def check_hp(self):
        return self.hp


class Room:
    def __init__(self, name):
        self.name = name

class Inventory:
    def __init__(self, inven_space):
        self.head = None
        self.chest = None
        self.left_arm = None
        self.right_arm = None
        self.pants = None
        self.boots = None
        self.pack = []

        # The number of slots that a character is able to hold
        self.inven_space = inven_space

    def inven_check(self, slot):
        match slot:
            case "head":
                return self.head == None
            case "chest":
                return self.chest == None
            case "l_arm":
                return self.left_arm == None
            case "r_arm":
                return self.right_arm == None
            case "pants":
                return self.pants == None
            case "boots":
                return self.boots == None
            case "pack":
                return len(self.pack) <= self.inven_space

    def add_item(self, item , slot):
        if self.inven_check(slot) and item.slot_check(slot):
            match slot:
            case "head":
                self.head = item
            case "chest":
                self.chest = item
            case "l_arm":
                self.left_arm = item
            case "r_arm":
                self.right_arm = item
            case "pants":
                self.pants = item
            case "boots":
                self.boots = item
            case "pack":
                self.pack.append(item)
        else:
            print(f"either {slot} slot is full or this is not the right slot for this item")


class Character:
    def __init__(self, name, hitbox, hp, inven_space):
        self.name = name

        # hit points
        self.hp = hp

        # dictionary of the length and width of the rectangular hitbox
        self.hitbox = hitbox

        # Any equipable that a character can use
        self.inventory = Inventory(inven_space)


    def add_item(self, item, slot):
        if self.inven_check(slot) and item.slot_check(slot):
            self.inven_check[slot].append(item)
        else:
            print(f"either {slot} slot is full or this is not the right slot for this item")



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
