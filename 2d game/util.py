from pygame import *
import pygame
from time import sleep


width = 800
height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
carh = 82
carw = 73

colors = [black , red , green]


def CreateText(txt , font ,  Color):
    TextSurf = font.render(txt , True ,Color)  

    return TextSurf , TextSurf.get_rect()

def message_display(msg , x , y  ,s, color , display):
    largeText = pygame.font.Font('freesansbold.ttf', s)
    TextSurf, TextRect = CreateText(msg, largeText , color)
    TextRect.center = (x, y)
    display.blit(TextSurf, TextRect)
    pygame.display.update(TextRect)

def draw_healthbar(display ,  x, y , w , h):
    if w < 50:
        pygame.draw.rect(display , red ,[x , y , w , h])
    else:
        pygame.draw.rect(display , green ,[x , y , w , h])

def show_fps(clock , win):
    message_display(f'FPS : {str(int(clock.get_fps()))}' , 50 , 90 , 25 , white , win)   

     