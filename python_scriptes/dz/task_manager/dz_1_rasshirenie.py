"""
Напишите программу, которая принимает имя файла и выводит его расширение. ПРИМЕР:  
 Ввод: "my_photo.png" Вывод: "Расширение файла - png" Ввод: "my_photo.jpeg" Вывод: "Расширение файла - jpeg" Ввод: "my_photo.html" Вывод: "Расширение файла - html" Ввод: "my_photo.oi" Вывод: None Если расширение у файла определить невозможно, то верните None Ожидаемые типы файлов: png, jpeg, html, doc, xlsx.

"""

extention_f = ['png','jpeg','html','doc','xlsx']

filename = input()
name_file = filename.split('.')
filename = name_file[::-1]
extention = filename[0]

for ex in extention_f:
    if ex == extention:
        print(f'"Расширение файла - {extention}"')
    else: 
        print('None')
