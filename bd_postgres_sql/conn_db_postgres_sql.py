import psycopg2


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