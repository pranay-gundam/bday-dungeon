import pygame as pyg
import screenInit


pyg.init()
running = True

pyg.key.set_repeat(1, 100)

wrapper = screenInit.screen_initialize()

while running:

    for e in pyg.event.get():
        if e.type == pyg.QUIT:
            running = False
        wrapper.act(e)
                
    wrapper.update()
    pyg.display.update()
    


pyg.quit()