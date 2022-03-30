'''Наисать программу по выбору компьютера. Нужен компьютер от 4 до 8 GB оперативной памяти. Размер жесткого диска как минимум 256, если SSD. Если HDD, то как минимум 1 террабайт. Стоимость ноутбука не должна превышать 1000$. Состояние новый. Функция должна возвращать TRUE или FALSE в зависимости от вводимых данных. Вы должны правильно соблюсти все условия. HDD и SSD пишите как hdd, ssd Если состояние новый, то значение будет 1, Если старый, то 0 def choose_pc(ram, hdd, hdd_type, price, condition): ''' 

def choose_pc(ram, hdd, hdd_type, price, condition):
    if ram >= 4 or ram >= 8:
        if hdd_type == 'ssd' and hdd >= 256 or  hdd_type == 'hdd' and hdd >= 1000:
            if price <= 1000 and condition == 1:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
'''
ram = int(input())
hdd = int(input()) 
hdd_type = str(input()) 
price = int(input()) 
condition = int(input())

if ram >= 4 or ram >= 8:
    if hdd_type == 'ssd' and hdd >= 256 or  hdd_type == 'hdd' and hdd >= 1000:
        if price <= 1000 and condition == 1:
            print(True)
        else:
            print(False)
    else:
        print(False)
else:
    print(False)
'''
