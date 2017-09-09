# self - the same as 'this' in java, reference to itself; represents the instance of the object itself
# __init__() - is a rough representation of construvtor in Python


import pygame
from pygame.locals import *

# class GameWindow has many methods
class GameWindow:
    # __init__(self) --executed as the constructor of the class
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640,400

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size,pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False: # if self.on_init() does not execute properly then it returns False
            self._running = False
 
        while( self._running ): # look above - if self.on_init() returns False, then self._running is False either and the while loop can't start
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    game = GameWindow() #here goes __init__(self) constructor of GameWindow()
    game.on_execute() #here goes method that executes all other initialising methods of the class
