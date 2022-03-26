filename = input()
name_file = filename.split('.')
filename = name_file[::-1]
extention = filename[0]

print(f'"Расширение файла - {extention}"')
