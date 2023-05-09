import psycopg2


conn = psycopg2.connect(database="pythondb", user="postgres", password="fixator1") 
with conn.cursor() as cur:
    cur.execute("CREATE TABLE test(id SERIAL PRIMARY KEY);")
    conn.commit()
