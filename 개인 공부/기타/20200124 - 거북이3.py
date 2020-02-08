import turtle, math

def set_space(x1, x2, y1, y2): # x, y 좌표계 설정 해주는 함수
    turtle.setworldcoordinates(x_min, y_min, x_max, y_max) # 좌표계 설정
    turtle.speed(0) # 최대 속도로
    turtle.pensize(1) # 얇은 선으로

    turtle.up() # x축 그림
    turtle.goto(x_min, 0)
    turtle.down()
    turtle.goto(x_max, 0)

    turtle.up() # y축 그림
    turtle.goto(0, y_min)
    turtle.down()
    turtle.goto(0, y_max)
    
    turtle.up() # 원점으로 돌아오고, 파란색, 사이즈2로 변경
    turtle.goto(0, 0)
    turtle.down()
    turtle.color('blue')
    turtle.pensize(2)

"""
# 삼각함수 그래프 그리기

x_min, x_max, y_min, y_max = -5, 5, -5, 5
set_space(x_min, x_max, y_min, y_max)

space = 0.1
func_list = ['y = math.tan(x)', 'y=math.cos(x)', 'y = math.sin(x)']

for func in func_list:
    x = x_min
    exec(func)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    while x <= x_max:
        x = x + space
        exec(func)
        turtle.goto(x, y)

turtle.mainloop()


# 극 좌표계를 이용한 그림 그리기

x_min, x_max, y_min, y_max = -5, 5, -5, 5

set_space(x_min, x_max, y_min, y_max)

func = 'r = 1 + math.cos(theta)'
theta = 0
space = 0.1

exec(func)
x = r * math.cos(theta)
y = r * math.sin(theta)

turtle.up()
turtle.goto(x, y)
turtle.down()

while theta <= 6.2:
    theta += space
    exec(func)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.goto(x, y)

turtle.goto(2, 0)

turtle.mainloop()


# 사이클로이드 곡선

x_min, x_max, y_min, y_max = 0, 10, -5, 5

set_space(x_min, x_max, y_min, y_max)
t = 0
space = 0.1

x = t - math.sin(t)
y = 1 - math.cos(t)

turtle.up()
turtle.goto(x, y)
turtle.down()

while t <= 10:
    t += space
    x = t - math.sin(t)
    y = 1 - math.cos(t)
    turtle.goto(x, y)

turtle.mainloop()


# 거북이 마지막

turtle.color('red')
turtle.begin_fill()

for x in range(100):
    h = math.pi * x /50
    x = 160 * math.sin(h)**3
    y = 130 * math.cos(h) - 50 * math.cos(2*h) - 20 * math.cos(3*h) -10 * math.cos(4*h)
    turtle.goto(x, y)

turtle.end_fill()

turtle.mainloop()
"""