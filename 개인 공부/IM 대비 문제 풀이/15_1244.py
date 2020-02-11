# 인덱스 꼬임

N = int(input())
data_list = [0] + list(map(int, input().split()))

M = int(input())
input_list = [list(map(int, input().split())) for _ in range(M)]

for k in range(M):
    if input_list[k][0] == 1:
        i = input_list[k][1]
        while i < N + 1:
            data_list[i] += 1
            if data_list[i] == 2:
                data_list[i] = 0
            i += input_list[k][1]
    else:
        i = input_list[k][1]
        data_list[i] += 1
        if data_list[i] == 2:
            data_list[i] = 0
        j = 1
        while i - j > 0 and i + j < N + 1 and data_list[i + j] == data_list[i - j]:
            data_list[i + j] += 1
            if data_list[i + j] == 2:
                data_list[i + j] = 0
                data_list[i - j] = 0
            else:
                data_list[i - j] += 1
            j += 1

data_list.pop(0)

while data_list:
    result = []
    if len(data_list) > 20:
        for _ in range(20):
            result.append(data_list.pop(0))
        print(' '.join(map(str, result)))
    else:
        print(' '.join(map(str, data_list)))
        data_list.clear()