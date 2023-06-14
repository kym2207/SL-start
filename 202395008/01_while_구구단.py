'''
사용자가 0을 입력할 때 까지
사용자가 원하는 구구단 출력하기

[문제분석]
무한반복 - while True
사용자가 0을 입력 할 때까지 계속 단을 입력 받는다.

사용자가 0을 이력 했는지 안닌지를 판단.

구구단은 곱하는 수가 1~9까지 1씩 증가한다.
'''
# 알고리즘
# 1 .무한 반복한다.
#       1) 단을 입력 받는다.
#       2) 입력 값이 0인가?
#           a. 프로그램을 종료한다. break
#       3) 곱하는 수를 1부터 10까지 반복하면서
#           a. 구구단을 출력한다.
# 2. 구구단 종료 출력한다.
while True:
    dan=int(input("단을 입력하세요. (0입력시 종료)"))
    if dan==0:
        break
    for i in range(1,10):
        print(dan,'*',i,'=',dan*i)
print("구구단 종료")
while True:
    dan=int(input("단을 입력하세요. (0입력시 종료)"))
    if dan==0:
        break
    su=1
    while su<=9:
        print("{} X {} = {}".format(dan,su,dan*su))
        su+=1
print("구구단 종료")