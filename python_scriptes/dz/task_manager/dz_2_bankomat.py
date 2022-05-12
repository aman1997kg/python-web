"""
# Банкомат # Напишите код банкомата,
который принимает цифру, выдает деньги
с номиналом 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1.

Пример: get_current(259) => [200, 50, 5, 3, 1]

"""
<<<<<<< HEAD

def get_current(amount):
    banknota = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1]
    nominal = []

    while amount > 0:
            for  i in banknota:
                if amount >= i:
                    amount -= i
                    nominal.append(i)
                    break
    return nominal


=======
amount = 200
banknota = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1]
summ = 0
nominal = []
>>>>>>> 982585404d5c6c0194abdc0003fdcd07f6f68a78

while amount > 0:
    for  i in banknota:
        if amount >= i:
            amount -= i
            nominal.append(i)
            summ += 1
print(nominal)


