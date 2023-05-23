from models import create_tables, Course, Homework 
import psycopg2
import sqlalchemy
from sqlalchemy.orm import sessionmaker

with open('/Users/roman/Git/SQL_pass.ini') as file:
    password = file.readline().strip()

DSN = f'postgresql://postgres:{password}@localhost:5432/alchemy'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

course1 = Course(name='Java') 
course2 = Course(name='Go')

session.add_all([course1, course2])
session.commit()

# print(course1)

homew1 = Homework(number=1, description='work 1', course=course1)
homew2 = Homework(number=2, description='work 2', course=course1)
# homew3 = Homework(number=3, description='work 3', course=course2)
session.add_all([homew1, homew2])
session.commit()

# for c in session.query(Homework).filter(Homework.description.like('%1%')).all():
#     print(c)

# for i in session.query(Course).join(Homework.course).filter(Homework.number == 1).all():
    # print(i)

subq = session.query(Homework).filter(Homework.description.like('%2%')).subquery()
for i in session.query(Course).join(subq, Course.id == subq.c.course_id).all():    # subq.c - обращаем внимание на с!!!
    print(i)
    print()

# session.query(Course).filter(Course.name == 'Java').update({'name':'Python'})
# session.commit()
# print(course1)

# session.query(Course).filter(Course.name == 'Go').delete()
# session.commit()

# for _ in session.query(Course).all():
#     print(_)

session.close()
