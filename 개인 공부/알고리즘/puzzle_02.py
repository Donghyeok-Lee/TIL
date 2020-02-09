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



# Step3. 책에서 제시한 코드

def bestTimeToParty(schedule):
    start = schedule[0][0]
    end = schedule[0][1]
    for c in schedule:  # 스케줄 표 내의 전체적인 시작점, 끝점 확인
        start = min(c[0], start)
        end = max(c[1], end)
    count = celebrityDensity(schedule, start, end)
    maxcount = 0
    for i in range(start, end + 1): # count 함수를 통해 생성된 리스트에서 최대값 확인
        if count[i] > maxcount:     # max, count 메서드로 줄일 수 있을 듯
            maxcount = count[i]
            time = i
    print('{}시에 가면 {}명을 만날 수 있습니다.'.format(time, maxcount))

def celebrityDensity(sched, start, end):    # range 내의 숫자를 count하는 함수
    count = [0] * (end + 1)
    for i in range(start, end+1):
        count[i] = 0
        for c in sched:
            if c[0] <= i and c[1] > i:
                count[i] += 1
    return count

sched= [(6, 7), (7, 9), (10, 11), (10, 12), (8, 10), (9, 11), (6, 8)]
bestTimeToParty(sched)



# Step4. 책을 본 뒤 생각한 방법
data_list = [(6, 7), (7, 9), (10, 11), (10, 12), (8, 10), (9, 11), (6, 8)]

test_list = []
for test in data_list:
    test_list.append((c[0], 's'))
    test_list.append((c[1], 'e'))

# 이런식으로 이름표 붙여서 한번에 숫자세기..?




# Step5. 다르게 생각해보기
# 어차피 새로운 사람이 올 때만 최댓값 확인하면 되지 않나...

data_list = [(6, 7), (7, 9), (10, 11), (10, 12), (8, 10), (9, 11), (6, 8)]
N = len(data_list)
max_cnt = 0

for i in range(N):
    temp_cnt = 0
    for j in range(N):
        if data_list[i][0] in range(data_list[j][0], data_list[j][1]):
            temp_cnt += 1
    if max_cnt < temp_cnt:
        max_cnt = temp_cnt
        time = data_list[i][0]

print('{}시에 가면 {}명을 만날 수 있습니다.'.format(time, max_cnt))

# 근데 생각해보면 이것도 시간복잡도가 N제곱인데..?



"""