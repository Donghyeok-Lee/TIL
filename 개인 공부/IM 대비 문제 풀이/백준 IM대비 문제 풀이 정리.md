# 백준 IM대비 문제 풀이 정리



## 1592. 영식이와 친구들

> 영식이와 친구들이 원형으로 모여서 시계방향으로 1부터 N까지 적혀있는 자리에 앉는다. 영식이와 친구들은 공 던지는 게임을 하기로 했다. 게임의 규칙은 다음과 같다.
>
> 일단 1번 자리에 앉은 사람이 공을 받는다. 그리고 나서 공을 다른 사람에게 던진다. 다시 공을 받은 사람은 다시 공을 던지고, 이를 계속 반복한다. 한 사람이 공을 M번 받았으면 게임은 끝난다. (지금 받은 공도 포함하여 센다.) 공을 M번보다 적게 받은 사람이 공을 던질 때, 현재 공을 받은 횟수가 홀수번이면 자기의 현재 위치에서 시계 방향으로 L번째 있는 사람에게, 짝수번이면 자기의 현재 위치에서 반시계 방향으로 L번째 있는 사람에게 공을 던진다.
>
> 공을 총 몇 번 던지는지 구하는 프로그램을 작성하시오.
>
>
> ### 입력
>
> 첫째 줄에 N, M, L이 입력으로 들어온다. N은 3보다 크거나 같고, 1,000보다 작거나 같은 자연수이고, M은 1,000보다 작거나 같은 자연수이다. L은 N-1보다 작거나 같은 자연수이다.
>
>
> ### 출력
>
> 첫째 줄에 공을 몇 번 던지는지 횟수를 출력한다.

| 예제 입력 | 예제 출력 |
| :-------: | :-------: |
|   5 3 2   |    10     |



```python
N, M, L = map(int, input().split())

num_list = [0] * N		# N명의 사람의 공 받은 횟수 Count list

num_list[0] = 1			# 첫번째 사람이 공을 받음
cnt = 0				    # 전체 공을 던진 횟수
i = temp_i = 0			# 현재 공의 위치
while True:
    if num_list[i] % 2: # 자신이 받은 횟수가 홀수이면 시계방향
        temp_i = i + L
    else:			   # 아니면 반시계방향
        temp_i = i - L

    if temp_i < 0:         # 리스트 범위로 맞추기
        i = temp_i + N
    elif temp_i >= N:
        i = temp_i - N
    else:
        i = temp_i
    num_list[i] += 1   # 받은 횟수 +1
    cnt += 1           # 공 던진 횟수 +1

    if num_list[i] == M: # 받은 횟수가 M이 되면 종료
        break

print(cnt)
```





## 2999. 비밀 이메일

> 매일 밤, 정인이는 상근이에게 이메일을 보낸다. 정인이는 자신의 이메일이 해킹당할 수도 있다는 생각에, 내용을 항상 암호화해서 보낸다.
>
> 정인이가 사용하는 암호 알고리즘은 다음과 같다. 정인이가 보내는 메시지는 총 N글자이다.
>
> 먼저, 정인이는 R<=C이고, R*C=N인 R과 C를 고른다. 만약, 그러한 경우가 여러 개일 경우, R이 큰 값을 선택한다.
>
> 그 다음, 행이 R개고, 열이 C개인 행렬을 만든다.
>
> 이제 메시지를 행렬에 옮긴다. 첫 번째 행의 첫 번째 열부터 C번째 열까지 메시지를 순서대로 옮긴 뒤, 남은 메시지는 두 번째 행, 세 번째 행,... R번째 행에 첫 번째 행을 채운 방법과 동일한 순서대로 옮긴다.
>
> 행렬에 모두 메시지를 옮겼다면, 이 것을 첫 번째 열의 첫 번째 행부터 R번째 행까지 차례대로 읽으면서 다시 받아 적는다. 그 다음에, 두 번째 열, 세 번째 열,..., C번째 열에 쓰여 있는 문자를 첫 번째 열을 읽은 방법과 동일하게 받아적는다.
>
> 상근이는 매일 밤 정인이의 메시지를 해독하는데 지쳤다. 정인이의 암호 이메일이 주어졌을 때, 이를 해독하는 프로그램을 작성하시오.
>
> ### 입력
>
> 첫째 줄에 상근이가 받은 메시지가 주어진다. 이 메시지는 알파벳 소문자로만 이루어져 있고, 최대 100글자이다.
>
> ### 출력
>
> 첫째 줄에 상근이가 받은 메시지를 해독한 메시지를 출력한다.

