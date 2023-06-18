import json
from models import create_tables, Publisher, Book, Shop, Stock, Sale 
import sqlalchemy
from sqlalchemy.orm import sessionmaker

with open('/Users/roman/Git/SQL_pass.ini') as file:
    password = file.readline().strip()

DSN = f'postgresql://postgres:{password}@localhost:5432/python_orm'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open('fixtures/tests_data.json', 'r') as fd:
    data = json.load(fd)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()

publisher_search = input('введите имя или id издателя: ')
shops = session.query(Shop).join(Stock).join(Book).join(Publisher)

if publisher_search.isdigit(): #Проверяем состоит ли строка, которую ввел пользователь, только из чисел    
    search = shops.filter(Publisher.id == publisher_search).all() #Применяем фильтрацию к уже ранее созданному запросу, где идентификационный номер публициста равен значению, который был передан в функцию, и сохраняем результат в переменную
else:
    search = shops.filter(Publisher.name == publisher_search).all() #Применяем фильтрацию к уже ранее созданному запросу, где имя публициста равен значению, который был передан в функцию, и сохраняем результат в переменную

for shop in search: #Проходим в цикле по полученным данным из функции, получая при каждой итерации экземпляр класса
    print(shop) #Обращаемся в к экземпляру и выводим его имя


session.close()