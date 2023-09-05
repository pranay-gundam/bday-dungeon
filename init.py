import GameOBJs as go
import GuiOBJs as gui
import pygame as pyg
import numpy as np

pyg.init()
running = True

HomeScreen = gui.Screen(title="Home Screen")


KEYDICT = {1073741906: "up", 1073741905: "down",
           1073741904: "left", 1073741903: "right"}

Hall1 = gui.Screen(title="Hall1")
P1 = go.Player(name="Pranay", 
               hitbox=pyg.Rect(Hall1.getWidth()/2-5,
                               Hall1.getHeight()/2-5,
                               10, 10),
               hp=10,
               inven_space=10,
               x=Hall1.getWidth()/2,
               y=Hall1.getHeight()/2,
               width=10,
               height=10)
Hall1.addElement(P1)
Hall1.makeCurrentScreen()

Hall2 = gui.Screen(title="Hall2")
CheckPoint = gui.Screen(title="Check Point")
Boss1 = gui.Screen(title="Boss One")
Boss2 = gui.Screen(title="Boss Two")
FinalBoss = gui.Screen(title="Final Boss")

screens = [HomeScreen, Hall1, Hall2, 
           CheckPoint, Boss1, Boss2,
           FinalBoss]

while running:

    for e in pyg.event.get():
        if e.type == pyg.QUIT:
            running = False
        if e.type == pyg.KEYDOWN:
            if KEYDICT[e.key] == "up":
                



    for page in screens:
        page.update()




    pyg.display.update()
    

    


pyg.quit()