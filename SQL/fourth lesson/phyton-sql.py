import psycopg2

with open('/Users/roman/Git/SQL_pass.ini') as file:
    password = file.readline().strip()


def create_db(conn):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS clients(
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(40),
            last_name VARCHAR(40),
            email VARCHAR(40));
            """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phone_numbers(
            id SERIAL PRIMARY KEY,
            id_client INTEGER REFERENCES clients(id),
            phonenumber VARCHAR(12) NOT NULL);
            """)
    conn.commit()


def add_client(conn, first_name, last_name, email, phone=None):
    cur.execute("""INSERT INTO clients (first_name, last_name, email) VALUES
    (%s, %s, %s) RETURNING id""", (first_name, last_name, email))

    client_id = cur.fetchone()[0]
    
    if phone is not None:
        cur.execute("""INSERT INTO phone_numbers (id_client, phonenumber) VALUES
        (%s, %s)""", (client_id, phone))
        print(f'номер телефона:{phone} добавлен')

    print(f'клиент: {first_name} {last_name} добавлен')

    
def add_phone(conn, client_id, phone):
    cur.execute("""SELECT phonenumber FROM phone_numbers  
    WHERE id_client=%s AND phonenumber=%s;""", (client_id, phone))  # Запрос в БД по данному номеру
    phone_number_search = cur.fetchall()  # Вывод значений из БД по заданному client_id иномеру

    if phone_number_search is None or len(phone_number_search) == 0:  # Если в базе такого номера нет, то добавляем. Для несуществующего клиента будет ошибка.
        cur.execute("""INSERT INTO phone_numbers (id_client, phonenumber) VALUES
        (%s, %s)""", (client_id, phone))
        print(f'номер телефона <<{phone}>> для клиента <<{client_id}>> успешно добавлен')

    else:
        print(f'данный номер уже существует у клиента <<{client_id}>>')

    conn.commit()


def change_client(conn, client_id, first_name=None, last_name=None, email=None):
    if first_name is not None:
        cur.execute("""
        UPDATE clients SET first_name=%s WHERE id=%s;
        """, (first_name, client_id))
        print(f'Имя клиента <<{client_id}>> успешно изменено на {first_name}')

    if last_name is not None:
        cur.execute("""
        UPDATE clients SET last_name=%s WHERE id=%s;
        """, (last_name, client_id))
        print(f'фамилия клиента <<{client_id}>> успешно изменена на {last_name}')

    if email is not None:
        cur.execute("""
        UPDATE clients SET email=%s WHERE id=%s;
        """, (email, client_id))
        print(f'email клиента <<{client_id}>> успешно изменен на {email}')

    if first_name is None and last_name is None and email is None:
        print(f'для клиента <<{client_id}>> нет изменений')
    
    print('__________________________________________\n')


def delete_phone(conn, client_id, phone):
    cur.execute("""SELECT phonenumber FROM phone_numbers  
    WHERE id_client=%s AND phonenumber=%s;""", (client_id, phone))
    phone_number_search = cur.fetchall()
    if phone_number_search is None or len(phone_number_search) == 0:
        print(f'нет такого номера или пользователя')

    else:
        cur.execute("""
            DELETE FROM phone_numbers WHERE id_client=%s and phonenumber=%s;
            """, (client_id, phone))
        print(f'у пользователя <<{client_id}>> удален номер телефона: {phone}')

def delete_client(conn, client_id):
    cur.execute("""SELECT id FROM clients  
    WHERE id=%s;""", (client_id))
    client_search = cur.fetchall()

    if client_search is None or len(client_search) == 0:
        print(f'нет такого пользователя')

    else:
        cur.execute("""
            DELETE  FROM phone_numbers WHERE id_client=%s;
            """, (client_id))
        cur.execute("""
            DELETE  FROM clients WHERE id=%s;
            """, (client_id))
        
        print(f'пользователь <<{client_id}>> успешно удален')


def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    if phone is not None:
        cur.execute("""SELECT clients.id FROM clients
                    JOIN phone_numbers ON clients.id = phone_numbers.id_client
                    WHERE phone_numbers.phonenumber=%s ;""", (phone,))
    
    else:
        cur.execute("""SELECT clients.id FROM clients
                    WHERE first_name=%s or last_name=%s or email=%s;""",
                    (first_name, last_name, email))
    
    print(cur.fetchall())


with psycopg2.connect(database="pythondb", user="postgres", password=password) as conn:
    with conn.cursor() as cur:
        # 1.Функция, создающая структуру БД. Т.е. в данной функции создаются таблицы в базе данных
        # create_db(conn)

        # 2.Функция, позволяющая добавить нового клиента как с номером телефона, так и без него
        # add_client(conn, 'Nick', 'Nolty', '222@dd.ru', '+79883342233')
        # add_client(conn, 'Addy', 'Harris', '222@dd.ru')
        # add_client(conn, 'Mary', 'XXX', 'xxx@dd.ru')
        #______________________________________________________
        # cur.execute("delete from phone_numbers where id>0;")
        # cur.execute("""ALTER SEQUENCE phone_numbers_id_seq RESTART WITH 1;""")
        # cur.execute("delete from clients where id>0;")
        # cur.execute("""ALTER SEQUENCE clients_id_seq RESTART WITH 1;""")       
        #_______________________________________________________
        
        # cur.execute("""select * from phone_numbers""") # все номера телефонов в БД
        # print(f'таблица телефонов: {cur.fetchall()}')

        # cur.execute("""select * from clients""") # все клиенты в БД
        # print(f'таблица клиентов: {cur.fetchall()}')

        # 3.Функция, позволяющая добавить телефон для существующего клиента
        # add_phone(conn, '1', '+79883342233')
        # add_phone(conn, '1', '+79883342233')
        # add_phone(conn, '1', '+79883342993')
        # add_phone(conn, '1', '+79883342533')
        # add_phone(conn, '2', '+79883342233')
        # add_phone(conn, '3', '+79883342233')

        # 4.Функция, позволяющая изменить данные о клиенте (имя, фамилию и email). 
        # Должна быть возможность как изменить одно значение, так и сразу несколько
        # change_client(conn, '1', 'Ann')
        # change_client(conn, client_id='1', first_name='Joe', last_name='Fradrich' , email='www@qqq.ru')
        # change_client(conn, client_id='1', first_name='Igor')
        # change_client(conn, client_id='3', first_name='Mary', last_name='Winter')
        # change_client(conn, client_id='2')

        # 5.Функция, позволяющая удалить телефон для существующего клиента
        # delete_phone(conn, '1', '+79883342533')
        # delete_phone(conn, '2', '+79883342233')
        # delete_phone(conn, '5', '+79883342233')

        # 6.Функция, позволяющая удалить существующего клиента
        # delete_client(conn, client_id='6')

        # 7.Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у и телефону) .
        #  Должна быть возможность найти клиента как по одному параметру, так и по нескольким. 
        #  При передачи нескольких параметров, круг поиска должен сужаться.
        # find_client(conn, phone='+79883342233')
        find_client(conn, first_name="Ann", last_name='Nolty')

