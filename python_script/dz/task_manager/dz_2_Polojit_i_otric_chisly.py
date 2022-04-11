""" Напишите функцию, которая принимает список, содержащий положительные и отрицательные числа. Функция должна вернуть кортеж из двух списков, один из которых содержит только положительные числа, а другой отрицательные. """

#def separate_numbers(numbers_list):
numbers = '1,-1,2,-2,-3,-5,-6,7,8,9'
otr = []
pol = []
new_list = [int(l) for l in numbers.split(',')]
for all_list in  new_list:
    if all_list > 0:
        otr = otr.append(all_list)
    else:
        pol = pol.append(all_list)
print(otr, pol)
