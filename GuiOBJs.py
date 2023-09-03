import GameOBJs as go
import pygame as pyg



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
 
    def addElement(self, elem):
        self.elements.append(elem)

    # DISPLAY THE CURRENT SCREEN OF
    # A WINDOW AT THE CURRENT STATE
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
            elem.draw()
 
    # THIS WILL SET THE STATE OF A CURRENT STATE TO OFF
    def endCurrentScreen(self):
        self.CurrentState = False
 
    # RETURNS THE TITLE OF THE SCREEN
    def returnTitle(self):
        return self.title



class ElemGroup:
    pass