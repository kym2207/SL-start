'''
학과 : 컴퓨터 공학부
학번 : 202395008
이름 : 김유민

학생 정보를 사전에 저장하고, (학번,이름)
특정 학생의 정보(학번)를 입력하여 학생을 찾아주세요.
'''

student = {}

print("::학생 정보 입력::")
while True:
    idNum = input("학번 입력 : ")
    if idNum == 'z':
        break
    name = input("이름 입력 : ")
    student[idNum] = name

print("입력 종료")
print(student)

print("학생 검색")
while True:
    idNum = input('찾고자 하는 학생의 학번을 입력 하세요 :')
    if idNum == "":
        break
    if idNum in student:
        print("<<검색 결과>>")
        print("학번 : ",idNum,'이름 : ',student(idNum))
    else:
        print('찾고자 하는 학생이 없습니다.')
print("프로그램 종료")