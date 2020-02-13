"""

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


def confirm(board, current, qindex, n): # 현재 보드, 현재 퀸을 놓은 위치(열)
    for i in range(current):
        if board[i][qindex] == 1:
            return False
    k = 1
    while qindex - k >= 0 and current - k >= 0:
        if board[current - k][qindex - k] == 1:
            return False
        k += 1
    k = 1
    while qindex + k < n and current - k < n:  # 대각선 2 검사
        if board[current - k][qindex + k] == 1:
            return False
        k += 1
    return True  # 행, 대각선 검사에서 return을 안 만날 경우 True를 리턴

#
def fourQueen(n=4):
    board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    for i in range(n):
        board[0][i] = 1     # 각 행에는 1개의 퀸만 배치함
        for j in range(n):  # 첫 퀸은 충돌이 날 리 없으니까 다음으로 ㄱㄱ
            board[1][j] = 1     # 두번째 퀸 배치
            if confirm(board, 1, j, n): # 기존 퀸과 충돌 확인
                for k in range(n):  # 충돌 X면 다음 퀸 배치, 반복
                    board[2][k] = 1
                    if confirm(board, 2, k, n):
                        for m in range(n):
                            board[3][m] = 1
                            if confirm(board, 3, m, n):
                                for l in range(5):
                                    print(board[l])
                                print()
                            board[3][m] = 0
                    board[2][k] = 0
            board[1][j] = 0
        board[0][i] = 0
    return

fourQueen()

def fiveQueen(n=5):
    board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    for i in range(n):
        board[0][i] = 1     # 각 행에는 1개의 퀸만 배치함
        for j in range(n):  # 첫 퀸은 충돌이 날 리 없으니까 다음으로 ㄱㄱ
            board[1][j] = 1     # 두번째 퀸 배치
            if confirm(board, 1, j, n): # 기존 퀸과 충돌 확인
                for k in range(n):  # 충돌 X면 다음 퀸 배치, 반복
                    board[2][k] = 1
                    if confirm(board, 2, k, n):
                        for m in range(n):
                            board[3][m] = 1
                            if confirm(board, 3, m, n):
                                for p in range(n):
                                    board[4][p] = 1
                                    if confirm(board, 4, p, n):
                                        for l in range(5):
                                            print(board[l])
                                        print()
                                    board[4][p] = 0
                            board[3][m] = 0
                    board[2][k] = 0
            board[1][j] = 0
        board[0][i] = 0
    return

fiveQueen()


"""

# 재귀로 해보기!

def confirm(board, current, qindex, n):
    for i in range(current):                        # 내가 놓은 열에 다른 퀸이 있나요? - 위아래
        if board[i][qindex] == 1:
            return False
    k = 1
    while qindex - k >= 0 and current - k >= 0:     # 대각선 1에 퀸이 ..(중략)..
        if board[current - k][qindex - k] == 1:
            return False
        k += 1
    k = 1
    while qindex + k < n and current - k < n:     # 대각선 2에 퀸이 ..(중략)..
        if board[current - k][qindex + k] == 1:
            return False
        k += 1
    return True

def queen(n):
    global cnt
    if n == N:                          # n == N이면 모든 행에 퀸을 놓았습니다!
        cnt += 1                        # 숫자를 셉니다.
        return
    for i in range(N):
        board[n][i] = 1                 # n행 에 퀸을 놓는 행위
        if confirm(board, n, i, N):     # 만약 놓았는데, n행까지 충돌이 없다면
            queen(n+1)                  # n+1 행에 퀸 놓으러 감
        board[n][i] = 0                 # 뭐... 어떻게 되면 다시 n행에 놓은 퀸 회수함

T = int(input())

for t in range(T):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    cnt = 0
    queen(0)                            # 0행부터 퀸을 놓습니다.
    print('#{0} {1}'.format(t+1, cnt))