'''Выбор дома будет осуществляться по району, стоимостью, строительных материалов и состоянию, размером участка. Дом нужен в районе чон-арык, байтик или ортосай Если дом из кирпича и участок до 4 соток, то стоимость должна быть не более 50000. Если дом из пескоблока и участок до 5 соток, то стоимость должна быть не более 45000. Входные параметры: ["чон-арык", "байтик ", "ортосай", "кирпич", "пескоблок"]'''

'''Функция должна возвращать TRUE или FALSE в зависимости от вводимых данных. Вы должны правильно соблюсти все условия выбора.
Условные выражения
'''

def choose_house(district, material, area, price):
    if district == "байтик" or district  == "ортосай" or  district == "чон-арык":
        if material == "кирпич" and  area  <= 4 and price <= 50000 :
            return True
        elif material == "пескоблок" and  area  <= 5 and price <= 45000 :
            return True
        else:
            return False

'''
material = str(input())
area = int(input())
price = int(input())

if district == "Байтик" or district  == "Орто сай" or  district == "чон-арык":
    if material == 'Кирпич' and  area  <= 4 and price <= 50000 :
        print(True)
    elif material == 'пескоблок' and  area  <= 5 and price <= 45000 :
        print(True)
    else:
        print(False)
'''
