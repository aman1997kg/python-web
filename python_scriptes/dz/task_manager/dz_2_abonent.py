'''
 Создайте класс Abonent Идентификационный номер(id_number),
 Полное ФИО(full_name), Адрес(address),
 Номер кредитной карточки (card_number),
 Дебет (debet), Кредит(credite),
 Время междугородных и городских переговоров (call_time) в минутах;

 Методы: вывод информации (ФИО, номер, номер кредитной карточки) (display_info).
 ФИО, номер кредитной карты, номер)

 Классметод (get_overused): получает список объектов класса
 Abonent и ворвращает новый список из тех, кто превысил норму по времени
 на городских переговорах (15min), также выводит информацию об абоненте.

 Классметод (sort_abo): получает список объектов класса Abonent  (параметр abos),
 и возвращает отсортированный список абонентов по алфовиту
 '''



class Abonent:

     def __init__(self, id_number, full_name, address, card_number, debet, credite, call_time):
        self.id_number = id_number
        self.full_name = full_name
        self.address = address
        self.card_number = card_number
        self.debet = debet
        self.credite = credite
        self.call_time = call_time


     def call_times(self):
        return self.call_time


     def display_info(self):
         return f'{self.full_name} {self.card_number} {self.id_number}'



     def get_overused(self):
         pass


     


abonent = Abonent(1, "Aman Bolotbek uulu", '8-mart', 145665465, 1456465, 165465, 4)

print(abonent.display_info())


