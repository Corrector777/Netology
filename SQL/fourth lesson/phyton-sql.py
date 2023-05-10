import psycopg2

with open('/Users/roman/Git/SQL_pass.ini') as file:
    password = file.readline().strip()

with psycopg2.connect(database="pythondb", user="postgres", password=password) as conn:
    with conn.cursor() as cur:
        cur.execute("CREATE TABLE test(id SERIAL PRIMARY KEY);")
        conn.commit()
