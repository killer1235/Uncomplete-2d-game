import pygame
from time import sleep
import random
from pygame import *

pygame.init()

width = 800
height = 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
carh = 82

display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

body = pygame.image.load('Body.png')

def DrawRect(rectx , recty , rectw , recth):
    pygame.draw.rect(display , black ,[rectx , recty , rectw , recth] )


def Draw(obj, x, y):
    display.blit(obj, (x, y))


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    display.blit(text,(0,0))

def CreateText(text, font):
    TextSurf = font.render(text, True, black)
    return TextSurf,  TextSurf.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = CreateText(text, largeText)
    TextRect.center = ((width/2), (height/2))
    display.blit(TextSurf, TextRect)

    pygame.display.update()

    sleep(1)

    GameLoop()


def crash():
    message_display('You Crashed')


car_width = 73

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(white)

        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = CreateText("A bit Racey", largeText)
        TextRect.center = ((width/2),(height/2))
        display.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        button("GO!",150,450,100,50,green,bright_green,GameLoop)

        pygame.draw.rect(display, red,(550,450,100,50))

        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(display, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(display, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = CreateText(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    display.blit(textSurf, textRect)

def GameLoop():
    x = (width * 0.5)
    y = (height * 0.5)

    x_change = 0

    running = True
    thing_startx = random.randrange(0, width)
    thing_starty = 0
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    dodged = 0
    body_rect = pygame.Rect(x , y , car_width ,  carh)

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0
        
        display.fill((255, 255, 255))

        DrawRect(thing_startx , thing_starty , thing_width ,  thing_height)
        thing_starty += thing_speed
        x += x_change
        things_dodged(dodged)

        Draw(body, x, y)                


        if x > width - car_width or x < 0:
            crash()

        if thing_starty > height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,width)
            dodged += 1

        objectrect = pygame.Rect(thing_startx , thing_starty , thing_width , thing_height)

        if body_rect.colliderect(objectrect):
            crash()
        '''
        if y < thing_starty + thing_height:
            print(f'y is {y} ,  thing_starty : {thing_starty}')

            if (x > thing_startx and x < thing_startx + thing_width )  or (x+car_width > thing_startx and x + car_width < thing_startx+thing_width):
                print(f'x is {x} , thingx is {thing_startx}')
                crash()  '''

        pygame.display.update()
        clock.tick(60)

game_intro()     
GameLoop()
pygame.quit()
quit()