|    예제 입력     |    예제 출력     |
| :--------------: | :--------------: |
| boudonuimilcbsai | bombonisuuladici |



```python
text = input()
N = len(text)
R = C = 0
result = ''
for i in range(1, int(N**0.5)+1):
    if not N % i:
        R = i

C = N // R

data_list = [[''] * C for _ in range(R)]
num = 0
for i in range(C):
    for j in range(R):
        data_list[j][i] = text[num]
        num += 1

for i in range(R):
    result += ''.join(data_list[i])

print(result)
```



## 3985. 롤 케이크

> 인기 티비 프로그램 "나는 요리사 인가?"의 새 시즌이 시작한다. 이번 시즌은 기네스북에 등재될 만한 음식을 만드는 것을 목표로 진행한다.
>
> 첫 번째 에피소드에 출연하는 요리사는 전설의 요리사 김상근이고, 길이 L미터의 롤 케이크를 만들 것이다.
>
> 상근은 몇 시간동안 집중해서 케이크를 만들었고, 이제 스튜디오의 방청객 N명에게 케이크를 나누어 주려고 한다.
>
> 상근이는 롤 케이크를 펼쳐서 1미터 단위로 잘라 놓았다. 가장 왼쪽 조각이 1번, 오른쪽 조각이 L번 조각이다. 방청객은 1번부터 N번까지 번호가 매겨져 있다. 각 방청객은 종이에 자신이 원하는 조각을 적어서 낸다. 이때, 두 숫자 P와 K를 적어서 내며, P번 조각부터 K번 조각을 원한다는 뜻이다.
>
> 프로그램의 진행자 고창영은 1번 방청객의 종이부터 순서대로 펼쳐서 해당하는 조각에 그 사람의 번호를 적을 것이다. 이때, 이미 번호가 적혀있는 조각은 번호를 적지 못하고 넘어간다. 이런 방식을 이용해서 방청객에게 조각을 주다보니, 자신이 원래 원했던 조각을 받지 못하는 경우가 생길 수 있다.
>
> 아래 그림은 이 문제의 예제를 나타낸 것이다.
>
> ![img](https://www.acmicpc.net/upload/images/roll.png)
>
> 가장 많은 케이크 조각을 받을 것으로 기대한 방청객의 번호와 실제로 가장 많은 케이크 조각을 받는 방청객의 번호를 구하는 프로그램을 작성하시오.
>
> ### 입력
>
> 첫째 줄에 롤 케이크의 길이 L (1 ≤ L ≤ 1000)이 주어진다. 둘째 줄에는 방청객의 수 N (1 ≤ N ≤ 1000)이 주어진다. 다음 N개 줄에는 각 방청객 i가 종이에 적어낸 숫자 Pi와 Ki가 주어진다. (1 ≤ Pi ≤ Ki ≤ L, i = 1..N)
>
> ### 출력
>
> 첫째 줄에 가장 많은 조각을 받을 것으로 기대하고 있던 방청객의 번호를 출력한다.
>
> 둘째 줄에 실제로 가장 많은 조각을 받은 방청객의 번호를 출력한다.
>
> 가장 많은 조각을 받도록 예상되는 방청객이 여러 명인 경우에는 번호가 작은 사람을 출력한다.

|              예제 입력               | 예제 출력 |
| :----------------------------------: | :-------: |
| 10<br />3<br />2 4<br />7 8<br />6 9 | 3<br />1  |

```python
L = int(input())
N = int(input())
test_list = [list(map(int, input().split())) for _ in range(N)]

data_list = [0] * L

max_cnt = max_exp = 0
max_per = max_exp_per = 1
for i in range(N):
    temp_cnt = 0
    for j in range(test_list[i][0]-1, test_list[i][1]):
        if not data_list[j]:
            data_list[j] = i + 1
            temp_cnt += 1
    if max_cnt < temp_cnt:
        max_cnt = temp_cnt
        max_per = i + 1
    if max_exp < test_list[i][1] - test_list[i][0]:
        max_exp = test_list[i][1] - test_list[i][0]
        max_exp_per = i + 1

print(max_exp_per)
print(max_per)
```





## 11399. ATM

> 인하은행에는 ATM이 1대밖에 없다. 지금 이 ATM앞에 N명의 사람들이 줄을 서있다. 사람은 1번부터 N번까지 번호가 매겨져 있으며, i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.
>
> 사람들이 줄을 서는 순서에 따라서, 돈을 인출하는데 필요한 시간의 합이 달라지게 된다. 예를 들어, 총 5명이 있고, P1 = 3, P2 = 1, P3 = 4, P4 = 3, P5 = 2 인 경우를 생각해보자. [1, 2, 3, 4, 5] 순서로 줄을 선다면, 1번 사람은 3분만에 돈을 뽑을 수 있다. 2번 사람은 1번 사람이 돈을 뽑을 때 까지 기다려야 하기 때문에, 3+1 = 4분이 걸리게 된다. 3번 사람은 1번, 2번 사람이 돈을 뽑을 때까지 기다려야 하기 때문에, 총 3+1+4 = 8분이 필요하게 된다. 4번 사람은 3+1+4+3 = 11분, 5번 사람은 3+1+4+3+2 = 13분이 걸리게 된다. 이 경우에 각 사람이 돈을 인출하는데 필요한 시간의 합은 3+4+8+11+13 = 39분이 된다.
>
> 줄을 [2, 5, 1, 4, 3] 순서로 줄을 서면, 2번 사람은 1분만에, 5번 사람은 1+2 = 3분, 1번 사람은 1+2+3 = 6분, 4번 사람은 1+2+3+3 = 9분, 3번 사람은 1+2+3+3+4 = 13분이 걸리게 된다. 각 사람이 돈을 인출하는데 필요한 시간의 합은 1+3+6+9+13 = 32분이다. 이 방법보다 더 필요한 시간의 합을 최소로 만들 수는 없다.
>
> 줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.
>
> ## 입력
>
> 첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)
>
> ## 출력
>
> 첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.

