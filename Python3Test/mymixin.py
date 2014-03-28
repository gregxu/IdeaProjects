__author__ = 'gregxu'

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer

class MyMixin(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = { 'mysql_engine' : 'ollmodel'}
    __mapper_args__ = { 'always_refresh' : True }

    id = Column(Integer, primary_key=True)


