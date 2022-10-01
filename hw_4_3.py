'''
3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов,
которые имеют средний балл более «4».
Пример:
Волков Андрей 5
Наталья Тарасова 5
Фредди Меркури 3
Денис Байцуров 4

Программа выдаст:
ВОЛКОВ АНДРЕЙ 5
НАТАЛЬЯ ТАРАСОВА 5
Фредди Меркури 3
Денис Байцуров 4
'''


def upper_case(file_name):
    text = ''
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            a = line.split()
            if int(a[-1]) == 5:
                a = ' '.join(a)
                text = text + a.upper() + '\n'
            else:
                a = ' '.join(a)
                text = text + a + '\n'
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(text)


upper_case('names.txt')
