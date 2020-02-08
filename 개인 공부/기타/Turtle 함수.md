# Turtle 함수

> 거북이(Turtle)를 이용하여 그림을 그리는 방법

```python
import turtle as t # turtle 함수를 t로 불러옴
t = t.shape('turtle') # 그림을 거북이 모양으로 바꿔줌

t.exitonclick() # 화면을 클릭하면 나가짐
```



* Turtle 함수를 이용하여 사각형 그리기

```python
t.forward(50)	# 거북이를 50 픽셀만큼 전진
t.right(90)		# 거북이를 90도 오른쪽으로 회전
t.forward(50)	# 반복
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)	# 마지막에 90도 회전을 안 줘서 거북이가 위쪽을 바라보고 있음
```

```python
for i in range(4):	# 반복문을 활용한 사각형 그리기
    t.forward(50)
    t.right(90)
```



![image-20200121223234515](C:\Users\lee33\AppData\Roaming\Typora\typora-user-images\image-20200121223234515.png)



* Turlte 함수를 이용하여 삼각형 그리기

```python
t.forward(50)
t.right(120)
t.forward(50)
t.right(120)
t.forward(50)
```

```python
t.left(90) # 거북이가 위를 바라보도록 바꿔줌
for i in range(3):
    t.forward(50)
    t.right(120)
```



![image-20200121223427242](C:\Users\lee33\AppData\Roaming\Typora\typora-user-images\image-20200121223427242.png)



* Turtle 함수를 이용하여 원 그리기

```python
t.right(120) # 바라보는 방향을 접선의 방향으로 가지는 원을 그리기 때문에 추가함
t.circle(50)
```

![image-20200121222534540](C:\Users\lee33\AppData\Roaming\Typora\typora-user-images\image-20200121222534540.png)



* Turtle 함수의 메서드

```python
t.forward(50) or t.fd(50)		# 거북이를 앞으로 50만큼 이동
t.backward(50) or t.back(50)	# 거북이를 뒤로 50만큼 이동
t.left(90) or t.lt(90)			# 거북이를 왼쪽으로 90도 회전
t.right(90) or t.rt(90)			# 거북이를 오른쪽으로 90도 회전
t.circle(50)					# 현재 위치에서 반지름 50인 원을 그림
t.down() or t.pendown()			# 펜(잉크 묻힌 꼬리)를 내림
t.up or t.penup()				# 펜(잉크 묻힌 꼬리)를 올림
t.shape('모양')				# 거북이 모양 변경('arrow', 'turtle', 'circle 등')
t.speed(10)					# 거북이 속도 조절 1 : 가장 느림 10 : 빠름 0 : 최고 속도
t.pensize(5) or width(5)	# 펜의 굵기 변경
t.color('red')	# 펜의 색상 변경
t.bgcolor('red') # 배경 색상 변경
t.fillcolor('red') # 도형 내부를 칠하는 색상 결정
t.begin_fill()	# 도형 내부 색칠 준비
t.end_fill()	# 도형 내부 색칠
t.showturtle() or t.st()	# 거북이를 화면에 표시
t.hideturtle() or t.ht()	# 거북이 숨기기
t.clear()					# 거북이는 놔두고 화면을 지움
t.reset()					# 거북이도 초기 상태로 되돌리고 화면도 지움
```

![image-20200121222718124](C:\Users\lee33\AppData\Roaming\Typora\typora-user-images\image-20200121222718124.png)



* 기타] 반복문을 활용한 도형 그리기

```python
for i in range(1, 101):
    t.forward(i)
    t.right(90)
```

![image-20200121222915108](C:\Users\lee33\AppData\Roaming\Typora\typora-user-images\image-20200121222915108.png)

* 반지름 100인 원을 그리고, 내부를 파란색으로 칠하기

```python
t.fillcolor('blue')
t.begin_fill()
t.circle(100)
t.end_fill()
```

![image-20200121225102593](C:\Users\lee33\AppData\Roaming\Typora\typora-user-images\image-20200121225102593.png)



* 반지름 100인 원을 반복해서 그리기

```python
t.bgcolor('black') # 배경 색을 검정색으로 지정
t.color('green') # 선의 색을 초록색으로 지정
t.speed(0) # 거북이는 최고 속도로
for i in range(40): # 40까지 반복
    t.circle(100) # 반지름 100인 원을 그림
    t.left(360/40) # 방향을 360/40도만큼 돌림

t.penup() # 펜(잉크가 묻은 꼬리)를 들어 올림
t.goto(400, 0) # (400, 0)으로 거북이 이동, 펜을 들어올렸기때문에 흔적 X
t.pendown() # 펜(잉크가 묻은 꼬리)를 내림 (그리기 시작)

for i in range(80): # 80으로 반복
    t.circle(100)
    t.left(360/80)
```

![image-20200121225755764](C:\Users\lee33\AppData\Roaming\Typora\typora-user-images\image-20200121225755764.png)