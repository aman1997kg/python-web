"""
Напишите программу, которая рассчитает сколько бензина израсходовал транспорт в среднем на 100 км. формула: Расход = литры израсходованные на дорогу / пройденный путь * 100 Возвратите расход

"""

def get_fuel_consumption(length_km, litres):
    rashod_benzin = litres/length_km*100
    print(rashod_benzin)

litres = int(input('Сколько литров расходован на дарогу: '))
length_km = int(input('Сколько км пройден:' ))

get_fuel_consumption(length_km, litres)