|    예제 입력     | 예제 출력 |
| :--------------: | :-------: |
| 5<br />3 1 4 3 2 |    32     |



```python
N = int(input())

Pi = list(map(int, input().split()))

for i in range(N):
    min_idx = i
    for j in range(i+1, N):
        if Pi[min_idx] > Pi[j]:
            min_idx = j
    Pi[min_idx], Pi[i] = Pi[i], Pi[min_idx]

total = 0
for i in range(N):
    for j in range(i+1):
        total += Pi[j]

print(total)
```







## 8958. OX 퀴즈

> "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
>
> "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
>
> OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
>
> ## 입력
>
> 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.
>
> ## 출력
>
> 각 테스트 케이스마다 점수를 출력한다.

|                          예제 입력                           |            예제 출력             |
| :----------------------------------------------------------: | :------------------------------: |
| 5<br />OOXXOXXOOO<br />OOXXOOXXOO<br />OXOXOXOXOXOXOX<br />OOOOOOOOOO<br />OOOOXOOOOXOOOOX | 10<br />9<br />7<br />55<br />30 |



```python
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
```





## 2563. 색종이

> 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.
>
> ![img](https://www.acmicpc.net/upload/images/IcZB4bH8h7wwEY6z7qyoqNXkMsh.png)
>
> 예를 들어 흰색 도화지 위에 세 장의 검은색 색종이를 그림과 같은 모양으로 붙였다면 검은색 영역의 넓이는 260이 된다.
>
> ## 입력
>
> 첫째 줄에 색종이의 수가 주어진다. 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다. 색종이를 붙인 위치는 두 개의 자연수로 주어지는데 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다. 색종이의 수는 100 이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다
>
> ## 출력
>
> 첫째 줄에 색종이가 붙은 검은 영역의 넓이를 출력한다.

| 예제 입력                     | 예제 출력 |
| ----------------------------- | --------- |
| 3<br />3 7<br />15 7<br />5 2 | 260       |



```python
color_list = [[0] * 100 for _ in range(100)]
N = int(input())
xy_list = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(xy_list[k][0], xy_list[k][0] + 10):
        for j in range(xy_list[k][1], xy_list[k][1] + 10):
            color_list[i][j] = 1

cnt = 0

for i in range(100):
    for j in range(100):
        if color_list[i][j] == 1:
            cnt += 1

print(cnt)
```





## 2567. 색종이 - 2

> 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 둘레의 길이를 구하는 프로그램을 작성하시오.
>
> 예를 들어 흰색 도화지 위에 네 장의 검은색 색종이를 <그림 1>과 같은 모양으로 붙였다면 검은색 영역의 둘레는 96 이 된다.
>
> ![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/upload/images/Jhmd3swxUQJ8nlBxoP.jpg)
>
> ## 입력
>
> 첫째 줄에 색종이의 수가 주어진다. 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다. 색종이를 붙인 위치는 두 개의 자연수로 주어지는데 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다. 색종이의 수는 100이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다. 
>
> ## 출력
>
> 첫째 줄에 색종이가 붙은 검은 영역의 둘레의 길이를 출력한다.

| 예제 입력                                | 예제 출력 |
| ---------------------------------------- | --------- |
| 4<br />3 7<br />5 2<br />15 7<br />13 14 | 96        |



```python
color_list = [[0] * 100 for _ in range(100)]
N = int(input())
xy_list = [list(map(int, input().split())) for _ in range(N)]


for k in range(N):
    for i in range(xy_list[k][0], xy_list[k][0] + 10):
        for j in range(xy_list[k][1], xy_list[k][1] + 10):
            color_list[i][j] = 1

dir_list = ((-1,0), (1,0), (0,-1), (0,1))


cnt = 0

for i in range(100):
    for j in range(100):
        if color_list[i][j] == 1:
            for l in range(4):
                temp_i = i + dir_list[l][0]
                temp_j = j + dir_list[l][1]
                if temp_i >= 0 and temp_j >= 0 and temp_i < 100 and temp_j < 100:
                    if color_list[temp_i][temp_j] == 1:
                        cnt -= 1

print(cnt)
```





## 17413. 단어 뒤집기2

> 문자열 S가 주어졌을 때, 이 문자열에서 단어만 뒤집으려고 한다.
>
> 먼저, 문자열 S는 아래와과 같은 규칙을 지킨다.
>
> 1. 알파벳 소문자('`a`'-'`z`'), 숫자('`0`'-'`9`'), 공백('` `'), 특수 문자('`<`', '`>`')로만 이루어져 있다.
> 2. 문자열의 시작과 끝은 공백이 아니다.
> 3. '`<`'와 '`>`'가 문자열에 있는 경우 번갈아가면서 등장하며, '`<`'이 먼저 등장한다. 또, 두 문자의 개수는 같다.
>
> 태그는 '`<`'로 시작해서 '`>`'로 끝나는 길이가 3 이상인 부분 문자열이고, '`<`'와 '`>`' 사이에는 알파벳 소문자와 공백만 있다. 단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열이고, 연속하는 두 단어는 공백 하나로 구분한다. 태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.
>
> ## 입력
>
> 첫째 줄에 문자열 S가 주어진다. S의 길이는 100,000 이하이다.
>
> ## 출력
>
> 첫째 줄에 문자열 S의 단어를 뒤집어서 출력한다.

| 예제 입력                                               | 예제 출력                                               |
| ------------------------------------------------------- | ------------------------------------------------------- |
| baekjoon online judge                                   | noojkeab enilno egduj                                   |
| <open>tag<close>                                        | <open>gat<close>                                        |
| <ab cd>ef gh<ij kl>                                     | <ab cd>fe hg<ij kl>                                     |
| one1 two2 three3 4fourr 5five 6six                      | 1eno 2owt 3eerht rruof4 evif5 xis6                      |
| <int><max>2147483647<long long><max>9223372036854775807 | <int><max>7463847412<long long><max>7085774586302733229 |
| <problem>17413<is hardest>problem ever<end>             | <problem>31471<is hardest>melborp reve<end>             |
| <   space   >space space space<    spa   c e>           | <   space   >ecaps ecaps ecaps<    spa   c e>           |



```python
text = input()
N = len(text)
idx_list = []
result = []
temp_result = []
test_list = []
i = 0
while i < N:
    if text[i] == '<':
        while text[i] != '>':
            temp_result.append(text[i])
            i += 1
        temp_result.append(text[i])
        result.append(''.join(temp_result))
        temp_result = []
        i += 1
    else:
        while i < N and text[i] != ' ' and text[i] != '<':
            temp_result.append(text[i])
            i += 1
        test_list.append(''.join(temp_result[::-1]))
        temp_result = []
        if i >= N or text[i] == '<':
            result.append(' '.join(test_list))
            test_list = []
        else:
            i += 1

print(''.join(result))
```





## 10817. 세 수

> 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 
>
> ## 입력
>
> 첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)
>
> ## 출력
>
> 두 번째로 큰 정수를 출력한다.

