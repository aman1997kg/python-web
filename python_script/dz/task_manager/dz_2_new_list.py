"""Создайте класс ContactList (название должно совпадать),
 который должен наследоваться от встроенного класса list.
 В нем должен быть реализован метод search_by_name, который должен принимать имя,
 и возвращать список всех совпадений.
 Создайте несколько контактов, используйте метод search_by_name."""


class List:

    def __init__(self):
        self.return_list_name = []
        self.new_list = []

    def __str__(self):
        return self.new_list

    def __repr__(self):
        return self.new_list


    def search_by_name(self, *name):
        for i in name:
            self.return_list_name.append(i.title())
        name_list = [i for i in self.return_list_name if self.return_list_name.count(i) > 1]
        set_name_list = set(name_list)
        for a in set_name_list:
            self.new_list.append(a)
        print(self.new_list)
        return  self.new_list.__str__()


class ContactList(List):

    def __init__(self):
        super().__init__()


my_contacts = ContactList()
my_contacts.search_by_name("Anan","banan","algan","salgan","Salgan","Banan","Algan")
