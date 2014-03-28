__author__ = 'gregxu'

from sqlalchemy import Column, String, func, create_engine, Integer, ForeignKey, Table, Text
from sqlalchemy.orm import sessionmaker, relationship, backref, with_polymorphic
from sqlalchemy.ext.declarative import  declarative_base

engine = create_engine('mysql+pymysql://root@localhost/ollmodel')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class RentableItem(Base):
    __tablename__ = 'RentableItems'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity' : 'rentableitem',
        'polymorphic_on' : type
    }

class Unit(RentableItem):
    __tablename__ = 'Units'

    id = Column(Integer, ForeignKey('RentableItems.id'), primary_key=True)
    unit_name = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity' : 'unit',
    }

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#session.add_all([ RentableItem(name = 'bed1'), RentableItem(name = 'garage1'), Unit(name='unit', unit_name='301A')])

#session.commit()

entities = with_polymorphic(RentableItem, '*')

all = session.query(entities).all()

u = session.query(Unit).first()
print(u)