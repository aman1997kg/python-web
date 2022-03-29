'''
Хочу лексус или тойоту от 2004 года с пробегом не более 150000, белую или серую, с левым рулем и максимум 2 хозяина. Со стоимостью не больше 10000, или такую же , но с пробегом 200000 и более, но с ценой меньше 8000


Функция должна возвращать True или False в зависимости от вводимых данных. Вы должны правильно соблюсти все условия выбора машины. left_wheel будет типа bool Марки машины пишите на англ: LEXUS, TOYOTA Цвет машины: white, grey


УЧТИТЕ: Данные в model могут быть разного регистра!!!!!!!!!!!!!!!!!!!!! (Lexus, LeXus, Toyota, ToYOTA и тд), а вы будете их сравнивать с LEXUS и TOYOTA!
Условные выражения

'''



def func(model, year, usage, color, owner, price, left_wheel):
    if (model.upper() == 'LEXUS' or model.upper() == 'TOYOTA') and usage <= 150000 and left_wheel == True and year >= 2004 and owner <= 2 and price <= 10000 and (color == 'white' or color == 'grey'):
        return True
    if (model.upper() == 'LEXUS' or model.upper() == 'TOYOTA') and usage > 200000 and left_wheel == True and year >= 2004 and owner <= 2 and price <= 8000 and (color == 'white' or color == 'grey'):
        return True
    
    return False


r = func('toyota',2007,150000,'серый',1,10000,True)

print(r)
