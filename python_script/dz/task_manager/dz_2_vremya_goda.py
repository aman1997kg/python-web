""" Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, к которому этот месяц принадлежит (зима, весна, лето или осень). """

months = ['4'] #['1','2','3','4','5','6','7','8','9','10','11','12']

spring = dict()
summer = dict()
autumn = dict()
winter = dict()

spring['3'] = 'Март'
spring['4'] = 'Апрель'
spring['5'] = 'Май'

summer['6'] = 'Июнь'
summer['7'] = 'Июль'
summer['8'] = 'Август'

autumn['9'] = 'Сентябрь'
autumn['10'] = 'Октябрь'
autumn['11'] = 'Ноябрь'

winter['12'] = 'Декабрь'
winter['1'] = 'Январь'
winter['2'] = 'Февраль'


for month in months:
    if month in spring:
        print('Весна')
    else:
        if month in summer:
            print('Лето')
        else:
            if month in autumn:
                print('Осень')
            else:
                if month in winter:
                    print('Зима')
                else:
                    print('Не правильный ввод!')


'''

def season(month):
    
    spring = dict()
    summer = dict()
    autumn = dict()
    winter = dict()
 
    spring['3'] = 'Март'
    spring['4'] = 'Апрель'
    spring['5'] = 'Май'
 
    summer['6'] = 'Июнь'
    summer['7'] = 'Июль'
    summer['8'] = 'Август'
     
    autumn['9'] = 'Сентябрь'
    autumn['10'] = 'Октябрь'
    autumn['11'] = 'Ноябрь'
     
    winter['12'] = 'Декабрь'
    winter['1'] = 'Январь'
    winter['2'] = 'Февраль'
    
    for month in months:
        if month in spring:
            return 'весна'
        else:
            if month in summer:
                return 'лето'
            else:
                if month in autumn:
                    return 'осень'
                else:
                    if month in winter:
                        return 'зима'
                    else:
                        return 'Не правильный ввод!'
'''
