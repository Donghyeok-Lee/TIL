
"""
# Turtle 함수를 이용한 그림 그리기 놀이

import turtle as t
t.shape("turtle")

# 빨간선으로 사각형 그리기
t.color('red')
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)

# 파란선, 굵기 5로 삼각형 그리기
t.color('blue')
t.pensize(5)
t.forward(50)
t.right(120)
t.forward(50)
t.right(120)
t.forward(50)

# 초록색선, 굵기 10으로 원 그리기
t.color('green')
t.pensize(10)
t.right(120)
t.circle(50)

# 반복문을 활용한 그림 그리기
for i in range(1, 201, 2):
    t.forward(i)
    t.right(90)

# 반복문을 활용한 사각형 그리기
for i in range(4):
    t.forward(50)
    t.right(90)

# 반복문을 활용한 삼각형 그리기
t.left(90)
t.fillcolor('green')
t.begin_fill()
for i in range(3):
    t.forward(50)
    t.right(120)
t.end_fill()

# 느리게 파란색으로 칠해진 원 그리기
t.speed(1)
t.fillcolor('blue')
t.begin_fill()
t.circle(100)
t.end_fill()

t.bgcolor('black')
t.color('green')
t.speed(0)
for i in range(40):
    t.circle(100)
    t.left(360/40)

t.penup()
t.goto(400, 0)
t.pendown()

t.speed(0)
for i in range(80):
    t.circle(100)
    t.left(360/80)


t.exitonclick()
"""

"""
# Time 함수를 이용한 시간 재기 게임
import time

input("시작 : Enter")
start = time.time() # 현재 시각 저장

input("20초가 된 것 같으면 Enter를 누르세요!")
end = time.time() # Enter를 누른 시점에서의 시각 저장

et = end - start #(end의 시간 - start의 시간)
print("실제 시간 : {0}초".format(et))
print("차이 : {0}초".format(abs(et-20)))

# random 함수를 이용한 덧셈 문제 내기
import random
a = random.randint(1, 50)
b = random.randint(1, 50)

x = int(input("{0} + {1}의 값은? ".format(a, b)))
# input 안에도 포맷팅 가능!

if x == a + b:
    print('정답입니다!')
else:
    print('오답입니다.')

# random 함수를 이용한 숫자 맞추기 게임
import random
num = random.randint(1, 100)

while True:
    x = int(input("숫자를 맞춰 보세요! : "))
    if x == num:
        print('정답입니다!')
        break
    if x > num:
        print('너무 큰 숫자입니다.')
    if x < num:
        print('너무 작은 숫자입니다.')
"""