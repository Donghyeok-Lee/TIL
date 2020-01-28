# 2차원 list 생성 방식에 따른 값 할당 문제

data_list = [[0] * 10] * 10

data_list2 = []
for _ in range(10):
    data_list2.append([0]*10)

for k in range(10):
    print(data_list[k])

print('-'*50)

for n in range(10):
    print(data_list2[n])

print('='*50)

for i in range(3, 7):
    for j in range(3, 7):
        data_list[i][j] = 1
        data_list2[i][j] = 1



for l in range(10):
    print(data_list[l])

print('-'*50)

for m in range(10):
    print(data_list2[m])

