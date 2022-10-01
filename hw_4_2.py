'''
2 - Задайте последовательность чисел.
Напишите программу, которая выведет список исключит повторы элементов исходной последовательности.
Не использовать множества.
[1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]
'''


def get_uniques(some_list):
    result = []
    for el in some_list:
        if el not in result:
            result.append(el)
        else:
            continue
    return result


print(get_uniques([1,1,1,1,2,2,2,3,3,3,4]))
