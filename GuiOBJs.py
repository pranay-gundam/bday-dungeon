import GameOBJs as go
import pygame as pyg


class ScreenWrapper:
    def __init__(self, screens = {}):
        self.screens = screens
        self.cur_screen = None
    
    def change_cur_screen(self, new_screen):
        if self.cur_screen != None:
            self.cur_screen.endCurrentScreen()
            #self.screens[self.cur_screen.getTitle()] = self.cur_screen
            self.cur_screen = new_screen
            self.cur_screen.makeCurrentScreen()
        else:
            self.cur_screen = new_screen
            self.cur_screen.makeCurrentScreen()

    def update(self):
        self.cur_screen.update()


    def add_screen(self, screen, make_cur_screen = False):
        if not screen.getTitle() in self.screens.keys:
            self.screens[screen.getTitle()] = screen
        else:
            raise Exception("you are trying to add a screen that already exists")
        if make_cur_screen:
            self.change_cur_screen(screen)

    def act(self, e):
        self.cur_screen.act(e)

class Screen:
    def __init__(self, title, width=1200, height=600,
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

    def getTitle(self):
        return self.title

    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width

    def addElement(self, elem):
        self.elements.append(elem)

    def makeCurrentScreen(self):
        
        pyg.display.set_caption(self.title)
        
        self.CurrentState = True
        
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

    def act(self, e):
        for elem in self.elements:
            elem.act(e)

    def endCurrentScreen(self):
        self.CurrentState = False
 
    def returnTitle(self):
        return self.title



class ElemGroup:
    pass