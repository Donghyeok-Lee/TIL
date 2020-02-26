# 단어2

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
