'''
Даны списки: Нужно вернуть список, который состоит из элементов, общих для этих двух списков. Пример: list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] same_lists_elements_check(list_1, list_2) Вывод: [1, 2, 3, 5, 8, 13]

'''

c = []
def same_lists_elements_check(first_list, second_list):
    for i in first_list:
        for j in second_list:
            if i == j:
                c.append(i)
            break
return c



