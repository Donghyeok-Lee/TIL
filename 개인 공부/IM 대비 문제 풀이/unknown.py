"""
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

"""