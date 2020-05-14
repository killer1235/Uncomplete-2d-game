import pygame

body = pygame.image.load('missile.png')

class Projectiles():
    def __init__(self ,  x, y  ,display  , vel):
        self._x = x
        self._y = y
        self.w = 32
        self.h = 92
        self.win = display
        self.vel = vel
        self.hitbox = (self.x , self.y , self.w , self.h)

    def draw(self):
        self.win.blit(body ,(self._x , self._y))
        self.hitbox = (self.x , self.y , self.w , self.h)


    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y  

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    def get_hitbox(self):
        return self.hitbox    