# 인덱스 꼬임
N = 8
data_list = [0, 1, 0, 1, 0, 0, 0, 1]

M = 2
input_list = [[1, 3], [2, 3]]

# for k in range(M):
#

if input_list[0][0] == 1:
    j = input_list[0][1]
    while j < N:
        data_list[j-1] += 1
        if data_list[j-1] == 2:
            data_list[j-1] = 0
        j += j

print(data_list)

if input_list[1][0] == 2:
    k = 0
    while data_list[input_list[1][1]-k] == data_list[input_list[1][1]+k]:
        data_list[input_list[1][1] - k] += 1
        data_list[input_list[1][1] + k] += 1
        if data_list[input_list[1][1]-k] == 2:
            data_list[input_list[1][1] - k] = 0
        if data_list[input_list[1][1]+k] == 2:
            data_list[input_list[1][1] + k] = 0
        k += 1

print(data_list)