'''Ввести координаты. Вернуть четверть координатной плоскости, которой принадлежит точка.'''
'''
    if x>0 and y>0:
        return "1"
    elif x<0 and y>0:
        return "2"
    elif x<0 and y<0:
        return "3"
    elif x>0 and y<0:
        return "4"
'''

def determine_quarter_of_coordinate(x, y):
    x = int(input())
    y = int(input())

    if x>0 and y>0:
        print('I')
    elif x<0 and y>0:
        print('II')
    elif x<0 and y<0:
        print('III')
    elif x>0 and y<0:
        print('IV')
determine_quarter_of_coordinate(-5,-5)
