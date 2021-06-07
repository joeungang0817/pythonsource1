##################################################
# pygame - 사운드 제어
#
# 참고 사이트
# https://pg.org
# https://pg.org/docs/
#
# space 다운로드 사이트
# http://learnsteam.co.kr/dn/space.zip
# http://learnsteam.co.kr/dn/gamesound.zip
##################################################

import pygame as pg
import sys
import time
import random

# 초기화 작업
# 반드시 주어진 함수이름과 순서를 지켜야 함.

pg.init()
screen = pg.display.set_mode((320, 600))
pg.display.set_caption("pygame 이해하기")

ship = pg.image.load("img/spaceship.png")

sound1 = pg.mixer.Sound("audio/takeoff.wav")
jump = pg.mixer.Sound("audio/match0.wav")
shoot = pg.mixer.Sound("audio/badswap.wav")
back = pg.mixer.Sound("audio/landing.wav")
jump2 = pg.mixer.Sound("audio/match1.wav")
left = pg.mixer.Sound("audio/match2.wav")
right = pg.mixer.Sound("audio/match3.wav")
sounddis = pg.mixer.Sound("audio/match4.wav")
sounddis2 = pg.mixer.Sound("audio/match5.wav")

pos_x = 160
pos_y = 550
SHIP_LEFT = -5
SHIP_RIGHT = 5
SHIP_STOP = 0
direction = SHIP_LEFT
running = True

sound1.play()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            key_event = pg.key.get_pressed()
            if key_event[pg.K_LEFT]:
                direction = SHIP_LEFT
                left.play()
            elif key_event[pg.K_RIGHT]:
                direction = SHIP_RIGHT
                right.play()
            elif key_event[pg.K_UP]:
                direction = SHIP_STOP
                shoot.play()
            elif key_event[pg.K_SPACE]:
                jump.play()
            elif key_event[pg.K_DOWN]:
                direction = SHIP_STOP
                back.play()
            elif key_event[pg.K_w]:
                jump2.play()
        if event.type == pg.MOUSEBUTTONDOWN:
            sounddisplay = random.randint(1,2)
            if sounddisplay == 1:
                sounddis.play()
            elif sounddisplay == 2:
                sounddis2.play()
    pos_x += direction
    print(pos_x)
    screen.fill((255, 255, 255))
    screen.blit(ship, (pos_x, pos_y))
    pg.display.update()

    time.sleep(0.05)

print('메인루프 종료')
pg.quit()