"""
import turtle as t
import math

x_min = -5
x_max = 5

y_min = -5
y_max = 5

space = 0.1
func_list = ['y = math.tan(x)', 'y=math.cos(x)', 'y = math.sin(x)']

t.setworldcoordinates(x_min, y_min, x_max, y_max)
t.speed(0)
t.pensize(2)

t.up()
t.goto(x_min, 0)
t.down()
t.goto(x_max, 0)

t.up()
t.goto(0, y_min)
t.down()
t.goto(0, y_max)

t.color('blue')
for func in func_list:
    x = x_min
    exec(func)
    t.up()
    t.goto(x, y)
    t.down()
    while x <= x_max:
        x = x + space
        exec(func)
        t.goto(x, y)

        
t.mainloop()

"""


import turtle, math

x_min = -5
x_max = 5
y_min = -5
y_max = 5

turtle.speed(0)

turtle.setworldcoordinates(x_min, y_min, x_max, y_max)
space = 0.1

func = 'r = 1 + math.cos(theta)'
turtle.color('red')

turtle.up()
turtle.goto(x_min, 0)
turtle.down()
turtle.goto(x_max, 0)

turtle.up()
turtle.goto(0, y_min)
turtle.down()
turtle.goto(0, y_max)

theta = 0
turtle.begin_fill()
exec(func)
x = r * math.cos(theta)
y = r * math.sin(theta)
turtle.up()
turtle.goto(x, y)
turtle.down()
while theta <= 7:
    theta += space
    exec(func)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.goto(x, y)


    
turtle.mainloop()

# 조금 더 수정 필요