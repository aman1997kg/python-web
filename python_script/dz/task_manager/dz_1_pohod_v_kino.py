'''
Жанр или ужасы, или детектив, или комедии. Время от 21, если билет стоит меньше 500, иначе билет дешевле 300.
Функция должна возвращать TRUE или FALSE в зависимости от вводимых данных. Вы должны правильно соблюсти все условия. Жанры пишите следующим образом: comedy, detective, horror
Условные выражения

def func(genre: str, time: int, price: float):
    if genre == "comedy" or genre == "detective" or genre == "horror":
        if time > 21 and price = 500 or time < 21 and price < 300:
            return True
        else:
            return False 
    else:
        return False
'''

genre = str(input())
time = int(input())
price = float(input())

if genre == "comedy" or genre == "detective" or genre == "horror":
    if time >= 21 and price <= 500 or time <= 21 and price <= 300:
        print(True)
    else:
        print(False)
else:
    print(False)
