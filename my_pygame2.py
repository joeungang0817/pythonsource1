import pygame
import random

pygame.init()
screen=pygame.display.set_mode((480,640))

running = True
FPS = 30
fpsClock = pygame.time.Clock()

while running:
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
    fpsClock.tick(FPS)
    pygame.display.flip()

