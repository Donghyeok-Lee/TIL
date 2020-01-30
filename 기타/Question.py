"""
# 물어본 내용들
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

for l in range(10):
    print(data_list2[l])

    
print('-'*50)

for m in range(10):
    print(id(data_list[m]))

print('=' * 50)

for m in range(10):
    print(id(data_list2[m]))

# data_list 의 방법으로 만들 경우 내부 값들의 id값이 다 똑같아서 하나를 바꿀 때 전부 바뀜
# data_list2 방법으로 만들어야 내부 id값이 달라서 괜찮음

"""

# 추가적으로 궁금한 사항

