""" Напишите функцию, которая принимает список, содержащий положительные и отрицательные числа. Функция должна вернуть кортеж из двух списков, один из которых содержит только положительные числа, а другой отрицательные. """
'''
def separate_numbers(numbers_list):
    pos = []
    neg = []

    for i in numbers_list:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
    return pos, neg

numbers_list = [1, 3, -1, -2, 4, -4]
print(separate_numbers(numbers_list))
'''

def separate_numbers(numbers_list):
    pos = [pos for pos in numbers_list if pos > 0]
    neg = [neg for neg in numbers_list if neg < 0]
    return pos, neg

numbers_list = [1, 3, -1, -2, 4, -4]

print(separate_numbers(numbers_list))
