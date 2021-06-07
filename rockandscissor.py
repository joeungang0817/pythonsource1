import random

gamelist=['가위','바위','보']
while 1:
    rockscissor=[]
    score = 10
    random.shuffle(gamelist)
    for i in range(0,10):
        rockscissor.append(random.choice(gamelist))
    for i in range(0,10):
        print('score : {}'.format(score))
        print('가위,바위,보!')
        print('어느것을 내시겠습니까? (가위, 바위, 보)')
        playerchoice=input()
        if playerchoice=='가위':
            if rockscissor[i]=='보':
                print('이김')
                score+=1
            elif rockscissor[i]=='바위':
                print('짐')
                score -= 1
            elif rockscissor[i]=='가위':
                print('무승부')
        elif playerchoice=='보':
            if rockscissor[i]=='보':
                print('무승부')
            elif rockscissor[i]=='바위':
                print('이김')
                score += 1
            elif rockscissor[i]=='가위':
                print('짐')
                score -= 1
        elif playerchoice=='바위':
            if rockscissor[i]=='보':
                print('짐')
                score -= 1
            elif rockscissor[i]=='바위':
                print('무승부')
            elif rockscissor[i]=='가위':
                print('이김')
                score += 1
        else:
            print('안 냈으니 짐')
    print('네 최종 스코어는 {} 이다.'.format(score))
