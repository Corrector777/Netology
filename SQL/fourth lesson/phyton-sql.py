import psycopg2


with psycopg2.connect(database="pythondb", user="postgres", password="fixator1") as conn:
    with conn.cursor() as cur:
        cur.execute("CREATE TABLE test(id SERIAL PRIMARY KEY);")
        conn.commit()
