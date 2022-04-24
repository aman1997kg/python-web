""" Создайте класс Person с атрибутами: имя(name) и возраст(age)
 строки типа. Создайте метод display(),
 который отображает имя и возраст объекта,
  созданного с помощью класса Person.
  Создайте дочерний класс Student, который наследуется от класса Person
  и также имеет атрибут раздела (название, которое нужно применить department).
  Создайте метод displayStudent(), который отображает имя, возраст и раздел объекта,
  созданного с помощью класса Student.
  Создайте объект Student через создание экземпляра в классе Student,
   а затем протестируйте метод displayStudent"""

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    def display(self):
        # return self.name, self.age
        print(f'{self.name} {self.age}')


class Student(Person):

    def __init__(self, name, age, department=None):
        super().__init__(name, age)
        self.department = department


    def displayStudent(self):
        print(f'{self.name} {self.age} {self.department}')
        # return self.name, self.aige, self.department

person = Person('Aman', 25)
person.display()
print(person.__dict__)


student = Student('Azamat', 25, 'IT_Technology')
student.displayStudent()
print(student.__dict__)












#
#
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         return self.name, self.age
#
#     def do_nothing(self):
#         print(f"{self.name} эч жерде иштебейт!")
#
# class Employeer(Person):
#
#     def work(self, department=None):
#         self.department = department
#         print(f'{self.name} "{self.department}" иштейт!')
#
# class Student(Person):
#
#     def __init__(self, name, age, study_in=None, department=None):
#         super().__init__(name, age)
#         self.study_in = study_in
#         self.department = department
#
#
#     def displayStudent(self):
#         return self.name, self.age,  self.study_in
#
#     # def all_info(self):
#     #     print(f'''
#     #     Аты : {self.name}
#     #     Жашы: {self.age}
#     #     {self.study_in}: окуйт жана сабактан тышкары бош убактысында {self.department} болуп иштейт.''')
#
#     def study(self):
#         print(f'{self.name}  окуйт!')
#
#     def work(self):
#         print(f'{self.name} "{self.department}" иштейт!')
#
#
#
#
#     def act(person):
#         if isinstance(person, Student):
#             person.study()
#         elif isinstance(person, Employeer):
#             person.work()
#         elif isinstance(person, Person):
#             person.do_nothing()
#
#
# # person = Person('Aman', 25)
# # print(person.display())
# # Asan = Person('Azat', 26)
# # print(Asan.display())
# # Asan.do_nothing()
#
#
# aman = Employeer('Аman', 23)
# aman.work('Китепканада')
#
# print(aman.__dict__)
#
#
# bolot = Person('Azamat', 25)
# bolot.do_nothing()
# print(bolot.__dict__)
#
#
# saltanat = Student('Saltanat', 26, 'SchoolIT')
# print(saltanat.display())
# print(saltanat.displayStudent())
# print(saltanat.all_info())
#
#
#


