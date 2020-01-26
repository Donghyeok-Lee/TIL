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
