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
