'''Инструкции
Необходимо написать программу, которая проверяет произведение первого и второго числа равна ли третьему числу Пример: 1) multiply(5, 5, 25) Программа должна вернуть "Верно." 2) multiply(5, 5, 30) Программа должна вернуть "Неверно. Правильный ответ 25!"
'''

def multiply(a, b, answer):
    if (a*b) == answer:
        return "Верно."
    else:
        return f"Неверно. Правильный ответ {a*b}!"