# 세 수

test = list(map(int, input().split()))

test.remove(max(test))
test.remove(min(test))

print(test[0])