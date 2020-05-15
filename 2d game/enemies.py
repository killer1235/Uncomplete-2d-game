import pygame
from pygame import *
from projectiles import Projectiles

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

    def Spawn(self  ):
        self.win.blit(Enem_sprite , (self.x, self.y))
        self.hitbox = (self.x , self.y , self.w , self.h)

    def move(self):
        self.y += self.speed

    def get_hitbox(self):
        return self.hitbox

    def fire(self , win  ,bullets = []  ):
    
        if len(bullets) < 4:  # This will make sure we cannot exceed 3 bullets on the screen at once
            bullets.append(Projectiles(round(self.x+self.w/2),( self.y  ) ,win , 5))    

