import pygame as pyg
import numpy as np

TIME_DELAY = 500 # 0.5 seconds
TIMER_EVENT = pyg.USEREVENT + 1
pyg.time.set_timer(TIMER_EVENT, TIME_DELAY )

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
        if slot == "head":
                return self.head == None
        elif slot == "chest":
                return self.chest == None
        elif slot == "l_arm":
                return self.left_arm == None
        elif slot == "r_arm":
                return self.right_arm == None
        elif slot == "pants":
                return self.pants == None
        elif slot == "boots":
                return self.boots == None
        elif slot == "pack":
                return len(self.pack) <= self.inven_space

    def add_item(self, item , slot):
        if self.inven_check(slot) and item.slot_check(slot):
            if slot == "head":
                self.head = item
            elif slot == "chest":
                self.chest = item
            elif slot == "l_arm":
                self.left_arm = item
            elif slot == "r_arm":
                self.right_arm = item
            elif slot == "pants":
                self.pants = item
            elif slot == "boots":
                self.boots = item
            elif slot == "pack":
                self.pack.append(item)
        else:
            print(f"either {slot} slot is full or this is not the right slot for this item")


class Character:
    def __init__(self, name, hitbox, hp, inven_space, x, y, width, height, animedict, deltax=0, deltay=0):
        self.name = name

        # hit points
        self.hp = hp

        # pygame rect object to track the hitbox
        self.hitbox = hitbox

        # Any equipable that a character can use
        self.inventory = Inventory(inven_space)

        # Keeping track of interaction of character with front end
        self.pos = np.array([x,y])
        self.size = np.array([width,height])

        # Helps with controlling movement of the character
        self.velocity = np.array([deltax, deltay])

        self.anime_dict = animedict

    def add_item(self, item, slot):
        if self.inven_check(slot) and item.slot_check(slot):
            self.inven_check[slot].append(item)
        else:
            print(f"either {slot} slot is full or this is not the right slot for this item")


    def update(self):
        self.pos += self.velocity
        

    def draw(self, screen):
        pyg.draw.circle(surface=screen, 
                        color="black", 
                        center=self.pos, 
                        radius=self.size[0])

    def act(self, e):
        if e.type == pyg.KEYDOWN:
            if e.key == pyg.K_UP:
                self.velocity += np.array([0, -0.1])
            if e.key == pyg.K_DOWN:
                self.velocity += np.array([0, 0.1])
            if e.key == pyg.K_LEFT:
                self.velocity += np.array([-0.1, 0])
            if e.key == pyg.K_RIGHT:
                self.velocity += np.array([0.1, 0])
        if e.type == pyg.KEYUP:
            if e.key == pyg.K_UP:
                self.velocity[1] = 0.0
            if e.key == pyg.K_DOWN:
                self.velocity[1] = 0.0
            if e.key == pyg.K_LEFT:
                self.velocity[0] = 0.0
            if e.key == pyg.K_RIGHT:
                self.velocity[0] = 0.0
        
class Player(Character):
    def __init__(self, name, hitbox, hp, inven_space, x, y, width, height, deltax=0, deltay=0):
        super().__init__(name, hitbox, hp, inven_space, x, y, width, height, deltax, deltay)

    def update(self):
        super().update()

    def add_item(self, item, slot):
        super().add_item(item, slot)

    def draw(self, screen):
        super().draw(screen)

    def act(self, e):
        if e.type == pyg.KEYDOWN:
            if e.key == pyg.K_UP:
                self.velocity += np.array([0, -0.1])
            if e.key == pyg.K_DOWN:
                self.velocity += np.array([0, 0.1])
            if e.key == pyg.K_LEFT:
                self.velocity += np.array([-0.1, 0])
            if e.key == pyg.K_RIGHT:
                self.velocity += np.array([0.1, 0])
        if e.type == pyg.KEYUP:
            if e.key == pyg.K_UP:
                self.velocity[1] = 0.0
            if e.key == pyg.K_DOWN:
                self.velocity[1] = 0.0
            if e.key == pyg.K_LEFT:
                self.velocity[0] = 0.0
            if e.key == pyg.K_RIGHT:
                self.velocity[0] = 0.0

    


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
        super().__init__(name=name, hitbox=hitbox, hp=hp)


class Melee_Enemy(Enemy):
    def __init__(self, name, animedict):
        hp = 20
        hitbox = {"l": 20,"w": 10}
        super().__init__(name=name, hitbox=hitbox, hp=hp, animedict=animedict)

        self.drawtimer = 0

    def update(self):
        super().update()

    def act(self, e):
        if e.type == TIMER_EVENT:
            self.drawtimer += 1

        if (self.drawtimer // 10) % 4 == 0:
            pass
        elif (self.drawtimer // 10) % 4 == 1:
            pass
        elif (self.drawtimer // 10) % 4 == 2:
            pass
        elif (self.drawtimer // 10) % 4 == 3:
            pass

    def draw(self, screen):
        if np.all(self.velocity):
            pass
        else:
            pass
        

    

class Ranged_Enemy(Enemy):
    def __init__(self, name):
        hp = 10
        hitbox = {"l": 20,"w": 10}
        super().__init__(name, hp)


class SkeletonV1(Melee_Enemy):
    def __init__(self, name):

        idle_anime = [pyg.image.load("Sprite-Bank/skeletonV1/skeleton_v1_1.png"),
                      pyg.image.load("Sprite-Bank/skeletonV1/skeleton_v1_2.png"),
                      pyg.image.load("Sprite-Bank/skeletonV1/skeleton_v1_3.png"),
                      pyg.image.load("Sprite-Bank/skeletonV1/skeleton_v1_4.png")]
        moving_anime = []
        attack_anime = []

        animedict = {"idle": idle_anime,
                     "moving": moving_anime,
                     "attack": attack_anime}

        super().__init__(name, animedict)