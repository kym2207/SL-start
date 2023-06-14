'''
continue
'''

numbers = [5, 16, 8, 17, 41, 1, 12, 3, 19, 10]

print("리스트 값 중 10보다 큰 수 - 반복문 사용 ")

for i in numbers:
    if i >= 10:
        print(i, end=', ')

print()

print("리스트 값 중 10보다 큰 수 - continue 사용")
for i in numbers:
    if i<10:
        continue
    print(i,end=', ')
    
print()

# 1~30사이의 수 중에서 7의 배수만 출력 - continue 사용

list=list(range(1,31))
print("1~30사이 수 중 7의 배수 출력")
for i in list:
    if i%7 != 0:
        continue
    print(i,end=', ')
