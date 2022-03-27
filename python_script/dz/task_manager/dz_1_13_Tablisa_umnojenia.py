'''Инструкции
Необходимо написать программу, которая проверяет произведение первого и второго числа равна ли третьему числу Пример: 1) multiply(5, 5, 25) Программа должна вернуть "Верно." 2) multiply(5, 5, 30) Программа должна вернуть "Неверно. Правильный ответ 25!"
'''


def multiply(a, b, answer):
     a = int(input())
     b = int(input())
     anser = int(input())

     multiply = a * b

     if anser == multiply:
         return print('Верно.')
     else:
        return print(f'Неверно. Правильный ответ {multiply}')
multiply(5, 5, 25)
