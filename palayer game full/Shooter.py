import pygame
import random
import keyboard
import time
import json 
from time import sleep
from sys import exit
edward=1
pygame.init()
screen = pygame.display.set_mode((800, 400))
screen.fill('darkviolet')
pygame.display.set_caption("Rider")
clock = pygame.time.Clock()
pack = screen.blit


targetx = random.randrange(800)
targety = random.randrange(300) 
        #inserting all the nessisary images
small_font = pygame.font.SysFont('Times New Roman', 25)
big_font = pygame.font.SysFont('Times New Roman', 50)
Start = pygame.image.load('Graphics/Start.png').convert_alpha()
Start_rect = Start.get_rect(center=(400, 300))
title = pygame.image.load('Graphics/logo.png').convert_alpha()
title_rect = title.get_rect(center=(400, 200))
Game_Over = pygame.image.load('Graphics/GmOv.png')
target=pygame.image.load('Graphics/bullseye.png').convert_alpha()
target_rect=target.get_rect(center=(targetx, targety))   
background = pygame.image.load('Graphics/bg.png').convert_alpha()
man_left = pygame.image.load('Graphics/player/man_left.png').convert_alpha()
man_right = pygame.image.load('Graphics/player/man_right.png').convert_alpha()
man_rect = man_right.get_rect(topleft=(410, 275))

        #inserting random variables 
score = 0
score = str(score) 





while edward == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if event.type== pygame.MOUSEBUTTONDOWN:
        if title_rect.collidepoint(event.pos):
            edward = 2
            start_ticks=pygame.time.get_ticks() 
    pack(background, (0, 0)) 
    pack(Start, Start_rect)
    pack(title, title_rect)
    clock.tick(60)
    pygame.display.update()

#Main game loop
while edward == 2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
          
                    #Setting the random postion of the target
    if man_rect.colliderect(target_rect) is True:
        targetx = random.randrange(50,750)
        targety = random.randrange(10,300)   
        target_rect=target.get_rect(midbottom=(targetx, targety))
    
                    #Scoreing system
        score = int(score)
        score += 1
        score = str(score)    
    big_text = big_font.render(score, False, 'Black')
    big_text_rect = big_text.get_rect(midbottom=(400, 100))
    
    
        #Showing all surfaces 
    pack(background, (0, 0))
    pack(big_text, big_text_rect)
    pack(man_right, man_rect)
    if man_rect.colliderect(target_rect) is not True:
        pack(target,target_rect)
        
              #Gravity Function   
    def gravity():
        if man_rect.y < 275:
            man_rect.y += 20
        if  man_rect.y > 275 and not keyboard.is_pressed('s'):
            man_rect.y -=20
            
                    #All the movement keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: 
        man_rect.x -=10
    if man_rect.x > 800: man_rect.left = -100
    if man_rect.x < -100: man_rect.left = 800
    if keys[pygame.K_d]:
        man_rect.x +=10
    if keys[pygame.K_w]:
        man_rect.y -=10
    if keys[pygame.K_s]:man_rect.y +=10
    if not keys[pygame.K_w]:gravity()    
    if man_rect.y < 0: man_rect.y = 0
    if man_rect.y > 320: man_rect.y = 320

    seconds=(pygame.time.get_ticks()-start_ticks)/1000 
    if seconds>30: 
        edward = 3
        
    
    pygame.display.update()
    clock.tick(60)
    
    
    
def save_highscore():
        with open('highscores.json', 'w') as file:
            json.dump(score, file)


#End screen loop
while edward == 3:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    with open('highscores.json', 'r') as file:
        highscores = json.load(file)  
    pack(Game_Over, (0,0))
    score_rect=big_text.get_rect(center=(360,240))
    pack(big_text, score_rect)
    if highscores < score:
        save_highscore()
        print(highscores, score)
    high = big_font.render('Your highscore is '+ highscores, False, 'Red')
    high_rect = high.get_rect(center = (400, 20))
    pack(high, high_rect)
    pygame.display.update()