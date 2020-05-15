import pygame
from time import sleep
import random
import time as tm
from pygame import *
from util import *
from player import Player
from enemies import Enemies
from projectiles import Projectiles

background = pygame.image.load('bg.png')

# firing function
def fire(win ,man ,bullets = []  ):

  if len(bullets) < 4:  # This will make sure we cannot exceed 3 bullets on the screen at once
        bullets.append(Projectiles(round(man.x+man.w/2),( man.y  ) ,win , 5))


# App class
class app:
    def __init__(self , displayd):
        self.isRunning = True
        self.window = displayd
        
        self.run()


    def run(self):
        # Game clock
        clock = pygame.time.Clock()

        # enemy Spawner
        Enems_pos = [50 , 200,350,500,650,750]

        Enem = []

        for i in range(5):
            Enem.append( Enemies(Enems_pos[i] , -100 , 1 , self.window))

        # Player variable
        player = Player(self.window , (width * 0.5) , (height * 0.5)  )

        # Game loop 
        isRunning = True

        # Player Score
        dodged = 0
        
        # player health
        health = 100

        # Bullets list
        bullets = []
        enem_bullets = []

        time0 = tm.time()

        # main game loop
        while isRunning:

            # Check if bullet is out of bounds
            for bullet in bullets:

                if bullet.y < -100:
                    bullets.pop(bullets.index(bullet))

                else :
                    bullet.y -= bullet.vel

            for bullet in enem_bullets:
    
                if bullet.y < -100:
                    bullets.pop(bullets.index(bullet))

                else :
                    bullet.y += bullet.vel               

            # Game events starts here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isRunning = False
                    self.app_quit()

                # key is pressed
                if event.type == pygame.KEYDOWN:
                    # move left
                    if event.key == pygame.K_LEFT:
                        player.acclerate(-5)    

                    # move right    
                    elif event.key == pygame.K_RIGHT:
                        player.acclerate(5)

                    # move up    
                    elif event.key == pygame.K_UP:
                        player.acclerate(0,-5) 

                    # move down    
                    elif event.key == pygame.K_DOWN:
                        player.acclerate(0,5)

                     # fire bullets   
                    elif event.key == pygame.K_SPACE:
                        fire(self.window , player , bullets)   

                # key is released                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player.acclerate(0 , 0) 

            # Game Events ends here                     

            # fill the screen with white color
            #self.window.fill(white)
            self.window.blit(background , (0,0))


            # Draw the player
            player.draw()


            for bullet in enem_bullets:
                bullet.draw()
            
            # Draw bullets
            for bullet in bullets:
                bullet.draw()

            # Spawn The enemeis
            for i in Enem:
                i.Spawn()
                i.move()

                if tm.time() - time0 > 1:  # Shoot once every 10 seconds
                    time0 = tm.time()
                    #fire(self.window ,i , enem_bullets )
                    i.fire(self.window , enem_bullets)
                
            # Move players and enemies    
            player.move()

            # Show fps
            show_fps(clock , self.window)
            message_display(f"dodged: {dodged}" , 70 , 15 ,25, white , self.window)

            hitbox = player.get_hitbox()

            draw_healthbar(self.window , player.x,(hitbox[1] + hitbox[3])+15 , health , 10)

            # check if player is out of bounds
            if player.x > width -  carw or player.x < 0:
                self.Crash()

            # bullet collision   
            for enemy in Enem:     
                z = 0
                z =+ 1
                if enemy.y > height:
                    enemy.y = 0 - enemy.y
                    enemy.x = Enems_pos[z]
                    dodged += 1        
                
                # enemy hitbox
                enem_hitbox = enemy.get_hitbox()

                
                collsion = self.detect_collisions(hitbox , enem_hitbox)

                # player collsion 
                if collsion:
                    # check if player health is Zero or below
                    if health <= 0:
                        self.Crash()
                    else:

                        enemy.y = 0 - enemy.h
                        enemy.x = random.randrange(0  , width)
                        health -= 10            
                
                for bullet in bullets:
                    
                    bullet_hitbox = bullet.get_hitbox()

                # collision detection function
                    collsion_bullet = self.detect_collisions(bullet_hitbox ,  enem_hitbox )
                    pl_col = self.detect_collisions(hitbox , bullet_hitbox)

                
                    if collsion_bullet:

                     # reset enemy position
                        enemy.y = 0 - enemy.h
                        enemy.x = random.randrange(0  , width)
                        bullets.pop(bullets.index(bullet))                
            

            pygame.display.update()
            clock.tick()

    def app_quit(self):
        pygame.quit()
        quit()

    def Draw(self,obj  ,x ,y):
        self.window.blit(obj , (x ,y))

    def Crash(self):
        message_display("crashed" , (width/2) , (height/2)  ,115, white , self.window)

        pygame.display.update()

        sleep(1)
        self.run()

    def detect_collisions(self , obj1 , obj2):

        # check collision 
        if obj1[0] < obj2[0] + obj2[2] and obj1[0] + obj1[2] > obj2[0] and obj1[1] < obj2[1] + obj2[3] and obj1[1] + obj1[3] > obj2[1]:
            return True
        else:
            return False      

