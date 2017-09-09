import pygame
from pygame.locals import *

class Application:
   def on_execute(self):
      print("hello")

if __name__ == "__main__":
   application = Application()
   application.on_execute()