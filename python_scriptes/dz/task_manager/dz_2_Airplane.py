'''
Создайте новый класс Airplane.
Создайте следующие характеристики (полей) объекта:
● make (марка)
● model
● year
● max_speed
● odometer
● is_flying и методы имитирующих поведение самолета
take off (взлет),
fly (летать),
land приземление).

Метод take off должен изменить is_flying на True,
а land на False. По умолчанию поле is_flying = False.
Метод fly должен принимать расстояние полета и изменять
показания одометра (километраж). Создайте 1 объект класса и
используйте все методы класса. Ps.
Значение одометра можно устанавливать при создании объекта.
'''

class Airplane:

    def __init__(self, make, model, year, max_speed, odometer, is_flying=False):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = is_flying


    def take_off(self):
        self.is_flying = True


    def fly(self, m):
        self.odometer += m


    def land(self):
        self.is_flying = False



