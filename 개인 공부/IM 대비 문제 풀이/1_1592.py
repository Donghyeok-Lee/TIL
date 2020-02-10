# 영식이

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