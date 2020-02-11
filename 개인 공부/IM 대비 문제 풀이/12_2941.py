# 크로아티아

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