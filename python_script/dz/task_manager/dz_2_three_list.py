'''
Напишите функцию, которая принимает три словаря и
с помощью цикла for собирает их в новый словарь.
Функция должна вернуть этот новый словарь.
Подсказка: Для удобства итерации,
словари можно записать в кортеж (dict_one, dict_two, dict_three)
Также учтите, что ключи в разных словарях НЕ ДОЛЖНЫ совпадать!!!
'''


new_dict = {}

dict_one = {'color': 'blue',  'green',  'yellow'}
dict_two = {'weight': '12', 'weight': '2','weight': '333'}
dict_three = {'price': '100', 'price': '130','price': '130'}

a_dict = (dict_one, dict_two, dict_three)

def get_dict(dict_one, dict_two, dict_three):


print(get_dict(dict_one, dict_two, dict_three))
