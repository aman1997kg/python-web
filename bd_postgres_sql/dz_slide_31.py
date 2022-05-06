import psycopg2

conn = psycopg2.connect(
    database = 'person',
    user = 'aman040997',
    password = '040997',
    host = 'localhost',
    port = 5432
)

cur = conn.cursor()
#cur.execute("INSERT INTO users(name) VALUES('Asan')")
#cur.execute("SELECT * FROM users;")

    #1.Посчитайте количество записей 
#cur.execute("SELECT COUNT(*) FROM users")


    #2.Сколько followerОВ у самого знаменитого пользователя 
#cur.execute("SELECT MAX(followers) FROM users;")
    
    #3.Напишите запрос, который выводит всю информацию самого знаменитого пользователя  
#cur.execute("SELECT ")
    
    #4.Отсортируйте всех пользователей по логину #ASK #DESC ----> Сортировка по алфавиту и набарот
#cur.execute("SELECT login FROM users ORDER BY login;")

    #5.Найдите среднее количество подписчиков 
#cur.execute("SELECT AVG(followers) FROM users;")
    
    #6.Просортируйте всех пользователей по стране 
#cur.execute("SELECT country FROM users ORDER BY country;")

    #7.Отсортируйте всех пользователей по email 
#cur.execute("SELECT * FROM users ORDER BY email;")

    #8.Напишите запрос, который выводит id из колонки пользователей и имя из колонки clients 
#cur.execute("SELECT user_id, login FROM users;")

    #9.Напишите запрос,который выводит всё о пользователе, чей логин содержит as, cg, si, am, qwe, er, ka, an
#cur.execute("SELECT * FROM users WHERE (login LIKE '%as%') OR (login LIKE '%cg%') OR (login LIKE '%si%') OR (login LIKE '%am%') OR (login LIKE '%qwe%') OR (login LIKE '%er%') OR (login LIKE '%ka%') OR (login LIKE '%ka%') OR (login LIKE '%an%');")

    #10.Напишите запрос,который выводит всё о пользователе, чей логин заканчивается на lol, kan, ck, ie. ig 
#cur.execute("SELECT * FROM users WHERE (login ILIKE '%lol') OR (login ILIKE '%kan') OR (login ILIKE '%ie') OR (login ILIKE '%ig') OR (login ILIKE '%ck');")

    #11.Напишите запрос, который выводит всё о пользователе, чей логин начинается на a, b, c, d, M, D, A
#cur.execute("SELECT * FROM users WHERE (login ILIKE 'a%') OR (login ILIKE 'b%') OR (login ILIKE 'd%') OR (login ILIKE 'M%') OR (login ILIKE 'D%') OR (login ILIKE 'A%');")

    #12. Как зовут самого знаменитого Сеньор Программиста(Senior Programmer) из Израиля(Israel)? 
#cur.execute("SELECT * FROM users WHERE country  LIKE '%Israel%';")

    #13. Выведите на экран всех пользователей у кого пустая почта. 
#cur.execute("SELECT * FROM users WHERE email LIKE '';")

    #14. Посчитайте сколько пользователей у которых нет email живут на Chui.
#cur.execute("SELECT")

    #15. Покажите имена и номера телефонов всех людей которые работают как Web Developer
#cur.execute("SELECT login, phone_number, profession FROM users WHERE profession ILIKE 'Web Developer';")

    #16. У всех пользователей у которых почта ровняется False обновите почту на user@gmail.com. 
#cur.execute("UPDATE users SET email = 'user@gmail.com' WHERE email LIKE '%Web developers%';")

    #17. Узнайте из каких стран люди которые не имею работы(Unemployed).
#cur.execute("SELECT login, country, profession FROM users WHERE profession ILIKE '%unemployed%';")
 
    #18. Везде где номер телефона начинается с 000 замените его любой РЕАЛЬНЫЙ номер в формате столбца phone_number. 
#cur.execute("UPDATE users SET phone_number = '+996700119997' WHERE phone_number LIKE '000%';")

    #19. 12345, user123б, qwerty считается лёгкими паролями у каждого пользователя у кого лёгкий пароль удалите из Базы Данных.
#cur.execute("SELECT * FROM users WHERE (password ILIKE '%qwerty%') OR (password ILIKE '%12345%') OR (password ILIKE '%user123б%');")

   #20. Выведите на экран email всех .NET Developer разработчиков и отсортируйте их по Имени.
#cur.execute("SELECT * FROM users WHERE profession ILIKE '%.nET developer%';")



#-----------------------------------------------------------------------------------------------------------------------------------------------------
                                               #Market, globus, narodnii

   #21. Найдите сколько разных типов продуктов в таблице globus.
#cur.execure(" ")

   #22.Используя HAVING найдите сколько и каких продуктов в narodnii испортятся меньше чем через дня. 
#cur.execute(" ")

    #23. Посчитайте в каком магазине больше сникерсов в globus или narodnii
#cur.execute(" person=> SELECT (SELECT product_name FROM  globus WHERE product_name ILIKE '%Snikers%' LIMIT 1), COUNT(product_name) AS globus,(SELECT COUNT(product_name) AS narodnii FROM narodnii WHERE product_name ILIKE '%Snikers%') FROM  globus WHERE product_name ILIKE '%Snikers%';")

    #24. Посмотрите продукты в globus и narodnii у которых product_type равен сроку годности продукта.
#cur.execute("SELECT product_name, product_type_id, day_to_expire FROM globus INTERSECT SELECT product_name, product_type_id, day_to_expire FROM narodnii;")

    #25. Посмотрите продукты из globus и narodnii у которых одинаковый срок годности.
#cur.execute("SELECT product_name, day_to_expire FROM globus INTERSECT SELECT product_name, day_to_expire FROM narodnii;")

    #26. Через Python подключитесь к БД main и узнайте сколько ВСЕГО piyaz в магазине globus
#cur.execute("SELECT COUNT(*) FROM globus WHERE product_name ILIKE '%piyaz%';")

    #27. Через Python удалите из магазина narodnii все продукты у которых срок годности
#cur.execute(" ")

    #28. Если ПРОДУКТ и СРОК ГОДНОСТИ продукта одинаковы в globus и narodnii удалите эту запись из globus. 
#cur.execute(" ")

    #29. Напишите запрос, который выводит всю информацию продукта из народного, где количество продуктов 200 < продукт < 1001
#cur.execute("SELECT * FROM narodnii WHERE 200 < product_amount OR product_amount > 1001;")

    #30. Напишите запрос, который соединяет таблицы глобус народный и выводит day delivered
#cur.execute("SELECT product_name, date_delivered FROM globus UNION ALL SELECT product_name, date_delivered FROM narodnii;")
#SELECT globus.product_name, globus.date_delivered, narodnii.product_name, narodnii.date_delivered FROM globus FULL JOIN narodnii ON globus.product_id = narodnii.product_id;

    #31. Напишите запрос, который соединяет таблицы глобус народный по столбцу глобуса и выводит название продукта 
#cur.execute("SELECT globus.product_name AS Globus, narodnii.product_name AS Narodnii FROM globus FULL JOIN narodnii ON globus.product_id = narodnii.product_id;") 

    #32. Напишите запрос, который соединяет таблицы глобус народный по столбцу народного и выводит название продукта  
#cur.execute(" ")

    #33. Напишите запрос, который соединяет таблицы глобус народный и выводит совпадения количества продуктов. 
#cur.execute(" ")














#conn.commit()
print(cur.fetchall())
