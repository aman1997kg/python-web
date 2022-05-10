"""Создайте класс ContactList,
который должен наследоваться от встроенного класса list.

В нем должен быть реализован метод search_by_name, который должен принимать имя,
и возвращать список всех совпадений. Если нету совпадений, то возвращает пустой список.

Создайте несколько контактов (просто имена в типе строка) ,
используйте метод search_by_name."""


class List:

    def __init__(self):
        self.return_list_name = []
        self.new_list = []

    def search_by_name(self, *name):
        for i in name:
            self.return_list_name.append(i.title())
        name_list = [i for i in self.return_list_name if self.return_list_name.count(i) > 1]
        set_name_list = set(name_list)

        for a in set_name_list:
            self.new_list.append(a)
        return self.new_list



class ContactList(List):
    all_list = []
    all_list3 = []

    def search_by_name(self, *name):
        for i in name:
            if name == self:
                print('ok')
            else:
                print('no')




my_contacts = ContactList()
my_contacts.search_by_name("1", "2", "3", "4", "1", "2", "5")

print(my_contacts.search_by_name())