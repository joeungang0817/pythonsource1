import random
import time


def dragonselect():
    dragonchoose=random.randint(1,20)
    return dragonchoose

def playerselect():
    print('select cave')
    playerchoose = input()
    return int(playerchoose)

def guess(dragonchosen, playerchosen):
    global win
    global y
    global score
    global score_report
    if playerchosen>dragonchosen:
        print('it is higher than dragon cave.')
        print('-200')
        score=score-200
        score_report.append(score)
        y=y+1
        print('your score is {}'.format(score))
        score=score-200
    elif playerchosen<dragonchosen:
        print('it is lower than dragon cave.')
        print('-200')
        score=score-200
        score_report.append(score)
        y=y+1
        print('your score is {}'.format(score))
    elif playerchosen==dragonchosen:
        print('you are killed dragon! congratulation!!!!')
        win=1
        score=score+500
        score_report.append(score)
        y=y+1
        print('your score is {}'.format(score))


playagain='yes'
while playagain=='yes':
    y=0
    score_report=[]
    win=0
    life=3
    score=1000
    while life>0:
        print('you have',life, 'life! start the game!!')
        dragon=dragonselect()
        print('kill the dragon!')
        for u in range(0,3):
            player=playerselect()
            guess(dragon,player)
            if win==1:
                break
        if win!=1:
            print('you do not kill dragon')
            print('you lose the life....')
            life=life-1
            print('your life is {}'.format(life))
    print('it is your score report.')
    for i in range(0,len(score_report)):
        print(score_report[i])
    print('do you want to playagain?')
    playagain=input()