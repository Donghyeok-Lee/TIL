"""

# 1.5.9.2 영식

N, M, L = map(int, input().split())

num_list = [0] * N

num_list[0] = 1
cnt = 0
i = temp_i = 0
while True:
    if num_list[i] % 2:
        temp_i = i + L
    else:
        temp_i = i - L

    if temp_i < 0:
        i = temp_i + N
    elif temp_i >= N:
        i = temp_i - N
    else:
        i = temp_i
    num_list[i] += 1
    cnt += 1

    if num_list[i] == M:
        break

print(cnt)


# 2.9.9.9 비밀
text = input()
N = len(text)
R = C = 0
result = ''
for i in range(1, int(N**0.5)+1):
    if not N % i:
        R = i

C = N // R

data_list = [[''] * C for _ in range(R)]
num = 0
for i in range(C):
    for j in range(R):
        data_list[j][i] = text[num]
        num += 1

for i in range(R):
    result += ''.join(data_list[i])

print(result)


# 3.9.8.5 기네스

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


# 1.1.3.9.9 ATM
N = int(input())

Pi = list(map(int, input().split()))

for i in range(N):
    min_idx = i
    for j in range(i+1, N):
        if Pi[min_idx] > Pi[j]:
            min_idx = j
    Pi[min_idx], Pi[i] = Pi[i], Pi[min_idx]

total = 0
for i in range(N):
    for j in range(i+1):
        total += Pi[j]

print(total)


"""
