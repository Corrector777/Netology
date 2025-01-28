import sqlalchemy as sq
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session
from data import db_url_object

metadata = MetaData()
Base = declarative_base()
engine = create_engine(db_url_object)


class Viewed(Base):
    __tablename__ = 'viewed'
    user_id = sq.Column(sq.Integer, primary_key=True)
    search_profile_id = sq.Column(sq.Integer, primary_key=True)


engine = create_engine(db_url_object)
Base.metadata.create_all(engine)


def add_user(engine, user_id, search_profile_id):
    with Session(engine) as session:
        to_bd = Viewed(user_id=user_id, search_profile_id=search_profile_id)
        session.add(to_bd)
        session.commit()

# извлечение записей из БД

def check_user(engine, user_id, search_profile_id):
    engine = create_engine(db_url_object)
    with Session(engine) as session:
        from_bd = session.query(Viewed).filter(Viewed.user_id == user_id, Viewed.search_profile_id == search_profile_id).all()
        return True if from_bd else False


if __name__ == '__main__':

    engine = create_engine(db_url_object)
    Base.metadata.create_all(engine)
    # add_user(engine, 221233, 123131231)
    # print(check_user(engine, 1542332, 7109775995))