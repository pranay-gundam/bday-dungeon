import GameOBJs as go
import GuiOBJs as gui
import pygame as pyg
import numpy as np

def screen_initialize():
    HomeScreen = gui.Screen(title="Home Screen")

    Hall1 = gui.Screen(title="Hall1")
    P1 = go.Player(name="Pranay", 
                hitbox=pyg.Rect(Hall1.getWidth()/2-5,
                                Hall1.getHeight()/2-5,
                                10, 10),
                hp=3,
                inven_space=10,
                x=Hall1.getWidth()/2,
                y=Hall1.getHeight()/2,
                width=10,
                height=10,
                deltax=0.0,
                deltay=0.0)
    Hall1.addElement(P1)


    Hall2 = gui.Screen(title="Hall2")
    CheckPoint = gui.Screen(title="Check Point")
    Boss1 = gui.Screen(title="Boss One")
    Boss2 = gui.Screen(title="Boss Two")
    FinalBoss = gui.Screen(title="Final Boss")

    screens = {HomeScreen.getTitle(): HomeScreen, 
            Hall1.getTitle(): Hall1, 
            Hall2.getTitle(): Hall2,
            CheckPoint.getTitle(): CheckPoint, 
            Boss1.getTitle(): Boss1, 
            Boss2.getTitle(): Boss2,
            FinalBoss.getTitle(): FinalBoss}

    wrapper = gui.ScreenWrapper(screens)
    wrapper.change_cur_screen(screens[Hall1.getTitle()])

    return wrapper
