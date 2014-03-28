__author__ = 'gregxu'

import sqlalchemy

from sqlalchemy import *
from sqlalchemy.ext.declarative import  declarative_base

#engine = create_engine('sqlite:///:memory:', echo=True)
#engine = create_engine('mysql://gregxu:@localhost')
engine = create_engine('mysql://root@localhost/test?charset=utf8&use_unicode=0', pool_recycle=3600)
# connection = engine.connect()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    fullname = Column(String(64))
    password = Column(String(64))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

Base.metadata.create_all(engine)

