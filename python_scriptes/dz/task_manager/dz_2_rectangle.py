"""
Написать класс для описания плоской геометрической фигуры:
Rectangle (Прямоугольник.) длина и
ширина прямоугольника (length, width)

Методы для операций с данными:
Нахождения периметра (perimeter)\n,
площади (square),
 изменения размеров (change_params(length, width)),
 печати данных (print_params).

 !! perimeter и square должны возвращать вычисленные значения !!
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def perimeter(self):
        print(2 * self.length + 2 * self.width)
        return (2 * self.length + 2 * self.width)


    def square(self):
        print(self.length  * self.length)
        return (self.length  * self.length)


    def change_params(self, length, width):
        self.length = length
        self.width = width


    def print_params(self):
        print((self.perimeter(), self.square()))
        return (self.perimeter(), self.square())


rectangle = Rectangle(10, 20)
rectangle.print_params()
rectangle.change_params(20, 30)
rectangle.print_params()
