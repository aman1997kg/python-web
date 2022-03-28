'''
Даны три числа. Найти максимальное и минимальное из них. Пример: find_max_and_min_digits(2, 3, 4) Вывод: (4, 2)

'''


def find_max_and_min_digits(a,b,c):
    if a > b:
        if a > c:
            print(a)
    else:
        print(c)
    else:
        if b > c:
        print(b)
    else:
        print(c)

'''d = list()
d.append(a)
d.append(b)
d.append(c)

print(max(d))
print(min(d))
'''

'''def find_max_and_min_digits(a, b, c):
    print(min(a,b,c))
    print(max(a,b,c))
find_max_and_min_digits(1,3,4)'''
