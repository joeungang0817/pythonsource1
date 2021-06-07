import pygame
import random
import time

pygame.init()
screen=pygame.display.set_mode((480, 640))

score=0
FPS = 50
fpsClock = pygame.time.Clock()
asteroidtimer = 100

asteroids = [[20,0,0]]
####################################################################################

def text(arg, x, y):
    font = pygame.font.Font(None, 24)
    text = font.render("Score: " +str(arg).zfill(6), True, (0,0,0))
    textRect = text.get_rect()
    textRect.centerx = x
    textRect.centery = y
    screen.blit(text, textRect)

#####################################################################################
try:
    spaceshipimg = pygame.image.load("./img/spaceship.png")
    asteroid0 = pygame.image.load("./img/asteroid00.png")
    asteroid1 = pygame.image.load("./img/asteroid01.png")
    asteroid2 = pygame.image.load("./img/asteroid02.png")
    asteroidimgs = (asteroid0, asteroid1, asteroid2)
    gameover = pygame.image.load("./img/gameover.jpg")
    gameintro = pygame.image.load("./img/game.png")

    takeoffsound = pygame.mixer.Sound("./audio/takeoff.wav")
    landingsound = pygame.mixer.Sound("./audio/landing.wav")
    takeoffsound.play()
except Exception as err:
    print('그림또는 효과음 삽입에 문제가 있습니다.')
    pygame.quit()
    exit(0)

running = True

##########################################################################################
screen.blit(gameintro,(0,0))
pygame.display.flip()
time.sleep(1)
takeoffsound.play()
direct=0
#########################################################################################
while running:
    screen.fill((255, 255, 255))

    score +=1
    text(score,400,10)
    if score%100 == 0:
        FPS+=3

    position = pygame.mouse.get_pos()

    spaceshiprect = pygame.Rect(spaceshipimg.get_rect())
    spaceshiprect.left = spaceshippos[0]
    spaceshiprect.top = spaceshippos[1]

    asteroidtimer -= 10
    if asteroidtimer <= 0:
        asteroids.append([random.randint(5,475), 0, random.randint(0, 2)])
        asteroidtimer = random.randint(50,200)
    index = 0
    for stone in asteroids:
        stone[1] += 10

        if stone[1] > 640:
            asteroids.pop(index)
        stonerect = pygame.Rect(asteroidimgs[stone[2]].get_rect())
        stonerect.left = stone[0]
        stonerect.top = stone[1]
        if stonerect.colliderect(spaceshiprect):
            landingsound.play()
            asteroids.pop(index)
            running = False

        screen.blit(asteroidimgs[stone[2]], (stone[0], stone[1]))
        index += 1

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)


    landingsound.play()


    fpsClock.tick(FPS)
    pygame.display.flip()

#####################################################################################

screen.blit(gameover,(0,0))
pygame.display.flip()

######################################################################################

print(score)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.flip()