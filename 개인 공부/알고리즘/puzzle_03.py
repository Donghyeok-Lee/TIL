"""
# 다른 사람의 마음 읽기
# 카드 마술! 5장의 카드 중 4장을 공개하고, 마지막 1장을 찾아내는 퍼즐


# Step1. 스스로 해보기
shape_list = ['D', 'H', 'C', 'S'] # 다이아몬드, 하트, 클로버, 스페이드
number_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K'] # 10의 경우 0으로 표시
card_list = ['H0', 'D9', 'H3', 'SQ', 'DJ']
test_list = [[], [], [], []] # 각 카드의 존재 여부 확인용

for card in card_list:
    test_list[shape_list.index(card[0])].append(card)
    if len(test_list[shape_list.index(card[0])]) >= 2:
        card_test_list = test_list[shape_list.index(card[0])]
        break

test = card_test_list[0]
finding = card_test_list[1]
test_num = number_list.index(test[1])
cnt = 0

while number_list[test_num] != finding[1]:
    test_num += 1
    cnt += 1
    if test_num > 12:
        test_num = 0

if cnt <= 6:
    secret_card = card_test_list[1]
    first_card = card_test_list[0]
else:
    secret_card = card_test_list[0]
    first_card = card_test_list[1]
    cnt = 13 - cnt

public_card_list = []
for card in card_list:
    if card not in card_test_list:
        public_card_list.append(card)

max_idx = min_idx = 0
for i in range(len(public_card_list)):
    if number_list.index(public_card_list[i][1]) > number_list.index(public_card_list[max_idx][1]):
        max_idx = i
    if number_list.index(public_card_list[i][1]) < number_list.index(public_card_list[min_idx][1]):
        min_idx = i

idx_list = [0, 1, 2]
idx_list.remove(max_idx)
idx_list.remove(min_idx)
mid_idx = idx_list[0]

result_list = ((), (min_idx, mid_idx, max_idx),
               (min_idx, max_idx, mid_idx),
               (mid_idx, min_idx, max_idx),
               (mid_idx, max_idx, min_idx),
               (max_idx, min_idx, mid_idx),
               (max_idx, mid_idx, min_idx)
                )
result_text = first_card
for i in range(3):
    result_text += public_card_list[result_list[cnt][i]]
print(result_text)


# 아 이거 아닌것 같은데...

"""

# Step2. 책 읽기

deck = ['A_C', 'A_D', 'A_H', 'A_S', '2_C', '2_D', '2_H', '2_S',
'3_C', '3_D', '3_H', '3_S', '4_C', '4_D', '4_H', '4_S',
'5_C', '5_D', '5_H', '5_S', '6_C', '6_D', '6_H', '6_S',
'7_C', '7_D', '7_H', '7_S', '8_C', '8_D', '8_H', '8_S',
'9_C', '9_D', '9_H', '9_S', '10_C', '10_D', '10_H', '10_S',
'J_C', 'J_D', 'J_H', 'J_S', 'Q_C', 'Q_D', 'Q_H', 'Q_S',
'K_C', 'K_D', 'K_H', 'K_S',]


def AssistantOrdersCards():
    print('Cards are character strings as shown below.')
    print('Ordering is :', deck)
    cards, cind, cardsuits, cnumbers = [], [], [], []
    numsuits = [0, 0, 0, 0]
    for i in range(5):
        print('Please give card', i+1, end = ' ')
        card = input('in above format : ')
        cards.append(card)
        n = deck.index(card)
        cind.append(n)
        cardsuits.append(n % 4)
        cnumbers.append(n // 4)
        numsuits[n % 4] += 1
        if numsuits[n % 4] > 1:
            pairsuit = n % 4
    cardh = []
    for i in range(5):
        if cardsuits[i] == pairsuit:
            cardh.append(i)
    hidden, other, encode = \
        outputFirstCard(cnumbers, cardh, cards)
    remindices =[]
    for i in range(5):
        if i != hidden and i != other:
            remindices.append(cind[i])
    sortList(remindices)
    outputNext3Cards(encode, remindices)
    return

def outputFirstCard(ns, oneTwo, cards):
    encode = (ns[oneTwo[0]] - ns[oneTwo[1]]) % 13
    if encode > 0 and encode <= 6:
        hidden = oneTwo[0]
        other = oneTwo[1]
    else:
        hidden = oneTwo[1]
        other = oneTwo[0]
        encode = (ns[oneTwo[1]] - ns[oneTwo[0]]) % 13
    print('First card is :', cards[other])
    return hidden, other, encode

def outputNext3Cards(code, ind):
    if code == 1:
        s, t, f = ind[0], ind[1], ind[2]
    elif code == 2:
        s, t, f = ind[0], ind[2], ind[1]
    elif code == 3:
        s, t, f = ind[1], ind[0], ind[2]
    elif code == 4:
        s, t, f = ind[1], ind[2], ind[0]
    elif code == 5:
        s, t, f = ind[2], ind[0], ind[1]
    else:
        s, t, f = ind[2], ind[1], ind[0]
    print('Second card is :', deck[s])
    print('Third card is :', deck[t])
    print('Fourth card is :', deck[f])

def sortList(tlist):
    for ind in range(len(tlist)-1):
        iSm = ind
        for i in range(ind, len(tlist)):
            if tlist[iSm] > tlist[i]:
                iSm = i
        tlist[ind], tlist[iSm] = tlist[iSm], tlist[ind]

AssistantOrdersCards()
