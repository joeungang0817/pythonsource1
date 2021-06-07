import pygame
import random

pygame.init()
screen=pygame.display.set_mode((480,640))

running = True
while running:
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)

    pygame.display.flip()

while 1:
    for event in pyagame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)