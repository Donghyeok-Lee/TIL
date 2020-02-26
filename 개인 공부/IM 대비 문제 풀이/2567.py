# 색종이2 - 약간 다름

color_list = [[0] * 100 for _ in range(100)]
N = int(input())
xy_list = [list(map(int, input().split())) for _ in range(N)]


for k in range(N):
    for i in range(xy_list[k][0], xy_list[k][0] + 10):
        for j in range(xy_list[k][1], xy_list[k][1] + 10):
            color_list[i][j] = 1

dir_list = ((-1,0), (1,0), (0,-1), (0,1))


cnt = 0

for i in range(100):
    for j in range(100):
        if color_list[i][j] == 1:
            for l in range(4):
                temp_i = i + dir_list[l][0]
                temp_j = j + dir_list[l][1]
                if temp_i >= 0 and temp_j >= 0 and temp_i < 100 and temp_j < 100:
                    if color_list[temp_i][temp_j] == 1:
                        cnt -= 1

print(cnt)