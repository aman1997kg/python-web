def get_fuel_consumption(length_km, litres):
    litres = int(input('Сколько литров расходован на дарогу: '))
    length_km = int(input('Сколько км пройден:' ))
    rashod_benzin = litres/length_km*100
    print(rashod_benzin)

