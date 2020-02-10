# ATM

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
