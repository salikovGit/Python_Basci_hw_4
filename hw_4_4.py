'''
4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо.
При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо.
"вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
Сдвиг часто называют ключом шифрования.
Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ,
считывает текст и дешифровывает его.
'''


def caesar_cipher(text, key = 1):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    coded_text = ''
    for symbol in text:
        if symbol in alphabet:
            position = alphabet.index(symbol)
            if position + key >= len(alphabet):
                coded_text += alphabet[-len(alphabet) + position + key]
            else:
                coded_text += alphabet[position + key]
        else:
            coded_text += symbol
    with open('coded_text.txt', 'w', encoding='utf-8') as file:
        file.write(coded_text)
    #print(coded_text)


def decoder(key=1):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    coded_text = ''
    with open('coded_text.txt', 'r', encoding='utf-8') as file:
        coded_text = file.read() + '\n'
    for symbol in coded_text:
        if symbol in alphabet:
            position = alphabet.index(symbol)
            if position - key <= 0:
                coded_text += alphabet[key - position]
            else:
                coded_text += alphabet[position - key]
        else:
            coded_text += symbol
    print(coded_text)


caesar_cipher('привет, как дела?')
decoder()
