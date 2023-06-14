'''
숫자 추측 게임 만들기
[문제 분석]
사용자가 입력한 값과 컴퓨터가 생성한 랜덤 값을 비교한다.
몇번 만에 맞혔는지 알려준다.

사용자에게 힌트를 준다.
사용자가 입력한 값이 랜덤값 보다 크면 숫자는 작다라고 한다.
사용자가 입력한 값이 랜덤값 보다 작으면 숫자는 크다라고 한다.

사용자가 값을 입력하여 힌트를 받을 대 마다 count를 한다.
'''
import random
while True:
    a=random.randint(1,30)
    print("UP DOWN게임 범위(1~30) / (0입력시 종료)")
    start=input("y입력시 시작됩니다.")
    if start=='y' or start=='Y':
        count = 1
        while True:
            su=int(input("수 입력 : "))
            if su==0:
               exit() 
            elif su>a:
                print(su,"보다 작습니다.")
                count += 1
            elif su<a:
                print(su,"보다 큽니다.")
                count += 1
            else:
                print("정답",count,"번 걸렸습니다.")
                count=1 
                break
    else:
        break
    
