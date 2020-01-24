
# # 동명 이인 찾기 함수 작성

# names = ['Tom', 'Jerry', 'Edgar', 'Tom', 'Eddy', 'Edgar', 'James', 'Jane', 'Jane']
# data_set = set()

# for i in range(0,len(names) - 1):
#     for j in range(i+1, len(names)):
#         if names[i] == names[j]:
#             data_set.add(names[i])

# print(data_set)


"""
재귀 호출 : 어떤 함수 안에서 자기 자신을 부르는 것
적절한 종료 조건을 통해서 호출을 마무리해야 됨
"""


# # 재귀 호출을 이용한 정수의 합 구하기
# def mysum(n):
#     if n != 1:
#         return n + mysum(n-1)
#     elif n == 1:
#         return 1
    
# n = int(input("숫자 입력하세요. : "))

# sums = mysum(n)
# print(sums)

# # 재귀 호출을 이용한 정수의 곱 구하기
# def mymul(n):
#     if n != 1:
#         return n * mymul(n-1)
#     elif n == 1:
#         return 1

# n = int(input("숫자 입력하세요. : "))

# muls = mymul(n)
# print(muls)

# # 재귀 호출을 이용한 피보나치 수열 계산

# def fibo(n):
#     if n > 1:
#         return fibo(n-1)+fibo(n-2)
#     else:
#         return n


# n = int(input("숫자 입력하세요. : "))

# x = fibo(n)
# print(x)


# # 재귀 호출을 이용한 하노이의 탑 예제

# def hanoi(number, fro, to, ass):
#     if number == 1:
#         print(fro, '->', to)
#         return

#     hanoi(number-1, fro, ass, to)
#     print(fro, '->', to)
#     hanoi(number-1, ass, to, fro)

# print('n = 1')
# hanoi(1, 1, 3, 2)
# print('n = 2')
# hanoi(2, 1, 3, 2)
# print('n = 3')
# hanoi(3, 1, 3, 2)



# # 순차 탐색을 통한 특정 값의 위치 찾기

# def search_list(a, x):
#     n = len(a)
#     test = []
#     for i in range(0, n): # 리스트 a의 모든 값을 순차적으로 비교
#         if x == a[i]: # x값과 비교
#             test.append(i) # 일치한다면 리스트에 항목 추가
#     return test # 끝까지 없으면 빈 리스트 [] 리턴

# v = [17, 92, 18, 33, 58, 7, 33, 42, 33, 42, 58, 77, 19, 54, 92, 33, 18]
# print(search_list(v, 18)) # 2, 16
# print(search_list(v, 92)) # 1, 14
# print(search_list(v, 109)) # [] (109는 리스트에 없음)


# # 순차 탐색을 활용한 학생부 만들기
# stu_no = [39, 14, 67, 105]
# stu_name = ['Justin', 'John', 'Mike', 'Summer']

# def search_no(a, x):
#     n = len(a)
#     for i in range(0, n):
#         if a[i] == x:
#             return i
#     return '?'

# n = int(input("학생 번호 입력 : "))

# a = search_no(stu_no, n)

# if a == '?':
#     print(a)
# else:
#     print(stu_name[a])
