'''
"""Создайте класс Student, конструктор которого имеет параметры
name, lastname, department, year_of_entrance.
Добавьте метод get_student_info, который возвращает имя, фамилию,
год поступления и факультет в отформатированном виде:
“Вася Иванов поступил в 2017 г. на факультет: программирование.'"""
'''


class Student:
    def __init__(self, name, lastname, department, year_of_enterance):
        self.__name = name
        self.__lastname = lastname
        self.__department = department
        self.__year_of_enterance = year_of_enterance

        self.get_info()

    def get_info(self):
        self.__name = str(input())
        self.__lastname = str(input())
        self.__department = str(input())
        self.__year_of_enterance = int(input())


    #@classmethod
    def get_student_info(self):
        return f"{self.__name} {self.__lastname} поступил в {self.__year_of_enterance} г. на факультет: {self.__department}."

st = Student('Вася', 'Иванова','программирование', 2017)
# st.get_student_info()
print(st.get_student_info())