#회전 수를 입력 받아 터틀 회전 시키기
import turtle
turtle.setup(320, 320)
screen = turtle.Screen()
screen.title('입력받은 수만큼 회전 시키기')

my_ttl = turtle.getturtle()

input = turtle.textinput("", "터틀 회전 시키기, 회전 횟수를 입력하세요")
n = int(input)
length = 20

while True:
    for i in range(n+1):
        my_ttl.forward(length)
        my_ttl.left(90)
        length += 10
    turtle.right(90)
    break