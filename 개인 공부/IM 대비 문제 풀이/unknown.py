"""
height_list = []
for _ in range(9):
    height_list.append(int(input()))

total = sum(height_list)

for i in range(1<<9):
    temp_list = []
    for j in range(9):
        if i & (1<<j):
            temp_list.append(height_list[j])
    if len(temp_list) == 2 and sum(temp_list) == total - 100:
        result_list = temp_list


for height in result_list:
    height_list.remove(height)

height_list.sort()

for height in height_list:
    print(height)




num_list = [
    [11, 12, 2, 24, 10],
    [16, 1, 13, 3, 25],
    [6, 20, 5, 21, 17],
    [19, 4, 8, 14, 9],
    [22, 15, 7, 23, 18]
    ]

numbers = [5, 10, 7, 16, 2, 4, 22, 8, 17, 13, 3, 18, 1, 6, 25, 12, 19, 23, 14, 21, 11, 24, 9, 20, 15]

for num in numbers:
    for i in range(5):
        for j in range(5):
            if num_list[i][j] == num:
                num_list[i][j] = ''

for i in range(5):
    print(num_list[i])




N, M = map(int, input().split())
num_list = list(map(int, input().split()))

max_total = 0
for i in range(M):
    max_total += num_list[i]

for i in range(1, N-M+1):
    temp_total = 0
    for j in range(M):
        temp_total += num_list[i+j]
    if max_total < temp_total:
        max_total = temp_total

print(max_total)

# 왜 시간초과..

# 처음껄 뺴고, 뒤에걸 더하는 식으로..?



"""


