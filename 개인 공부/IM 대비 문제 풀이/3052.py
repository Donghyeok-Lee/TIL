# 나머지

test_list = []

for _ in range(10):
    num = int(input())
    if num % 42 not in test_list:
        test_list.append(num % 42)

print(len(test_list))


