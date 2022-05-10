""" Написать функцию season, принимающую 1 аргумент —
номер месяца (от 1 до 12), и возвращающую время года,
к которому этот месяц принадлежит (зима, весна, лето или осень). """


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

    if str(month) in spring:
        return 'весна'
    else:
        if str(month) in summer:
            return 'лето'
        else:
            if str(month) in autumn:
               return 'осень'
            else:
                if str(month) in winter:
                   return 'зима'
                else:
                   return 'Не правильный ввод!'

print(season(7))
