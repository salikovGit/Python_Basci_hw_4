'''
1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N = 20 -> [2,5]
N = 30 -> [2, 3, 5]
'''


def get_simple_multipliers(n):
    simple_multipliers = []
    multiplier = 2
    while multiplier <= n:
        if n % multiplier == 0:
            simple_multipliers.append(multiplier)
            n = n // multiplier
            multiplier = 2
        else:
            multiplier += 1
    return list(set(simple_multipliers))

print(get_simple_multipliers(20))
print(get_simple_multipliers(30))
