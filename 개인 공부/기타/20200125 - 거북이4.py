# 재귀호출을 이용한 프랙탈 - 재귀호출 이해

# 1. 시에르핀스키의 삼각형
import turtle

def tri(tri_len):
    if tri_len <= 10: # 10이하이면 삼각형 1개 그림
        for i in range(0, 3):
            turtle.fd(tri_len)
            turtle.left(120)
        return
    new_len = tri_len / 2
    tri(new_len)
    turtle.fd(new_len)
    tri(new_len)
    turtle.bk(new_len)
    turtle.left(60)
    turtle.fd(new_len)
    turtle.right(60)
    tri(new_len)
    turtle.left(60)
    turtle.bk(new_len)
    turtle.right(60)

turtle.speed(0)
tri(10) # 2배로 할 수록 전체 삼각형의 높이 2배 됨
turtle.hideturtle()
turtle.done

turtle.mainloop()