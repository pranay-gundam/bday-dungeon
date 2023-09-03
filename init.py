import GameOBJs as go
import GuiOBJs as gui
import pygame as pyg
import numpy as np

pyg.init()
running = True

HomeScreen = gui.Screen(title="Home Screen")
#HomeScreen.makeCurrentScreen()

Hall1 = gui.Screen(title="Hall1")
Hall1.makeCurrentScreen()


P1 = go.Player(name="Pranay")
Hall1.addElement()


Hall2 = gui.Screen(title="Hall2")
CheckPoint = gui.Screen(title="Check Point")
Boss1 = gui.Screen(title="Boss One")
Boss2 = gui.Screen(title="Boss Two")
FinalBoss = gui.Screen(title="Final Boss")


while running:

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    pyg.display.update()
    

    


pyg.quit()