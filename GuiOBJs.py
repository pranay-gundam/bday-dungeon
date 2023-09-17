import GameOBJs as go
import pygame as pyg

KEYDICT = {1073741906: "up", 1073741905: "down",
           1073741904: "left", 1073741903: "right"}

class ScreenWrapper:
    def __init__(self, screens = {}):
        self.screens = screens
    
    def add_screen(self, screen, screen_name):
        if not screen_name in self.screens.keys:
            self.screens[screen_name] = screen

    def act(self, e):
        if e.type == pyg.KEYDOWN:
            if KEYDICT[e.key] == "up":
                pass
            if KEYDICT[e.key] == "down":
                pass
            if KEYDICT[e.key] == "left":
                pass
            if KEYDICT[e.key] == "right":
                pass
        if e.type == pyg.KEYUP:
            if KEYDICT[e.key] == "up":
                pass
            if KEYDICT[e.key] == "down":
                pass
            if KEYDICT[e.key] == "left":
                pass
            if KEYDICT[e.key] == "right":
                pass

class Screen:
    def __init__(self, title, width=1250, height=625,
                 screenColor=(189, 154, 154)):
        # HEIGHT OF A WINDOW
        self.height = height
        # TITLE OF A WINDOW
        self.title = title
        # WIDTH OF A WINDOW
        self.width = width
        # COLOUR CODE
        self.screenColor = screenColor
        # CURRENT STATE OF A SCREEN
        self.CurrentState = False
        # ARRAY CONTAINING ALL THE ELEMENTS ON THE SCREEN
        self.elements = []
 
    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width

    def addElement(self, elem):
        self.elements.append(elem)

    def makeCurrentScreen(self):
        # SET THE TITLE FOR THE CURRENT STATE OF A SCREEN
        pyg.display.set_caption(self.title)
        # SET THE STATE TO ACTIVE
        self.CurrentState = True
        # ACTIVE SCREEN SIZE
        self.screen = pyg.display.set_mode((self.width,
                                           self.height))
        self.screen.fill(self.screenColor)

        for elem in self.elements:
            elem.draw(self.screen)
 
    def update(self):
        self.screen.fill(self.screenColor)
        for elem in self.elements:
            elem.update()
            elem.draw(self.screen)

        

    def endCurrentScreen(self):
        self.CurrentState = False
 
    def returnTitle(self):
        return self.title



class ElemGroup:
    pass