# 가짜 찾기 ㅎㅎ - 분할 정복
# 한번의 저울질로 리스트를 1/3으로 할 수 있기때문에 이분 탐색보다 유리함

def compare(group_A, group_B):
    if sum(group_A) > sum(group_B):
        result = 'left'
    elif sum(group_A) < sum(group_B):
        result = 'right'
    else:
        result = 'equal'
    return result


def splitCoins(coinsList):  # 코인의 개수는 3의 n제곱
    length = len(coinsList)
    group1 = coinsList[0 : length // 3]
    group2 = coinsList[length // 3 : length * 2 // 3]
    group3 = coinsList[length * 2 // 3 : length]
    return group1, group2, group3


def find(group1, group2, group3):   # 이거랑 위의 함수를 반복하면
    test = compare(group1, group2)  # 계속 1/3으로 줄일 수 있을 듯
    if test == 'left':
        fake = group1
    elif test == 'right':
        fake = group2
    else:
        fake = group3
    return fake


def comparison(coinsList):
    cnt = 0
    currList = coinsList
    while len(currList) > 1:
        group1, group2, group3 = splitCoins(currList)
        currList = find(group1, group2, group3)
        cnt += 1
    fake = currList[0]
    print(coinsList.index(fake)+1)

coinsList = [10, 10, 10, 10, 11, 10, 10, 10, 10]
comparison(coinsList)