# 단어2

text = '<   space   >space space space<    spa   c e>'
N = len(text)
idx_list = []
result = []
temp_result = ''

i = 0
while i < N:
    if text[i] == '<':
        while text[i] != '>':
            temp_result += text[i]
            i += 1
        temp_result += text[i]
        result.append(temp_result)
        temp_result = ''
        i += 1
    else:
        while i < N and text[i] != ' ' and text[i] != '<':
            temp_result += text[i]
            i += 1
        result.append(temp_result[::-1])
        if i < N and text[i] == '<':
            temp_result = ''
            pass
        else:
            temp_result = ''
            i += 1

print(''.join(result))