| 예제 입력 | 예제 출력 |
| --------- | --------- |
| 20 30 10  | 20        |
| 30 30 10  | 30        |
| 40 40 40  | 40        |
| 20 10 10  | 10        |



```python
test = list(map(int, input().split()))

test.remove(max(test))
test.remove(min(test))

print(test[0])
```





## 9655. 돌 게임

> 돌 게임은 두 명이서 즐기는 재밌는 게임이다.
>
> 탁자 위에 돌 N개가 있다. 상근이와 창영이는 턴을 번갈아가면서 돌을 가져가며, 돌은 1개 또는 3개 가져갈 수 있다. 마지막 돌을 가져가는 사람이 게임을 이기게 된다.
>
> 두 사람이 완벽하게 게임을 했을 때, 이기는 사람을 구하는 프로그램을 작성하시오. 게임은 상근이가 먼저 시작한다.
>
> ## 입력
>
> 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 1000)
>
> ## 출력
>
> 상근이가 게임을 이기면 SK를, 창영이가 게임을 이기면 CY을 출력한다.

| 예제 입력 | 예제 출력 |
| --------- | --------- |
| 5         | SK        |



```python
N = int(input())

if N % 2:
    print('SK')
else:
    print('CY')
```



## 3052. 나머지

> 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 
>
> 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
>
> ## 입력
>
> 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.
>
> ## 출력
>
> 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.

