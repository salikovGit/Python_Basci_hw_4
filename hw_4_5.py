'''
5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в
отдельных текстовых файлах.
файл первый:
AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
файл второй:
сжатый текст.
'''


def text_compressor(origin_string):
    count = 1
    compressed_text = ''
    for i in range(1, len(origin_string)):
        if origin_string[i] == origin_string[i-1]:
            count += 1
        else:
            compressed_text += str(count) + origin_string[i-1]
            count = 1
    return compressed_text


def text_recovery(compressed_string):
    count = ''
    result = ''
    for symbol in compressed_string:
        if symbol.isdigit():
            count += symbol
        else:
            result += symbol * int(count)
            count = ''
    return result


def compress_file(original_file, result_file='compressed_text.txt'):
    with open(original_file, encoding='utf-8') as file:
        origin_text = file.read()
        result = text_compressor(origin_text)
    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(result)
    print(result)


compress_file('original_task5.txt')
print(text_recovery('12A11B10C6D5E4F1G1 1p1y1t1h1o1n1 1i1s1 1s7o1 1c7o'))
