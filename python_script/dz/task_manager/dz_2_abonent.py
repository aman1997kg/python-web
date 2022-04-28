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


    def get_overused()

abonent = Abonent(1, "Aman Bolotbek uulu", '8-mart', 145665465, 1456465, 165465, 4)

print(abonent.display_info())


     # def time(self):
     #     if self.call_time == 'Нет':
     #        return self.call_time
     #     str_date = self.call_time.split(":")
     #     str_date = str_date[0]
     #     return int(str_date)
     #
     #
     # @classmethod
     # def get_overuser(cls):
     #    all_obj_list = []
     #    user1 = Abonent("1", "Aman Bolotbek uulu", "Naryn", "41587978897", "5235324", "5457948273", "10:15")
     #    user2 = Abonent("2", "Bolotbek uulu Erkin", "Naryn", "43234224234", "43424243", "433423432", "11:10")
     #
     #    all_obj_list.append(user1)
     #    all_obj_list.append(user2)
     #
     #    for user in all_obj_list:
     #        try:
     #            user_time  = user.time()
     #            if user_time == "Нет":
     #                pass
     #            elif 0 < user_time <= 15:
     #                new_list = user.display_info()
     #                new_user_list = []
     #                new_user_list.append(new_list)
     #                return new_user_list
     #                print(new_user_list)
     #        except:
     #            print("\nПользователь указал время не правильно!")




     # def sort_abo(cls, ):
     #    pass


