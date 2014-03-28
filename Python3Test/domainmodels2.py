__author__ = 'gregxu'


from sqlalchemy import create_engine, Table, MetaData, Column, ForeignKey, Integer, String
from sqlalchemy.orm import  mapper, relationship, backref

engine = create_engine('mysql+pymysql://root@localhost/ollmodel')

metadata = MetaData()

users = Table('users', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(64)),
             Column('fullname', String(64)),
             Column('password', String(64)))

class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

address = Table('addresses', metadata,
                Column('id', Integer, primary_key=True),
                Column('user_id', Integer, ForeignKey('users.id')),
                Column('email_address', String(128)))

class Address(object):
    def __init__(self, email_address):
        self.email_address = email_address

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

mapper(User, users, properties={
    'addresses' : relationship(Address, backref='user', order_by=address.c.id)
})

mapper(Address, address)

metadata.create_all(engine)

