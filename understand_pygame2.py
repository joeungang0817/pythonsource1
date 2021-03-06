##################################################
# pygame - 혹성 출현
#
# 참고 사이트
# https://pg.org
# https://pg.org/docs/
#
# space 다운로드 사이트
# http://learnsteam.co.kr/dn/space.zip
# http://learnsteam.co.kr/dn/gamesound.zip
##################################################
import random

import pygame as pg
import sys
import time

# 초기화 작업
# 반드시 주어진 함수이름과 순서를 지켜야 함.

WIDHT = 450
HEIGHT = 600
pg.init()
screen = pg.display.set_mode((WIDHT, HEIGHT))
pg.display.set_caption("pygame 이해하기")

ship = pg.image.load("img/spaceship.png")
asteroid = pg.image.load("img/asteroid00.png")
asteroid2= pg.image.load("img/asteroid01.png")
asteroid3= pg.image.load("img/asteroid02.png")
sound1 = pg.mixer.Sound("audio/takeoff.wav")
jump = pg.mixer.Sound("audio/match0.wav")
over = pg.image.load("img/gameover.jpg")

# 리스트를 활용하여 혹성을 여러 개 만들도록 한다.
# 혹성의 좌표를 리스트 안에 아이템에서 자체적으로 관리하도록 한다.
enemy_list = []
enemy2_list = []
enemy3_list = []
for _ in range(5):
    enemy_list.append( [asteroid, random.randint(10, WIDHT-10), random.randint(-100, HEIGHT-200)] )
for _ in range(5):
    enemy2_list.append([asteroid2, random.randint(10, WIDHT-10), random.randint(-50, HEIGHT-250)])
for _ in range(5):
    enemy3_list.append([asteroid3, random.randint(10, WIDHT-10), random.randint(-50, HEIGHT-250)])

pos_x = 160
pos_y = 550
SHIP_LEFT = -5
SHIP_RIGHT = 5
SHIP_STOP = 0
direction = SHIP_LEFT
running = True
running2= True

sound1.play()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            key_event = pg.key.get_pressed()
            if key_event[pg.K_SPACE]:
                jump.play()
        if event.type == pg.MOUSEMOTION:
            pos = pg.mouse.get_pos()
            direction=pos[0]

    pos_x = direction

    # 화면 전체 지우기
    screen.fill((255, 255, 255))

    # 혹성 그리기
    for x in enemy_list:
        x[2] += 10
        if( x[2] > HEIGHT):
            x[2] = 0
            x[1] = random.randint(10, WIDHT - 10)

        screen.blit(x[0], (x[1], x[2]))
    for x in enemy2_list:
        x[2] += 10
        if( x[2] > HEIGHT):
            x[2] = 0
            x[1] = random.randint(10, WIDHT - 10)

        screen.blit(x[0], (x[1], x[2]))
    for x in enemy3_list:
        x[2] += 10
        if( x[2] > HEIGHT):
            x[2] = 0
            x[1] = random.randint(10, WIDHT-10)
        if(x[2]>HEIGHT-80):
            if(x[1]<pos_x<x[1]+20):
                running=False
            elif(pos_x==x[1]+20):
                running=False
            elif(pos_x+20==x[1]):
                running=False

        screen.blit(x[0], (x[1], x[2]))

    # 우주선 그리기
    screen.blit(ship, (pos_x, pos_y))

    # 화면갱신
    pg.display.update()

    time.sleep(0.1)

print('메인루프 종료')
while running2:
    screen.blit(over,(0,0))
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running2 = False
pg.quit()