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
    name = None
    age = None


    def display(self):
        return self.name, self.age

class Student(Person):
    def work(self):
        self.deportament = None

    def DisplayStudent(self):
        return self.name, self.age, self.deportament

student = Student()
student.display()