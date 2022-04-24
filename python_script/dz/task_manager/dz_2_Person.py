""" Создать класс Person a) поля full_name, age, address (age по умолчанию 18)
б) метод talk(), в которых просто вывести на консоль сообщение -"Такой-то Person говорит".
Метод move() будет менять его адрес в) Настроить метод __str__
(Сделать отображение всех полей объекта) по очередности full_name, age, address Пример:
"Balanchaev Balancha, 18, gagarina 66" """


class Person:

    default_age = 18
    default_address = None
    default_full_name = None

    def __init__(self, full_name = default_full_name, age = default_age, address = default_address):
        self.full_name = full_name
        self.age = age
        self.address = address


    def talk(self):
        return f"Такой-то {self.full_name} говорит"


    def move(self, value):
        self.address = value


    def __str__(self):
        print(self.full_name, self.age, self.address)


person = Person('Aman Bolotbek uulu', '25', 'Amanbekov 8')
print(person.talk())
person.move('at-bashy')
print(person.__str__())





