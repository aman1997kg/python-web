'''
Создайте класс Car.
Пропишите в конструкторе параметры make, model, year, odometer, fuel.
Пусть у показателя odometer будет первоначальное значение 0, а у fuel 70.

Добавьте метод drive, который будет принимать расстояние в км.
В самом начале проверьте, хватит ли вам бензина из расчета того,
что машина расходует 10 л / 100 км (1л - 10 км) .

Если его хватит на введенное расстояние,
то пусть этот метод добавляет эти километры к значению одометра,
но не напрямую, а с помощью приватного метода __add_distance.

Помимо этого пусть метод drive также отнимет потраченное количество
бензина с помощью приватного метода __subtract_fuel,
затем пусть распечатает на экран “Let’s drive!”.

Если же бензина не хватит, то распечатайте
“Need more fuel, please, fill more!”

Расcчитанное количество бензина нужно округлить
до ближайшего целого числа.
Пример, 13км -> 1.3л -> 1 л; 17км -> 1.7 л -> 2л￤
'''

class Car:
    def __init__(self, make, model, year, odometer=0, fuel=70):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        self.fuel = fuel


    def drive(self, km):
        fuel = km / 10
        if self.fuel >= fuel:
            self.__add_distance(km)
            self.__subtract_fuel(fuel)
            print('Let’s drive!')
        else:
            print('Need more fuel, please, fill more!')

    def __add_distance(self, km):
        self.odometer += round(km)

    def __subtract_fuel(self, fuel):
        self.fuel -= round(fuel)


car = Car('make', 'model', 2005, 0, 10)
car.drive(1.3)
print(car.__dict__)