'''Выведите первый, последний и средний элемент списка. Количество элементов в списке будет больше 3. Пример: get_first_midd_last_list_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]) Вывод: [1, 5, 9]'''

'''
def get_first_midd_last_list_elements(test_list):
    test_list = [1,2,3,4,5,6,7,8,9]

    print(min(test_list))
    print(int(sum(test_list)/len(test_list)))
    print(max(test_list))
get_first_midd_last_list_elements([1,2,3,4,5,6,7,8,9])i
'''

test_list = [1,2,3,4,5,6,7,8,9]
print(test_list[0])
print(int(sum(test_list)/len(test_list)))
print(test_list[-1])

