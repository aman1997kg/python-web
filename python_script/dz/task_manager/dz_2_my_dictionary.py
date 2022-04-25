'''
""" Напишите функцию, которая принимает три словаря и с помощью цикла for собирает их в новый словарь. Функция должна вернуть этот новый словарь. Подсказка: Для удобства итерации, словари можно записать в кортеж (dict_one, dict_two, dict_three) Также учтите, что ключи в разных словарях НЕ ДОЛЖНЫ совпадать!!! """
'''
dict_one = (1,3,4)
dict_two = (3,5,6)
dict_three = (4,5,6)

def get_dict(dict_one, dict_two, dict_three):
    new_dict = dict()

    for i in (dict_one, dict_two, dict_three):
        new_dict.update(i)
    return new_dict()
print(get_dict(dict_one, dict_two, dict_three))
