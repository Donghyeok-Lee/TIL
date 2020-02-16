# 파티에 오지 않는 사람 목록 찾기


# Step1. DFS로 시도 - DFS로는 풀기 어려울 듯...

# Step2. 탐욕 알고리즘으로 시도 - 오답 발생

# Step3. 완전탐색..?
# 어차피 5명밖에 안되는데... 부분집합 만들지 뭐..

"""
# 비트연산자를 이용한 모든 부분집합 만들기!

people = ['A', 'B', 'C', 'D', 'E']
N = 5
result_list = []

for i in range(1<<N):
    temp_list = []
    for j in range(N):
        if i & (1<<j):
            temp_list.append(people[j])
    result_list.append(temp_list)

max_list = []
max_len = 0
for result in result_list:
    if not ('C' in result and 'E' in result) and not ('D' in result and 'E' in result):
        if max_len < len(result):
            max_len = len(result)
            max_list = result

print(max_list)

"""

# 재귀를 이용한 부분집합..?

def com(n, lst):
    comb = []
    for i in range(2**n):
        num = i
        temp_list = []
        for j in range(n):
            if num % 2:
                temp_list = [lst[n-1-j]] + temp_list
            num //= 2
        comb.append(temp_list)
    return comb

print(com(5, [1,2,3,4,5]))