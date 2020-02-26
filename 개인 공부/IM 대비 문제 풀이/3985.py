# 케이크

L = int(input())
N = int(input())
test_list = [list(map(int, input().split())) for _ in range(N)]

data_list = [0] * L

max_cnt = max_exp = 0
max_per = max_exp_per = 1
for i in range(N):
    temp_cnt = 0
    for j in range(test_list[i][0]-1, test_list[i][1]):
        if not data_list[j]:
            data_list[j] = i + 1
            temp_cnt += 1
    if max_cnt < temp_cnt:
        max_cnt = temp_cnt
        max_per = i + 1
    if max_exp < test_list[i][1] - test_list[i][0]:
        max_exp = test_list[i][1] - test_list[i][0]
        max_exp_per = i + 1

print(max_exp_per)
print(max_per)