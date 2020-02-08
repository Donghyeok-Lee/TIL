"""
# 파티에 참석 하기 가장 좋은 시간
# 파티에서 가장 많은 사람을 만나기!


# Step1. 혼자 해보기 - 딕셔너리..?
data_list = ((6, 7), (7, 9), (10, 11), (10, 12), (8, 10), (9, 11), (6, 8))
data_dict = {}

for i in range(len(data_list)):
    for j in range(data_list[i][0], data_list[i][1]):
        data_dict[j] = data_dict.get(j, 0) + 1

max_val = max_key = 0
for key, val in data_dict.items():
    if max_val < data_dict[key]:
        max_val = data_dict[key]
        max_key = key

print('{}시에 가면 {}명을 만날 수 있습니다.'.format(max_key, max_val))


# Step2. 다른 방법으로 해보기 - Count list 만들기
data_list = ((6, 7), (7, 9), (10, 11), (10, 12), (8, 10), (9, 11), (6, 8))
count_list = [0] * 13
N = len(data_list)

for i in range(N):
    for j in range(data_list[i][0], data_list[i][1]):
        count_list[j] += 1

max_idx = 0
max_val = count_list[0]
for i in range(len(count_list)):
    if max_val < count_list[i]:
        max_val = count_list[i]
        max_idx = i
print('{}시에 가면 {}명을 만날 수 있습니다.'.format(max_idx, max_val))


"""


# Step3. 책에서 제시한 코드

def bestTimeToParty(schedule):
    start = schedule[0][0]
    end = schedule[0][1]
    for c in schedule:
        start = min(c[0], start)
        end = max(c[1], end)
    count = celebrityDensity(schedule, start, end)
    print(count)
    maxcount = 0
    for i in range(start, end + 1):
        if count[i] > maxcount:
            maxcount = count[i]
            time = i

def celebrityDensity(sched, start, end):
    count = [0] * (end + 1)
    print(count)
    for i in range(start, end+1):
        count[i] = 0
        for c in sched:
            if c[0] <= i and c[1] > i:
                count[i] += 1
    return count

sched= [(6, 7), (7, 9), (10, 11), (10, 12), (8, 10), (9, 11), (6, 8)]
bestTimeToParty(sched)