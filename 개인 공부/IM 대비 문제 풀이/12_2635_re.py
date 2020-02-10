# 수 잇기

N = int(input())
test = []
test.append(N)
max_len = 0
for i in range(N):
    test.append(i)
    while test[-1] > 0:
        test.append(test[-2] - test[-1])
    test.pop(-1)
    if max_len < len(test):
        max_len = len(test)
        max_list = test
    test = [N]

print(max_len)
print(' '.join(map(str, max_list)))