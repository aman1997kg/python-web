import psycopg2

'''
conn = psycopg2.connect(
    database = 'users',
    user = 'aman040997',
    password = '040997',
    host = 'localhost',
    port = 5432
)

cur = conn.cursor()
cur.execute("INSERT INTO users(name) VALUES('Asan')")
cur.execute("SELECT * FROM users;")
#conn.commit()
print(cur.fetchall())

'''

#-----------------Работа с ORM Peewee----------------

from peewee import *
from datetime import datetime

            #Подключение уже созданной БД
pg_bd = PostgresqlDatabase(
    'followers',
    login='aman040997',
    password='040997',
    host='localhost',
    port=5432
)

class Followers(Model):
    id = PrimaryKeyField(default=datetime.today())
    name = CharField(max_length=255)
