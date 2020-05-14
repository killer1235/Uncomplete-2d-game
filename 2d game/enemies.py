import pygame
from pygame import *

Enem_sprite = pygame.image.load('Enemy.png')

enem_w = 115
enem_h = 140

class Enemies:
    def __init__(self , x , y ,spd, disp):
        self.x = x
        self.y = y
        self.h = enem_h
        self.w = enem_w
        self.win =  disp
        self.speed = spd
        self.not_removed = False
        self.hitbox = (self.x , self.y , self.w , self.h)

    def Spawn(self  , rect_color):
        #pygame.draw.rect(self.win , rect_color ,[self.x , self.y , self.w , self.h] )
        self.win.blit(Enem_sprite , (self.x, self.y))
        self.hitbox = (self.x , self.y , self.w , self.h)

    def move(self):
        self.y += self.speed

    def get_hitbox(self):
        return self.hitbox

