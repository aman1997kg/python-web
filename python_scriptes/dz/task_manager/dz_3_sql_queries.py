import psycopg2

conn = psycopg2.connect(
    database = 'products',
    user = 'aman040997',
    password = '040997',
    host = 'localhost',
    port = 5432
)



cur = conn.cursor()
#cur.execute("INSERT INTO products(name) VALUES('Asan')")
#cur.execute("SELECT * FROM products;")

    #1.Вывести бренды и модели из таблицы products. Поля таблицы: id | brand | model | speed | hd | ram | price | cd .

#cur.execute("SELECT brand, model FROM products;")


    #2. Вывести все записи из таблицы productsi
#cur.execute("SELECT * FROM products;")

    #3. id	brand	model	speed	hd	ram	price	cd

#1	Acer	Aspire	450	32	10	350	24x
#2	Acer	Aspire	450	64	8	350	24x
#3	Acer	Aspire	500	32	10	400	12x
#4	Acer	Aspire	500	64	5	600	12x
#5	Acer	Extensa	500	64	5	600	12x
#6	Acer	Extensa	750	128	20	950	50x
#7	Acer	Extensa	800	128	20	970	50x
#8	Acer	Extensa	900	128	40	980	40x
#9	Toshiba	Satellite	600	128	14	850	40x
#10	Toshiba	Satellite	600	128	8	850	40x
#11	Toshiba	Satellite	750	128	14	850	40x
#12	HP	Probook	500	32	10	350	12x
    

    #4. Вывести все поля таблицы products, где бренд равняется Acer

#cur.execute("SELECT * FROM products WHERE brand = 'Acer';")


    #5. Вывести модели и стоимость ноутбуков, цена которых не превышает 750 долларов и объемом жесткого диска (hd) не менее 50 Gb из таблицы products. Поля таблицы: id | brand | model | speed | hd | ram | price | cd .

#cur.execute("SELECT model, price FROM products WHERE price < 750 and hd > 50;")
 

    #6. Вывести бренды, модели и скорость ноутбуков, цена которых превышает 600 долларов из таблицы products. Поля таблицы: id | brand | model | speed | hd | ram | price | cd .

#cur.execute("SELECT brand, model, speed FROM products WHERE price >600;")

    #7. Вывести бренд, модель и стоимость ноутбуков, у которых стоимость не превышает 600 долларов или у которых скорость не менее 600 и cd равен '50x' из таблицы products. Поля таблицы: id | brand | model | speed | hd | ram | price | cd .

#cur.execute("SELECT brand, price FROM products WHERE price < 600 or speed > 600 or cd = '50';")


    #8.Вывести бренды, у которых размер жесткого диска равен 32 и 64 из таблицы products. Поля таблицы: id | brand | model | speed | hd | ram | price | cd .

#cur.execute("SELECT brand FROM products WHERE hd = 32 or hd = 64;")

    #9. Вывести бренды, модели, у которых cd не в числе '12х', '24х', '40х' из таблицы products. Поля таблицы: id | brand | model | speed | hd | ram | price | cd .

cur.execute("SELECT brand, model FROM products WHERE cd NOT = '12х', '24х', '40х';")



#conn.commit()
print(cur.fetchall())


