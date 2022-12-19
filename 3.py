# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


def decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

with open('in_encode.txt','r') as file:
    a = file.read()
print (a)
b = encode(a)
print (b)
with open('encode.txt','w') as file:
    file.write(b)

with open('in_decode.txt','r') as file:
    a = file.read()
print (a)
b = decode(a)
print (b)
with open('decode.txt','w') as file:
    file.write(b)

    