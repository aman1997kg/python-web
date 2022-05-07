from models import *
import datetime

with db:
    #создание БД
    #db.create_tables([Inner_flights,Outer_flights])

    #Ввод данных на таблицу / Ленивый бд
    '''Inner_flights(
        from_region='Osh',
        to_destination='Bishkek',
        #quantity=50,
        company='Pegasus'
    ).save()
    '''

    ''' 
    Inner_flights.create(
        from_region='Jalal-Abad',
        to_destination='Bishkek',
        quantity=10,
        company='Air-Manas'
    )
    '''

    #'''
    data = [
        {'from_region':'Bishkek',
        'to_destionation':'Naryn',
        'company':'Pegasus',
        'quantity':70},

        {'from_region': 'Balykchy',
         'to_destionation': 'Osh',
         'company': 'Air Manas',
         'quantity': 80},
    ]

    Inner_flights.insert_many(data).execute()
    #'''

    #Вывод данных из БД

    '''
    #i = Inner_flights.select()
    #print(i)
    '''

    #Ввод данных на таблицу Outer_flight
    '''
    data = [
        {'from_country': 'Ош',
         'to_country': 'Баткен',
         'company':'Pegasus',
         'flight_type': Outer_flights.TYPE[0],
         'neighbors': 129},

        {'from_country': 'ЖалалАбад',
         'to_country': 'Каракол',
         'company': 'Pegasus',
         'flight_type': Outer_flights.TYPE[1],
         'neighbors': 103},
    ]

    Outer_flights.insert_many(data).execute()
    
    '''

    # Вывести из БД из таблицы Inner_flight | SELECT запросы
    '''
    # Вывести все записи из таблицы  Inner_flight

    in_fl = Inner_flights.select()
    for i_f in in_fl:
        print(
            i_f.id,
            i_f.from_region,
            i_f.to_destionation,
            i_f.quantity,
            i_f.company
        )

    '''

    # Вывести из БД те которые меньше 5
    '''
    in_fl = Inner_flights.select().where(Inner_flights.id < 5)
    for i_f in in_fl:
        print(
            i_f.id,
            i_f.from_region,
            i_f.to_destionation,
            i_f.quantity,
            i_f.company
        )
    
    #i_f = [(i_f.id, i_f.from_region, i_f.company, i_f.quantity, i_f.to_destionation) for i_f in in_fl]
    #print(i_f)
        
    '''

    # Вывести те строки где страна прилета Ош или (|) Бишкек
    '''
    in_fl = Inner_flights.select().where((Inner_flights.to_destionation == 'Karakol') | (Inner_flights.to_destionation == 'Osh'))
    for i_f in in_fl:
        print(
            i_f.id,
            i_f.from_region,
            i_f.to_destionation,
            i_f.quantity,
            i_f.company
            )
    '''

    # Вывести те строки где кол-во пассажиров больше 20;
    '''
    in_fl = Inner_flights.select().where(Inner_flights.quantity > 20)
    for i_f in in_fl:
        print(
            i_f.id,
            i_f.from_region,
            i_f.to_destionation,
            i_f.quantity,
            i_f.company
        )
    '''

    # Вывести из таблицы outter_flights выведите только имя компании которые занимаются перевозкой
    '''
    ou_fl = Outer_flights.select().where(Outer_flights.flight_type == 'Жүк ташуучу')
    for o_f in ou_fl:
        print(
            o_f.company,
        )
        
    '''

    #


