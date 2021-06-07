import pygame
import random

pygame.init()
screen=pygame.display.set_mode((480,640))
FPS = 30
fpsClock = pygame.time.Clock()

try:
    spaceshipimg = pygame.image.load("./img/spaceship.png")
    asteroid0 = pygame.image.load("./img/asteroid00.png")
    asteroid1 = pygame.image.load("./img/asteroid01.png")
    asteroid2 = pygame.image.load("./img/asteroid02.png")
    asteroidimgs = (asteroid0,asteroid1,asteroid2)
    gameover = pygame.image.load("./img/gameover.jpg")

    takeoffsound = pygame.mixer.Sound("./audio/takeoff.wav")
    landingsound = pygame.mixer.Sound("./audio/landing.wav")
    takeoffsound.play()

except Exception as err:
    print('그림 또는 효과음 삽입에 문제가 있습니다.:',err)
    pygame.quit()
    exit(0)

running = True
while running:
    screen.fill((255, 255, 255))

    asteroidtimer = 100

    asteroids = [[20, 0, 0]]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    screen.blit(spaceshipimg, (240,600))

    landingsound.play()

    screen.blit(asteroidimgs[0],(240,320))

    position = pygame.mouse.get_pos()
    spaceshippos = (position[0],600)
    screen.blit(spaceshipimg, spaceshippos)

    fpsClock.tick(FPS)
    pygame.display.flip()