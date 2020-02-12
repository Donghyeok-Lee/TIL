# N-queen이라서 빨리 해야징

# Step1. 책을 통해 백트래킹 예시 확인하기

def noConflicts(board, current, qindex, n): # 새로 추가된 퀸이 기존 퀸과 충돌하는지 검사
    for j in range(current):        # qindex의 행에 다른 퀸이 있는지 검사
        if board[qindex][j] == 1:
            return False

    k = 1
    while qindex - k >= 0 and current - k >= 0:  # 대각선 1 검사
        if board[qindex - k][current - k] == 1:
            return False
        k += 1

    k = 1
    while qindex + k < n and current - k < n:   # 대각선 2 검사
        if board[qindex + k][current - k] == 1:
            return False
        k += 1

    return True    # 행, 대각선 검사에서 return을 안 만날 경우 True를 리턴

def fourQueen(n=4):
    board = [[0, 0, 0, 0], [0, 0, 0, 0],
             [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(n):
        board[i][0] = 1     # 각 열에는 1개의 퀸만 배치함
        for j in range(n):  # 첫 퀸은 충돌이 날 리 없으니까 다음으로 ㄱㄱ
            board[j][1] = 1     # 두번째 퀸 배치
            if noConflicts(board, 1, j, n): # 기존 퀸과 충돌 확인
                for k in range(n):  # 충돌 X면 다음 퀸 배치, 반복
                    board[k][2] = 1
                    if noConflicts(board, 2, k, n):
                        for m in range(n):
                            board[m][3] = 1
                            if noConflicts(board, 3, m, n):
                                for l in range(n):
                                    print(board[l])
                                print()
                            board[m][3] = 0
                    board[k][2] = 0
            board[j][1] = 0
        board[i][0] = 0
    return

fourQueen()

# 현재는 4개의 퀸을 놓는 경우만 확인


# 3개의 경우엔?
def threeQueen(n=3):
    board = [[0,0,0], [0,0,0], [0,0,0]]
    for i in range(n):
        board[i][0] = 1
        for j in range(n):
            board[j][1] = 1
            if noConflicts(board, 1, j, n):
                for k in range(n):
                    board[k][2] = 1
                    if noConflicts(board, 2, k, n):
                        for l in range(n):
                            print(board[l])
                        print()
                    board[k][2] = 0
            board[j][1] = 0
        board[i][0] = 0
    return

threeQueen()    # 아 맞다 3개면 없지.........

# 5개면?

def fiveQueen(n=5):
    board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    for i in range(n):
        board[i][0] = 1     # 각 열에는 1개의 퀸만 배치함
        for j in range(n):  # 첫 퀸은 충돌이 날 리 없으니까 다음으로 ㄱㄱ
            board[j][1] = 1     # 두번째 퀸 배치
            if noConflicts(board, 1, j, n): # 기존 퀸과 충돌 확인
                for k in range(n):  # 충돌 X면 다음 퀸 배치, 반복
                    board[k][2] = 1
                    if noConflicts(board, 2, k, n):
                        for m in range(n):
                            board[m][3] = 1
                            if noConflicts(board, 3, m, n):
                                for l in range(n):
                                    board[l][4] = 1
                                    if noConflicts(board, 4, l, n):
                                        for p in range(n):
                                            print(board[p])
                                        print()
                                    board[l][4] = 0
                            board[m][3] = 0
                    board[k][2] = 0
            board[j][1] = 0
        board[i][0] = 0
    return

fiveQueen()

# 수가 많아질 수록 너무 ...좀 그런데?

def noConflicts2(board, current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        if (current - i == abs(board[current] - board[i])):
            return False
    return True