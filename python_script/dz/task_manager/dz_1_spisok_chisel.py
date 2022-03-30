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
'''
import math
def get_first_midd_last_list_elements(test_list):
    first = test_list[0]
    midd = math.ceil(len(test_list)/2)
    last = test_list[-1]
    list_t = [first, midd, last]
    #return list_t 
    print(test_list.index(midd))

test_list = [1,2,3,4,5,6,7,8,9]
print(get_first_midd_last_list_elements(test_list))
'''

import math
def get_first_midd_last_list_elements(test_list):
    first = test_list[0]
    midd_c = math.ceil(len(test_list)/2)
    midd = test_list.index(midd_c)
    last = test_list[-1]
    list_t = [first, test_list[midd], last]
     #return list_t
    print(list_t)
test_list = [1,2,3,4,7,6,7,8,9]
get_first_midd_last_list_elements(test_list)
