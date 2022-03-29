'''Написать программу авторизации. При успешной авторизации вернуть «Вход выполнен», иначе вернуть «Неверное имя пользователя или пароль»'''

'''
def authorize_check(username, password, entered_username, entered_password):
    if username == entered_username and password == entered_password:
        return "Вход выполнен"
    else:
        return "Неверное имя пользователя или пароль"
'''

username = str(input('user name : '))
password = str(input('password : '))
entered_username = str(input('entered_username : '))
entered_password = str(input('entered_password :'))

if username == entered_username and password == entered_password:
    print("Вход выполнен")
else:
    print('Неверное имя пользователя или пароль')
