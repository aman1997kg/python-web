def coordinates_check(x1, x2, y1, y2):
    x1 = int(input())
    x2 = int(input())
    y1 = int(input())
    y2 = int(input())

    if x1*x2>0 and y1*y2>0:
        print("Да")
    else:
        print("Нет")
        
coordinates_check(3, 3, 5, 1)

