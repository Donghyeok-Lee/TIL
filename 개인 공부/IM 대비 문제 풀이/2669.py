# 직사각형 네개

num_list = [[0] * 100 for _ in range(100)]
xy_list = [list(map(int, input().split())) for _ in range(4)]

for k in range(4):
    for i in range(xy_list[k][0], xy_list[k][2]):
        for j in range(xy_list[k][1], xy_list[k][3]):
            num_list[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if num_list[i][j] == 1:
            cnt += 1

print(cnt)
