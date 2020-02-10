# 비밀

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