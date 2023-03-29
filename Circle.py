#반지름 입력받아 원의 넓이 및 원의 둘레 정수 데이터형으로 출력하는 프로그램
PI = 3.14159
radius = input('반지름의 길이를 입력하세요. : ')

#원의 넓이 구하는 함수
def calcArea(PI, r):
    a = PI * int(r) ** 2
    return a

#원의 둘레 구하는 함수
def calcCircum(PI, r):
    c = 2 * PI * int(r)
    return c

area = int(calcArea(PI, radius))
circum = int(calcCircum(PI, radius))

print('area = ', area)
print('circum = ', circum)
