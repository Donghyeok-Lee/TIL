num_list = [[0] * 21 for _ in range(21)]

dir_list = ((1, 0), (0, 1), (1, 1), (1, -1))

N = int(input())

for tc in range(1, N+1):
    i, j = map(int, input().split())
    if tc % 2:
        num_list[i][j] = 1
    else:
        num_list[i][j] = 2
    result = []
    for k in range(4):
        test = ''
        for d in range(-30, 30):
            temp_i = i + dir_list[k][0] * d
            temp_j = j + dir_list[k][1] * d
            if temp_i >= 0 and temp_j >=0 and temp_i < 21 and temp_j < 21:
                test += str(num_list[temp_i][temp_j])
        result.append(test)

    flag = 0
    for i in range(len(result)):
        if '11111' in result[i]:
            if'111111' not in result[i]:
                print(tc)
                flag = 1
                break
        if '22222' in result[i]:
            if '222222' not in result[i]:
                print(tc)
                flag = 1
                break
    if flag:
        break
if not flag:
    print(-1)


"""
# 오답?
num_list = [[0] * 21 for _ in range(21)]

dir_list = ((1, 0), (0, 1), (1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1), (-1, 1))

N = int(input())
case = [list(map(int, input().split())) for _ in range(N)]
flag = True

for t in range(N):
    if (t + 1) % 2:
        num_list[case[t][0]][case[t][1]] = color = 1
    else:
        num_list[case[t][0]][case[t][1]] = color = 2

    cnt_list = [0] * 8
    for l in range(8):
        dis = 1
        temp_i = case[t][0] + dir_list[l][0] * dis
        temp_j = case[t][1] + dir_list[l][1] * dis
        while num_list[temp_i][temp_j] == color:
            dis += 1
            temp_i = case[t][0] + dir_list[l][0] * dis
            temp_j = case[t][1] + dir_list[l][1] * dis
        cnt_list[l] = dis - 1

    for i in range(4):
        if cnt_list[i] + cnt_list[i+4] == 4:
            flag = False
            print(t+1)
if flag:
    print(-1)
    


# 교수님 방식
def f(i, j):
    global flag
    c = bd[i][j]
    v = [0] * 8
    for k in range(8):
        ni = i + di[k][0]
        nj = j + di[k][1]
        cnt = 0
        while bd[ni][nj] == c:
            ni = ni + di[k][0]
            nj = nj + di[k][1]
            cnt += 1
        v[k] = cnt
    for i in range(4):
        if v[i] + v[i+4] == 4:
            flag = False
            return 1
    else:
        return 0


bd = [[0] * 21 for _ in range(21)]

di = ((1, 0), (0, 1), (1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1), (-1, 1))

N = int(input())
case = [list(map(int, input().split())) for _ in range(N)]
flag = True
for t in range(N):
    i = case[t][0]
    j = case[t][1]
    bd[i][j] = t % 2 + 1
    if f(i, j):
        print(t+1)
        break
if flag:
    print(-1)


"""