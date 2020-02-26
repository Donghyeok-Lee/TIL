# OX

T = int(input())

for _ in range(T):
    text = input()
    N = len(text)

    total = 0
    score = 1
    for i in range(N):
        if text[i] == 'O':
            total += score
            score += 1
        else:
            score = 1

    print(total)