```python
test_list = []

for _ in range(10):
    num = int(input())
    if num % 42 not in test_list:
        test_list.append(num % 42)

print(len(test_list))
```





## 2941. 크로아티아 알파벳

> 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.
>
> | 크로아티아 알파벳 | 변경 |
> | :---------------- | :--- |
> | č                 | c=   |
> | ć                 | c-   |
> | dž                | dz=  |
> | đ                 | d-   |
> | lj                | lj   |
> | nj                | nj   |
> | š                 | s=   |
> | ž                 | z=   |
>
> 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
>
> dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.
>
> ## 입력
>
> 첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
>
> 단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.
>
> ## 출력
>
> 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

| 예제 입력 | 예제 출력 |
| --------- | --------- |
| ljes=njak | 6         |
| ddz=z=    | 3         |
| nljj      | 3         |
| c=c=      | 2         |



```python
data_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt_list = [0] * 8
number_list = [1, 1, 2, 1, 1, 1, 1, 1]

text = input()

for char in data_list:
    cnt_list[data_list.index(char)] = text.count(char)

cnt_list[7] -= cnt_list[2]

result = len(text)
for i in range(8):
    result -= cnt_list[i] * number_list[i]

print(result)
```





## 2699. 직사각형 네개의 합집합의 면적 구하기

