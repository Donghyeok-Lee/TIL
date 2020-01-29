"""

# 키보드로 거북이 움직이기

import turtle

def turtle_right():
    turtle.setheading(0)
    turtle.fd(10)

def turtle_left():
    turtle.setheading(180)
    turtle.fd(10)

def turtle_up():
    turtle.setheading(90)
    turtle.fd(10)

def turtle_down():
    turtle.setheading(270)
    turtle.fd(10)

def turtle_clear():
    turtle.clear()

def turtle_penup():
    turtle.penup()

def turtle_pendown():
    turtle.pendown()

turtle.shape('turtle')
turtle.speed(0)

turtle.onkeypress(turtle_right, 'Right')
turtle.onkeypress(turtle_left, 'Left')
turtle.onkeypress(turtle_up, 'Up')
turtle.onkeypress(turtle_down, 'Down')


turtle.onkeypress(turtle_penup, 'q')
turtle.onkeypress(turtle_pendown, 'w')

turtle.onkeypress(turtle_clear, "Escape")
turtle.listen()
turtle.mainloop()



# 마우스로 거북이 그리기
import turtle

def turtle_clear():
    turtle.clear()

turtle.shape('turtle')

turtle.speed(1)
turtle.onscreenclick(turtle.goto)

turtle.onkeypress(turtle_clear, "Escape")

turtle.mainloop()
"""


"""
# 소인수 분해 프로그램

def make_list(x):
    n = 2
    data_list = []
    while n <= x:
        if x % n == 0:
            x /= n
            data_list.append(n)
            n = 2
        else:
            n += 1
    return data_list

x = int(input('숫자 입력 : '))

data_list = make_list(x)

if x in data_list:
    print("소수입니다!")

data_dict ={}
for val in data_list:
    if val not in data_dict.keys():
        data_dict[val] = 1
    else:
        data_dict[val] += 1

text = []
for key, val in data_dict.items():
    text.append("{0}의 {1}제곱".format(key, val))

print(' x '.join(text))


#미로 찾기 알고리즘 공부할 것!

def solve_maze(maze, start, end):
    ex_rt = [] # 앞으로 이동 경로
    dn_rt = set() # 이미 이동한 꼭짓점

    ex_rt.append(start) # 시작 지점 입력
    dn_rt.add(start)

    while ex_rt:
        p = ex_rt.pop(0) # 앞으로 이동 경로에서 처리 대상을 가져옴
        v = p[-1] # 저장된 이동경로의 마지막 문자가 현재 처리할 꼭짓점
        if v == end: # 현재 꼭짓점이 도착점이면
            return p # 현재까지 저장된 전체 이동 경로
        for x in maze[v]: # 대상 꼭짓점에 연결된 꼭짓점 중에
            if x not in dn_rt: # 아직 이동한 적 없는 꼭짓점
                ex_rt.append(p + x) # 새 꼭짓점으로 추가하여, 이동경로에 추가
                dn_rt.add(x) # 이미 이동한 꼭짓점에도 추가
    return "빠져나오지 못하는 미로"


maze = {
    'a' : ['b'],
    'b' : ['a', 'f'],
    'c' : ['d'],
    'd' : ['c', 'h'],
    'e' : ['i'],
    'f' : ['b', 'g'],
    'g' : ['f', 'h'],
    'h' : ['d', 'g', 'l'],
    'i' : ['e', 'm'],
    'j' : ['f'],
    'k' : ['o'],
    'l' : ['h', 'p'],
    'm' : ['n', 'i'],
    'n' : ['o', 'm'],
    'o' : ['n', 'k', 'p'],
    'p' : ['l', 'o']
}

print(solve_maze(maze,'a', 'n'))


stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
n = len(stock)
max_profit = 0

for i in range(n-1):
    for j in range(i+1, n):
        profit = stock[j] - stock[i]
        if profit > max_profit:
            max_profit = profit

print(max_profit)
"""

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
n = len(stock)
max_profit = 0
min_price = stock[0]
for i in range(1, n):
    profit = stock[i] - min_price # 지금까지 최솟값에 주식을 사서 i 날에 파는 수익
    if profit > max_profit:
        max_profit = profit
    if stock[i] < min_price:
        min_price = stock[i]
print(max_profit)