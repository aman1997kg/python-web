months = ['8'] #['1','2','3','4','5','6','7','8','9','10','11','12']
#months = dict()


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
    if month == spring:
        print('Весна')
    elif month == summer:
        print('Весна')
    elif month == autumn:
        print('Осень')
    elif month == winter:
        print('Зима')
