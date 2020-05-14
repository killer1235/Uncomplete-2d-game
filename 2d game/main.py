from app import app
from pygame import *
import pygame

pygame.init()

width = 800
height = 600

display = pygame.display.set_mode((width , height))

Game = app(display)
Game.run()

