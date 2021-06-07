import pygame
import random
pygame.init()
screen = pygame,display,set_mode((480.640))

FPS = 30
fpsClock = pygame.time.Clock()
asteroidtimer = 100

asteroids=[[20,0,0]]