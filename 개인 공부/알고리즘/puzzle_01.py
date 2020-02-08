"""
# 모두 똑같이 만들기!
# 1 : 흰 모자, 2: 검은 모자


# Step1. 혼자서 풀어보기
# 더 적은 갯수의 모자를 쓴 사람들에게 직접 다 명령하기

data_list = [1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1]
N = len(data_list)
cnt_1 = 0
min_color = 1       # 흰 모자가 더 적다고 가정 함
max_color = 2

for num in data_list:   # 리스트 내 흰 모자 개수를 cnt_1에 저장
    if num == min_color:
        cnt_1 += 1

if cnt_1 <= N // 2:     # 만약 cnt_1이 N//2보다 작다면
    min_cnt = cnt_1
else:
    min_color = 2       # 아닐 경우, 더 적은 모자를 검은색으로 변경
    max_colot = 1
    min_cnt = N - cnt_1 # 전체 개수에서 흰 모자 개수를 뺀 것을 최소 모자 개수로

cnt = 0 # 바꾸라고 말한 횟수
for i in range(N):
    if data_list[i] == min_color:
        data_list[i] = max_color
        cnt += 1

print('명령해야되는 횟수 : {}'.format(cnt))


# Step2. 조금 더 효율적으로 바꿔보기
# 1 모자를 쓴 사람들에게 범위로 명령하기
data_list = [1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1]
N = len(data_list)
idx_list = []   # 바꾸라고 명령하기 시작할 위치
dis_list = []   # 바꾸라고 명령할 범위

temp_idx = temp_dis = 0
flag = True
for i in range(N):
    if data_list[i] == 1:
        temp_dis += 1
        if flag:
            idx_list.append(i)
            flag = False
    if data_list[i] == 2 and temp_dis:
        dis_list.append(temp_dis)
        temp_dis = 0
        flag = True
    if i == N-1 and temp_dis:
        dis_list.append(temp_dis)

cnt = 0
for test in zip(idx_list, dis_list):
    cnt += 1
    for i in range(test[1]):
        data_list[test[0] + i] = 2

print('명령해야되는 횟수 : {}'.format(cnt))


# Step3. 조금 더 좋은 방법 찾아보기

data_list = [1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 3, 3, 3]
color_list = [1, 2, 3]
n = len(color_list)
N = len(data_list)
idx_list = [[] for _ in range(n)]
dis_list = [[] for _ in range(n)]

cur_color = data_list[0]
temp_dis = 1
idx_list[cur_color-1].append(0)

for i in range(1, N):
    if data_list[i] != cur_color:
        idx_list[data_list[i]-1].append(i)
        dis_list[cur_color-1].append(temp_dis)
        cur_color = data_list[i]
        temp_dis = 0
    temp_dis += 1
    if i == N-1 and temp_dis:
        dis_list[cur_color-1].append(temp_dis)

min_idx = 0
min_length = len(idx_list[min_idx]) # 각 모자 색생 별 idx list 중 짧은거
for i in range(1, n):
    if min_length > len(idx_list[i]):
        min_length = len(idx_list[i])
        min_idx = i

if min_idx == 1: # 2 모자가 더 적은 횟수로 처리 가능할 경우
    color = 1
else:               # 반대 경우
    color = 2
cnt = 0
for i in range(min_length):
    for j in range(dis_list[min_idx][i]):
        data_list[idx_list[min_idx][i] + j] = color
    cnt += 1

print('명령해야되는 횟수 : {}'.format(cnt))


# 모자가 3종류 이상이면 어떻게 해야될까

data_list = [1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 3, 3, 3]
color_list = [1, 2, 3]
n = len(color_list)
N = len(data_list)
idx_list = [[] for _ in range(n)]
dis_list = [[] for _ in range(n)]

cur_color = data_list[0]
temp_dis = 1
idx_list[cur_color-1].append(0)

for i in range(1, N):
    if data_list[i] != cur_color:
        idx_list[data_list[i]-1].append(i)
        dis_list[cur_color-1].append(temp_dis)
        cur_color = data_list[i]
        temp_dis = 0
    temp_dis += 1
    if i == N-1 and temp_dis:
        dis_list[cur_color-1].append(temp_dis)

# 여기까지는 모자 색상이 3개 이상이어도 적용 가능





# Step4. 책에서 제시한 코드 이해하기
# 책에서 제시한 코드 - 찾고, 명령하고 2번 확인 필요

def pleaseConform(caps):
    start = forward = backward = 0
    intervals = []  # (시작, 끝, 모자색)으로 된 튜플
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            intervals.append((start, i-1, caps[start]))
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i
    intervals.append((start, len(caps)-1, caps[start]))
    if caps[start] == 'F':
        forward += 1
    else:
        backward += 1
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
            print('{}에서 {}까지 모자를 뒤집어주세요.'.format(t[0], t[1]))

cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']

pleaseConform(cap1)



# 한번에 해결하자! - 검은색을 줄이는게 옳다는 것을 알고 있는 듯..

def pleaseConformOnepass(caps):
    caps = caps + [caps[0]]
    for i in range(1, len(caps)):
        if caps[i] != caps[i-1]:
            if caps[i] != caps[0]:
                print('{}에서'.format(i), end ='')
            else:
                print('{}까지 모자를 뒤집어주세요'.format(i-1))

cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']

pleaseConformOnepass(cap1)


"""