# 종이

N, M = map(int, input().split())
n = int(input())
input_list = [list(map(int, input().split())) for _ in range(n)]
row_list = []
col_list = []

for case in input_list:
    if case[0] == 0:
        row_list.append(case[1])
    else:
        col_list.append(case[1])

row_list = [0] + sorted(row_list) + [M]
col_list = [0] + sorted(col_list) + [N]

result = []

for i in range(len(row_list)-1):
    for j in range(len(col_list)-1):
        total = 0
        for k in range(row_list[i], row_list[i+1]):
            for l in range(col_list[j], col_list[j+1]):
                total += 1
        result.append(total)

print(max(result))