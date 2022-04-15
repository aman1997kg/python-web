'''
# Банкомат # Напишите код банкомата, который принимает цифру, выдает деньги с номиналом 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1. Пример: 3009 будет передан функции и она вернут -> [2000, 1000, 5, 3, 1] 
Первым должны быть купюры с большим номиналом.

'''
'''
s = 4331 
bankomat = []


banknot = {5000: 0, 2000: 0, 1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 3: 0, 1: 0}


for b in banknot:
    if s == 0:
        break
    while b  > 0 and s >= b:
        banknot[b] - 1
        banknot[b] += 1
        s -= b
        if s == 0:
            for key, value in banknot.items():
                if value > 0:
                    bankomat.append(key)
print(bankomat)
'''
amount = 3009
bankomat = []
def get_current(amount):
    for b in amount:
        if amount == 0:
            break
    while b  > 0 and amount >= b:
        amount[b] - 1
        amount[b] += 1
        s -= b
        if s == 0:
            for key, value in amount.items():
                if value > 0:
                    bankomat.append(key)
return bankomat

print(get_corrent())
