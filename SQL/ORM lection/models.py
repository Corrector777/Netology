import sqlalchemy as sq

from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Course(Base):
    __tablename__ = 'course'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    def __str__(self):
        return f'Curse_id {self.id} : {self.name}'
    homeworks = relationship('Homework', backref='course')

class Homework(Base):
    __tablename__ = 'homework'

    id = sq.Column(sq.Integer, primary_key=True)
    number = sq.Column(sq.Integer, nullable=False)
    description = sq.Column(sq.Text, nullable=False)
    course_id = sq.Column(sq.Integer, sq.ForeignKey('course.id'), nullable=False)

    def __str__(self):
        return f'Homework_id {self.id} : ({self.number}, {self.description}, {self.course_id})'

    # course = relationship(Course, backref='homeworks')


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)