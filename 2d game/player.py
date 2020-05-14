import pygame
from pygame import *

body = pygame.image.load('Body.png')

carh = 115
carw = 100

class Player():
    def __init__(self , display  , x , y ):
        self.win = display
        self._x = x
        self._y = y
        self.w = carw
        self.h = carh
        self._health = 100
        self.accx = 0
        self.accy = 0
        self.hitbox = (self._x , self._y , carw , carh)

    def move(self ):
        self._x += self.accx
        self._y += self.accy


    def acclerate(self , x=0 , y=0): 
        self.accx = x
        self.accy = y

    def draw(self ):
        self.win.blit(body , (self._x , self._y))
        self.hitbox = (self._x , self._y , carw , carh)
        
    @property
    def x(self):
        return self._x
    @property
    def y(self ):
        return self._y 

    @property
    def health(self):
        return self._health  

    @x.setter
    def x(self, value):
        self._x = value  

    @y.setter
    def y(self , value):
        self._y = value  

    @health.setter
    def health(self , value):
        self._health = value    

    def get_hitbox(self):
        return self.hitbox   




