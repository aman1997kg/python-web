'''Выведите первый, последний и средний элемент списка. Количество элементов в списке будет больше 3. Пример: get_first_midd_last_list_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]) Вывод: [1, 5, 9]'''

'''
def get_first_midd_last_list_elements(test_list):
    test_list = [1,2,3,4,5,6,7,8,9]

    print(min(test_list))
    print(int(sum(test_list)/len(test_list)))
    print(max(test_list))
get_first_midd_last_list_elements([1,2,3,4,5,6,7,8,9])i
'''
'''
test_list = [0,2,3,4,8,6,7,8,10]
print(test_list[0])
print(test_list/len(test_list))
print(test_list[-1])
'''
from statistics import mean
test_list = [0,2,3,4,8,6,7,8,10]

print(test_list[0])
test =len(test_list)/3 
print(test_list[-1])
print(test)