> 평면에 네 개의 직사각형이 놓여 있는데 그 밑변은 모두 가로축에 평행하다. 이 네 개의 직사각형들은 서로 떨어져 있을 수도 있고, 겹쳐 있을 수도 있고, 하나가 다른 하나를 포함할 수도 있으며, 변이나 꼭짓점이 겹칠 수도 있다.
>
> 이 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오.
>
> ![img](https://www.acmicpc.net/upload/images/8vR77Ew2O2PqvZ1lER716.png)
>
> ## 입력
>
> 입력은 네 줄이며, 각 줄은 직사각형의 위치를 나타내는 네 개의 정수로 주어진다. 첫 번째와 두 번째의 정수는 사각형의 왼쪽 아래 꼭짓점의 x좌표, y좌표이고 세 번째와 네 번째의 정수는 사각형의 오른쪽 위 꼭짓점의 x좌표, y좌표이다. 모든 x좌표와 y좌표는 1이상이고 100이하인 정수이다.
>
> ## 출력
>
> 첫 줄에 네개의 직사각형이 차지하는 면적을 출력한다.

| 예제 입력                                      | 예제 출력 |
| ---------------------------------------------- | --------- |
| 1 2 4 4<br />2 3 5 7<br />3 1 6 5<br />7 3 8 6 | 26        |



```python
num_list = [[0] * 100 for _ in range(100)]
xy_list = [list(map(int, input().split())) for _ in range(4)]

for k in range(4):
    for i in range(xy_list[k][0], xy_list[k][2]):
        for j in range(xy_list[k][1], xy_list[k][3]):
            num_list[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if num_list[i][j] == 1:
            cnt += 1

print(cnt)
```





## 2635 . 수 이어가기

> 다음과 같은 규칙에 따라 수들을 만들려고 한다.
>
> 1. 첫 번째 수로 양의 정수가 주어진다.
> 2. 두 번째 수는 양의 정수 중에서 하나를 선택한다.
> 3. 세 번째부터 이후에 나오는 모든 수는 앞의 앞의 수에서 앞의 수를 빼서 만든다. 예를 들어, 세 번째 수는 첫 번째 수에서 두 번째 수를 뺀 것이고, 네 번째 수는 두 번째 수에서 세 번째 수를 뺀 것이다.
> 4. 음의 정수가 만들어지면, 이 음의 정수를 버리고 더 이상 수를 만들지 않는다.
>
> 첫 번째 수로 100이 주어질 때, 두 번째 수로 60을 선택하여 위의 규칙으로 수들을 만들면 7개의 수들 100, 60, 40, 20, 20 , 0, 20이 만들어진다. 그리고 두 번째 수로 62를 선택하여 위의 규칙으로 수들을 만들면 8개의 수들 100, 62, 38, 24, 14, 10, 4, 6이 만들어진다. 위의 예에서 알 수 있듯이, 첫 번째 수가 같더라도 두 번째 수에 따라서 만들어지는 수들의 개수가 다를 수 있다.
>
> 입력으로 첫 번째 수가 주어질 때, 이 수에서 시작하여 위의 규칙으로 만들어지는 최대 개수의 수들을 구하는 프로그램을 작성하시오. 최대 개수의 수들이 여러 개일 때, 그중 하나의 수들만 출력하면 된다.
>
> ## 입력
>
> 첫 번째 수가 주어진다. 이 수는 30,000 보다 같거나 작은 양의 정수이다.
>
> ## 출력
>
> 첫 번째 줄에는 입력된 첫 번째 수로 시작하여 위의 규칙에 따라 만들 수 있는 수들의 최대 개수를 출력한다.
>
> 둘째 줄에 그 최대 개수의 수들을 차례대로 출력한다. 이들 수 사이에는 빈칸을 하나씩 둔다.

| 예제 입력 | 예제 출력                     |
| --------- | ----------------------------- |
| 100       | 8<br />100 62 38 24 14 10 4 6 |



```python
N = int(input())
test = []
test.append(N)
max_len = 0
for i in range(N + 1):
    test.append(i)
    while test[-1] >= 0:
        test.append(test[-2] - test[-1])
    test.pop(-1)
    if max_len < len(test):
        max_len = len(test)
        max_list = test
    test = [N]

print(max_len)
print(' '.join(map(str, max_list)))
```





## 1244. 스위치 켜고 끄기

> 1부터 연속적으로 번호가 붙어있는 스위치들이 있다. 스위치는 켜져 있거나 꺼져있는 상태이다. <그림 1>에 스위치 8개의 상태가 표시되어 있다. ‘1’은 스위치가 켜져 있음을, ‘0’은 꺼져 있음을 나타낸다. 그리고 학생 몇 명을 뽑아서, 학생들에게 1 이상이고 스위치 개수 이하인 자연수를 하나씩 나누어주었다. 학생들은 자신의 성별과 받은 수에 따라 아래와 같은 방식으로 스위치를 조작하게 된다.
>
> 스위치 번호 ① ② ③ ④ ⑤ ⑥ ⑦ ⑧
> 스위치 상태  0 1  0 1  0  0  0 1
> <그림 1>
>
> 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다. 즉, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다. <그림 1>과 같은 상태에서 남학생이 3을 받았다면, 이 학생은 <그림 2>와 같이 3번, 6번 스위치의 상태를 바꾼다.
>
> 스위치 번호 ① ② ③ ④ ⑤ ⑥ ⑦ ⑧
> 스위치 상태  0 1  1 1  0  1  0 1
> <그림 2>
>
> 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다. 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.
>
> 예를 들어 <그림 2>에서 여학생이 3을 받았다면, 3번 스위치를 중심으로 2번, 4번 스위치의 상태가 같고 1번, 5번 스위치의 상태가 같으므로, <그림 3>과 같이 1번부터 5번까지 스위치의 상태를 모두 바꾼다. 만약 <그림 2>에서 여학생이 4를 받았다면, 3번, 5번 스위치의 상태가 서로 다르므로 4번 스위치의 상태만 바꾼다.
>
> 스위치 번호 ① ② ③ ④ ⑤ ⑥ ⑦ ⑧
> 스위치 상태  1  0 0  0 1  1  0 1
> <그림 3>
>
> 입력으로 스위치들의 처음 상태가 주어지고, 각 학생의 성별과 받은 수가 주어진다. 학생들은 입력되는 순서대로 자기의 성별과 받은 수에 따라 스위치의 상태를 바꾸었을 때, 스위치들의 마지막 상태를 출력하는 프로그램을 작성하시오.
>
> ## 입력
>
> 첫째 줄에는 스위치 개수가 주어진다. 스위치 개수는 100 이하인 양의 정수이다. 둘째 줄에는 각 스위치의 상태가 주어진다. 켜져 있으면 1, 꺼져있으면 0이라고 표시하고 사이에 빈칸이 하나씩 있다. 셋째 줄에는 학생수가 주어진다. 학생수는 100 이하인 양의 정수이다. 넷째 줄부터 마지막 줄까지 한 줄에 한 학생의 성별, 학생이 받은 수가 주어진다. 남학생은 1로, 여학생은 2로 표시하고, 학생이 받은 수는 스위치 개수 이하인 양의 정수이다. 학생의 성별과 받은 수 사이에 빈칸이 하나씩 있다.
>
> ## 출력
>
> 스위치의 상태를 1번 스위치에서 시작하여 마지막 스위치까지 한 줄에 20개씩 출력한다. 예를 들어 21번 스위치가 있다면 이 스위치의 상태는 둘째 줄 맨 앞에 출력한다. 켜진 스위치는 1, 꺼진 스위치는 0으로 표시하고, 스위치 상태 사이에 빈칸을 하나씩 둔다.

| 예제 입력                                       | 예제 출력       |
| ----------------------------------------------- | --------------- |
| 8<br />0 1 0 1 0 0 0 1<br />2<br />1 3<br />2 3 | 1 0 0 0 1 1 0 1 |



```python
N = int(input())
data_list = [0] + list(map(int, input().split()))

M = int(input())
input_list = [list(map(int, input().split())) for _ in range(M)]

for k in range(M):
    if input_list[k][0] == 1:
        i = input_list[k][1]
        while i < N + 1:
            data_list[i] += 1
            if data_list[i] == 2:
                data_list[i] = 0
            i += input_list[k][1]
    else:
        i = input_list[k][1]
        data_list[i] += 1
        if data_list[i] == 2:
            data_list[i] = 0
        j = 1
        while i - j > 0 and i + j < N + 1 and data_list[i + j] == data_list[i - j]:
            data_list[i + j] += 1
            if data_list[i + j] == 2:
                data_list[i + j] = 0
                data_list[i - j] = 0
            else:
                data_list[i - j] += 1
            j += 1

data_list.pop(0)

while data_list:
    result = []
    if len(data_list) > 20:
        for _ in range(20):
            result.append(data_list.pop(0))
        print(' '.join(map(str, result)))
    else:
        print(' '.join(map(str, data_list)))
        data_list.clear()
```





## 2628. 종이 자르기

> 아래 <그림 1>과 같이 직사각형 모양의 종이가 있다. 이 종이는 가로방향과 세로 방향으로 1㎝마다 점선이 그어져 있다. 가로 점선은 위에서 아래로 1번부터 차례로 번호가 붙어 있고, 세로 점선은 왼쪽에서 오른쪽으로 번호가 붙어 있다.
>
> ![img](https://www.acmicpc.net/upload/images/sjp8TTetlSbGSiPQxxi3e3vO5JNp7x.gif)
>
> 점선을 따라 이 종이를 칼로 자르려고 한다. 가로 점선을 따라 자르는 경우는 종이의 왼쪽 끝에서 오른쪽 끝까지, 세로 점선인 경우는 위쪽 끝에서 아래쪽 끝까지 한 번에 자른다. 예를 들어, <그림 1>의 가로 길이 10㎝이고 세로 길이 8㎝인 종이를 3번 가로 점선, 4번 세로 점선, 그리고 2번 가로 점선을 따라 자르면 <그림 2>와 같이 여러 개의 종이 조각으로 나뉘게 된다. 이때 가장 큰 종이 조각의 넓이는 30㎠이다.
>
> 입력으로 종이의 가로 세로 길이, 그리고 잘라야할 점선들이 주어질 때, 가장 큰 종이 조각의 넓이가 몇 ㎠인지를 구하는 프로그램을 작성하시오.
>
> ## 입력
>
> 첫줄에는 종이의 가로와 세로의 길이가 차례로 자연수로 주어진다. 가로와 세로의 길이는 최대 100㎝이다. 둘째 줄에는 칼로 잘라야하는 점선의 개수가 주어진다. 셋째 줄부터 마지막 줄까지 한 줄에 점선이 하나씩 아래와 같은 방법으로 입력된다. 가로로 자르는 점선은 0과 점선 번호가 차례로 주어지고, 세로로 자르는 점선은 1과 점선 번호가 주어진다. 입력되는 두 숫자 사이에는 빈 칸이 하나씩 있다.
>
> ## 출력
>
> 첫째 줄에 가장 큰 종이 조각의 넓이를 출력한다. 단, 넓이의 단위는 출력하지 않는다.

| 예제 입력                              | 예제 출력 |
| -------------------------------------- | --------- |
| 10 8<br />3<br />0 3<br />1 4<br />0 2 | 30        |



```python
N, M = map(int, input().split())
n = int(input())
input_list = [list(map(int, input().split())) for _ in range(n)]
row_list = []
col_list = []

for case in input_list:
    if case[0] == 0:
        row_list.append(case[1])
    else:
        col_list.append(case[1])

row_list = [0] + sorted(row_list) + [M]
col_list = [0] + sorted(col_list) + [N]

result = []

for i in range(len(row_list)-1):
    for j in range(len(col_list)-1):
        total = 0
        for k in range(row_list[i], row_list[i+1]):
            for l in range(col_list[j], col_list[j+1]):
                total += 1
        result.append(total)

print(max(result))
```





## 2309. 일곱 난쟁이

> 왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.
>
> 아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.
>
> 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.
>
> ## 입력
>
> 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.
>
> ## 출력
>
> 일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.

```python
height_list = []
for _ in range(9):
    height_list.append(int(input()))

total = sum(height_list)

for i in range(1<<9):
    temp_list = []
    for j in range(9):
        if i & (1<<j):
            temp_list.append(height_list[j])
    if len(temp_list) == 2 and sum(temp_list) == total - 100:
        result_list = temp_list


for height in result_list:
    height_list.remove(height)

height_list.sort()

for height in height_list:
    print(height)
```







## 2072. 오목

```python
num_list = [[0] * 21 for _ in range(21)]

dir_list = ((1, 0), (0, 1), (1, 1), (1, -1))

N = int(input())

for tc in range(1, N+1):
    i, j = map(int, input().split())
    if tc % 2:
        num_list[i][j] = 1
    else:
        num_list[i][j] = 2
    result = []
    for k in range(4):
        test = ''
        for d in range(-30, 30):
            temp_i = i + dir_list[k][0] * d
            temp_j = j + dir_list[k][1] * d
            if temp_i >= 0 and temp_j >=0 and temp_i < 21 and temp_j < 21:
                test += str(num_list[temp_i][temp_j])
        result.append(test)

    flag = 0
    for i in range(len(result)):
        if '11111' in result[i]:
            if'111111' not in result[i]:
                print(tc)
                flag = 1
                break
        if '22222' in result[i]:
            if '222222' not in result[i]:
                print(tc)
                flag = 1
                break
    if flag:
        break
if not flag:
    print(-1)
```

```python
def f(i, j):
    global flag
    c = bd[i][j]
    v = [0] * 8
    for k in range(8):
        ni = i + di[k][0]
        nj = j + di[k][1]
        cnt = 0
        while bd[ni][nj] == c:
            ni = ni + di[k][0]
            nj = nj + di[k][1]
            cnt += 1
        v[k] = cnt
    for i in range(4):
        if v[i] + v[i+4] == 4:
            flag = False
            return 1
    else:
        return 0


bd = [[0] * 21 for _ in range(21)]

di = ((1, 0), (0, 1), (1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1), (-1, 1))

N = int(input())
case = [list(map(int, input().split())) for _ in range(N)]
flag = True
for t in range(N):
    i = case[t][0]
    j = case[t][1]
    bd[i][j] = t % 2 + 1
    if f(i, j):
        print(t+1)
        break
if flag:
    print(-1)
```

