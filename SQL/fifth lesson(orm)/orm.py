import json
from models import create_tables, Publisher, Book, Shop, Stock, Sale 
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_

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
    # print(record)
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
subq = session.query(Publisher).filter(or_(Publisher.id == publisher_search, Publisher.name == publisher_search)).subquery()
for i in session.query(Shop).join(Stock).join(Book).join(subq, Book.id_publisher == subq.c.Publisher.id).all():
    print(i)

session.close()