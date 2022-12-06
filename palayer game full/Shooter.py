import pygame
import random
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 400))
screen.fill('darkviolet')
pygame.display.set_caption("Rider")
clock = pygame.time.Clock()
pack = screen.blit

x_random= random.randint(0, 800)
y_random= random.randint(0, 300)
target=pygame.image.load('Graphics/bullseye.png')
sky_surface = pygame.image.load('Graphics/sky.png').convert_alpha()
ground_surface = pygame.image.load(
    'Graphics/Ground.png').convert_alpha()
cloud_surface = pygame.image.load(
    'Graphics/cloud.png').convert_alpha()
man_left = pygame.image.load(
    'Graphics/player/man_left.png').convert_alpha()
man_right = pygame.image.load(
    'Graphics/player/man_right.png').convert_alpha()
man_rect = man_right.get_rect(topleft=(410, 275))
bullet_surface = pygame.image.load(
    'Graphics/player/bullet.png').convert_alpha()
bullet_rect = bullet_surface.get_rect(midbottom=(10, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    target_rect= target.get_rect(center=(x_random, y_random))
    pack(target,target_rect)
    pack(sky_surface, (0, 0))
    pack(ground_surface, (0, 300))
    pack(ground_surface, (100, 300))
    pack(cloud_surface, (100, 100))
    pack(cloud_surface, (700, 10))
    pack(man_right, man_rect)
    bullet_rect = man_rect        
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: 
        man_rect.x -=5
    if man_rect.x > 800: man_rect.left = -100
    if man_rect.x < -100: man_rect.left = 800
    if keys[pygame.K_d]:
        man_rect.x +=5
    if keys[pygame.K_w]:
        man_rect.y -=10
    else:man_rect.y = 275
    
    if man_rect.y < -100: man_rect.y = 500
    pygame.display.update()
    clock.tick(60)
