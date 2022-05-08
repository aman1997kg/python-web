'''
Создайте класс Phone,
который содержит атрибуты
number,
model и
weight.

Создайте три экземпляра этого класса.
Выведите на консоль значения их атрибутов.
Создать метод sendMessage.
Данный метод принимает на вход номера телефонов,
которым будет отправлено сообщение.
Метод выводит на консоль номера этих телефонов.
'''


class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight


    def info(self):
        print(self.number, self.model, self.weight)
        return self.number, self.model, self.weight


    def sendMessage(self, number):
        print(number)
        return number

phone = Phone('07001*999*7', 'MI', 200)

#phone.info()
#phone.SendMessage('070088888')