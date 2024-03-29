import psycopg2

with open('/Users/roman/Git/SQL_pass.ini') as file:
    password = file.readline().strip()


def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS clients(
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(40),
                last_name VARCHAR(40),
                email VARCHAR(40) UNIQUE);
                """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phone_numbers(
                id SERIAL PRIMARY KEY,
                id_client INTEGER REFERENCES clients(id) ON DELETE CASCADE,
                phonenumber VARCHAR(12) UNIQUE NOT NULL);
                """)
        conn.commit()


def add_client(conn, first_name, last_name, email, phone=None):
    with conn.cursor() as cur:
        cur.execute("""INSERT INTO clients (first_name, last_name, email) VALUES
        (%s, %s, %s) RETURNING id""", (first_name, last_name, email))

        client_id = cur.fetchone()[0]
    
        if phone is not None:
            cur.execute("""INSERT INTO phone_numbers (id_client, phonenumber) VALUES
            (%s, %s)""", (client_id, phone))
            print(f'номер телефона:{phone} добавлен')

        print(f'клиент: {first_name} {last_name} добавлен')

    
def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
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
    with conn.cursor() as cur:
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
    with conn.cursor() as cur:
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
    with conn.cursor() as cur:
        cur.execute("""DELETE FROM clients
                    WHERE id = %s
                    RETURNING *; """,
                    (client_id))
        
        if not cur.fetchall():
            print('нет такого пользователя')
        else:
            print(f'пользователь <<{client_id}>> успешно удален')

        
        # cur.execute("""SELECT id FROM clients  
        # WHERE id=%s;""", (client_id))
        # client_search = cur.fetchall()

        # if client_search is None or len(client_search) == 0:
        #     print(f'нет такого пользователя')

        # else:
        #     cur.execute("""
        #         DELETE  FROM clients WHERE id=%s;
        #         """, (client_id))
        
        #     print(f'пользователь <<{client_id}>> успешно удален')


def find_client(conn, first_name='%', last_name='%', email='%', phone='%'):
    with conn.cursor() as curs:
        find = f"""  /* Описываем будущий запрос и сохраняем в переменную */
            SELECT
                cl.id,  
                email, /* поле почты */
                first_name, /* поле имени */
                last_name,  /* поле фамилии*/
                CASE
                    WHEN ARRAY_AGG(phonenumber) = '{{Null}}' THEN '{{}}' /* Вместо точек указывается столбец, содержащий телефон. В данной строке, если у клиента нет номеров, то отправляем пустой массив */
                    ELSE ARRAY_AGG(phonenumber) /* Вместо точек указывается столбец, содержащий телефон */
                END phone_numbers 
            FROM clients cl /* Из таблицы клиентов */
            LEFT JOIN phone_numbers ph_n ON ph_n.id_client = cl.id /* Объединяем с таблицей телефонов */
            WHERE first_name ILIKE %s AND last_name ILIKE %s AND email ILIKE %s AND phonenumber ILIKE %s /* Где имя, фамилия имейл и телефон соответствуют неким передаваемым значениям. Именно в таком поряке и необходимо писать условие */
	    GROUP BY cl.id, email, first_name , last_name /* Группируем по почте, имени и фамилии */       
	    """
        curs.execute(
            find,  # Передаем переменную с запросом
            (first_name, last_name, email, phone)  # Передаем кортеж из имени, фамилии, почты и телефона
        )
        result = curs.fetchall()
        print('следующие клиенты соответсвуют результату запроса :')
        # print(result)
        for i in result:
            id_number, email, name, l_name, phone = i       
            print(f'клиент с id = {id_number} ---> {name} {l_name} \n email:' 
                  f'{email} \n phone: {phone}\n ______________')

# def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
#     with conn.cursor() as cur:
#         if phone is not None:
#             cur.execute("""SELECT clients.id, clients.first_name, clients.last_name FROM clients
#                         JOIN phone_numbers ON clients.id = phone_numbers.id_client
#                         WHERE phone_numbers.phonenumber=%s ;""", (phone,))
    
