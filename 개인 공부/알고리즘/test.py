# 개인 공부 시 Test Code 입니다.
#
# coins = [100, 50, 10, 1]
# value = 362
# dic = {}
#
# for i in coins: # 각 동전의 크기를 key 값, value를 0으로 초기화
#     dic[i] = 0
#
# while value != 0:
#     for coin in coins:
#         if coin <= value:
#             dic[coin] += 1
#             value -= coin
#             break
#
# for key, val in dic.items():
#     print('{0}원 동전 : {1}개'.format(key, val))


# # 삽입 정렬 알고리즘
# def find_ins_idx(r, v): # list r에서 v가 들어가야할 위치 찾기
#     for i in range(0, len(r)): # 정렬된 리스트 r의 자료를 앞에서부터 확인
#         if v < r[i]: # v보다 i번째 위치의 값이 크면 v가 그 값 바로 앞에 놓여야 됨
#             return i
#     return len(r) # 위치를 못 찾았으면, r의 모든 원소보다 v가 큼 (가장 마지막에 들어감)

# def ins_sort(a):
#     result = [] # 정렬된 값 저장
#     while a: # 기존 리스트에 값이 있으면 반복
#         value = a.pop(0) # 기존 리스트에서 꺼냄
#         ins_idx = find_ins_idx(result, value) # 꺼낸 값이 들어갈 위치 찾기
#         result.insert(ins_idx, value) # 찾은 위치에 값 삽입 (이후 값이 한 칸 씩 밀림)
#         print('정렬할 값 : {0}, 들어갈 위치 인덱스 : {1}\n정렬된 리스트 : {2}'.format(value, ins_idx, result))
#     return result

# d = [2, 4, 5, 1, 3]
# print(ins_sort(d))


# # 병합 정렬
# def merge_sort(a):
#     n = len(a)
#     if n <= 1: # 종료조건, 정렬할 리스트의 자료 개수가 1개 이하이면 정렬할 필요 없음
#         return a
#     # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
#     mid = n //2 # 중간을 기준으로 2개로 나눔
#     g1 = merge_sort(a[:mid]) # 재귀 호출, 첫 번째 그룹
#     g2 = merge_sort(a[mid:]) # 재귀 호출, 두 번째 그룹
#     # 이제부터 2개의 그룹을 1개로 병합하기 시작
#     result = []
#     while g1 and g2: # g1과 g2에 모두 자료가 남아있을 때
#         if g1[0] < g2[0]: # 두 그룹의 맨 앞 위치 비교
#             result.append(g1.pop(0))
#         else:
#             result.append(g2.pop(0))
#         # 아직 남은 자료들이 다시 추가되어 반복
#     while g1:
#         result.append(g1.pop(0))
#     while g2:
#         result.append(g2.pop(0))
#     return result

# d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
# print(merge_sort(d))


"""




x = 30
test = []

while x != 1:
    for i in range(2, x+1):
        if x % i == 0:
            test.append(i)
            x //= i
            print(x)

print(test)


data_list = [1, 3, 4, 5, 7, 2, 6]
test = [] # 두 값의 차이를 저장할 함수

for i in range(1, len(data_list)):
    print(data_list[:i], data_list[i:])
    print('첫번째 합 : {0} / 두번째 합 {1}'.format(sum(data_list[:i]), sum(data_list[i:])))
    test.append(sum(data_list[:i]) - sum(data_list[i:]))

print('test : {0}'.format(test))
"""


def solution(s):
    que = []
    stack = []
    
    for x in s:
        if x.isalpha():
            que.append(x.lower())
            stack.append(x.lower())
    while que:
        if que.pop(0) != stack.pop():
            return False
    return True

print(solution('Wow'))
print(solution('Madam,I`m Adam'))
print(solution('Madam,I am Adam'))


