'''
"""Создайте класс Student, конструктор которого имеет параметры
name, lastname, department, year_of_entrance.
Добавьте метод get_student_info, который возвращает имя, фамилию,
год поступления и факультет в отформатированном виде:
“Вася Иванов поступил в 2017 г. на факультет: программирование.'

class Student:
    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance


    def get_student_info(self):
        return f'{self.name} {self.lastname} поступил в {self.year_of_entrance} г. на факультет: {self.department}.'
"""
'''


class Student:
    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance

        self.get_info()
    def get_info(self):
        self.name = str(input())
        self.lastname = str(input())
        self.department = str(input())
        self.year_of_enterance = int(input())



    def get_student_info(self):
        return f'{self.name} {self.lastname} поступил в {self.year_of_entrance} г. на факультет: {self.department}.'



st = Student(name=None, lastname=None, year_of_entrance=None, department=None)

print(st.get_student_info())