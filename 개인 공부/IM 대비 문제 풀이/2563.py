# 색종이

color_list = [[0] * 100 for _ in range(100)]
N = int(input())
xy_list = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(xy_list[k][0], xy_list[k][0] + 10):
        for j in range(xy_list[k][1], xy_list[k][1] + 10):
            color_list[i][j] = 1

cnt = 0

for i in range(100):
    for j in range(100):
        if color_list[i][j] == 1:
            cnt += 1

print(cnt)