#         elif email is not None:
#             cur.execute("""SELECT clients.id, clients.first_name, clients.last_name FROM clients
#                         WHERE email=%s;""",
#                         (email,))
        
#         elif first_name is not None and last_name is not None:
#             cur.execute("""SELECT clients.id, clients.first_name, clients.last_name FROM clients
#                         WHERE first_name=%s and last_name=%s;""",
#                         (first_name, last_name))
        
#         else:
#             cur.execute("""SELECT clients.id, clients.first_name, clients.last_name FROM clients
#                         WHERE first_name=%s or last_name=%s;""",
#                         (first_name, last_name))
#         result = cur.fetchall()
#         print('следующие клиенты соответсвуют результату запроса :')
#         for i in result:
#             id, name, l_name = i       
#             print(f'клиент с id = {id} ---> {name} {l_name}')
   

with psycopg2.connect(database="pythondb", user="postgres", password=password) as conn:
    
        # 1.Функция, создающая структуру БД. Т.е. в данной функции создаются таблицы в базе данных
    create_db(conn)

        # 2.Функция, позволяющая добавить нового клиента как с номером телефона, так и без него
    add_client(conn, 'Mike', 'Nolty', '212@dd.ru', '+79883342233')
    add_client(conn, 'Addy', 'Harris', '213@dd.ru')
    add_client(conn, 'Mary', 'XXX', 'xxx@dd.ru')
    add_client(conn, 'Ann', 'Harris', '214@dd.ru')
    add_client(conn, 'Mary', 'Colt', '191@dd.ru')

        # ______________________________________________________
    # with conn.cursor() as cur:    
        # cur.execute("delete from phone_numbers where id>0;")
        # cur.execute("""ALTER SEQUENCE phone_numbers_id_seq RESTART WITH 1;""")
        # cur.execute("delete from clients where id>0;")
        # cur.execute("""ALTER SEQUENCE clients_id_seq RESTART WITH 1;""")       
        # _______________________________________________________
        
        # cur.execute("""select * from phone_numbers""") # все номера телефонов в БД
        # print(f'таблица телефонов: {cur.fetchall()}')

        # cur.execute("""select * from clients""") # все клиенты в БД
        # print(f'таблица клиентов: {cur.fetchall()}')

        # 3.Функция, позволяющая добавить телефон для существующего клиента
    add_phone(conn, '1', '+79883342230')
    add_phone(conn, '2', '+79883342231')
    add_phone(conn, '3', '+79883342232')
    add_phone(conn, '4', '+79883342533')
    add_phone(conn, '2', '+79883346234')
    add_phone(conn, '55', '+79883344235')

        # 4.Функция, позволяющая изменить данные о клиенте (имя, фамилию и email). 
        # Должна быть возможность как изменить одно значение, так и сразу несколько
    change_client(conn, client_id='1', first_name='Joe', last_name='Fradrich' , email='www@qqq.ru')
    change_client(conn, client_id='1', first_name='Igor')
    change_client(conn, client_id='3', first_name='Mary', last_name='Winter')
    change_client(conn, '1', 'Ann')
    # change_client(conn, client_id='2')

        # 5.Функция, позволяющая удалить телефон для существующего клиента
    delete_phone(conn, '1', '+79883342230')
    delete_phone(conn, '2', '+79883346234')
    delete_phone(conn, '5', '+79883342233')

        # 6.Функция, позволяющая удалить существующего клиента
    delete_client(conn, client_id='1')

        # 7.Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у и телефону) .
        #  Должна быть возможность найти клиента как по одному параметру, так и по нескольким. 
        #  При передачи нескольких параметров, круг поиска должен сужаться.
    find_client(conn, first_name="Ann")
    find_client(conn, phone='+79883346234')
    find_client(conn, first_name='Ann', phone='+79883342230')
    find_client(conn, last_name='Harris')

