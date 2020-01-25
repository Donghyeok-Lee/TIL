# 2차원 list 생성 방식에 따른 값 할당 문제

data_list = [[0] * 10] * 10

data_list2 = []
for i in range(10):
    data_list2.append([0]*10)




for i in range(10):
    print(data_list)

print('-'*50)

for i in range(10):
    print(data_list2[i])

print('='*50)

for i in range(3,7):
    for j in range(3, 7):
        data_list[i][j] = 1
        data_list2[i][j] = 1




for i in range(10):
    print(data_list[i])

print('-'*50)

for i in range(10):
    print(data_list2[i])


data_list = [3, 6, 7, 1, 5, 4]
n = len(data_list) # n:원소의 개수

for i in range(1<<n) : # 1<<n : 부분 집합의 개수
    for j in range(n): # 원소의 수만큼 비트를 비교함
        if i & (1<<j) : # i의 j번째 비트가 1이면 j번째 원소 출력
            print(data_list[j], end=',')
    print() 