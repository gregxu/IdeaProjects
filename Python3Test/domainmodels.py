__author__ = 'gregxu'

# import pymysql
# conn = pymysql.connect(host='localhost', user='root', passwd=None, db='test')
# cur = conn.cursor()
# cur.execute("SELECT * FROM client_firms")
# for response in cur:
#     print(response)
# cur.close()
# conn.close()

from sqlalchemy import Column, String, func, create_engine, Integer, ForeignKey, Table, Text
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import  declarative_base

#engine = create_engine('sqlite:///:memory:', echo=True)
#engine = create_engine('mysql://gregxu:password@localhost/foo')
engine = create_engine('mysql+pymysql://root@localhost/test')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    fullname = Column(String(128))
    password = Column(String(128))
    #addresses = relationship("Address", order_by="Address.id", backref="user")

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    email_address = Column(String(128), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", backref=backref('addresses', order_by=id))

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

post_keywords = Table('post_keywords', Base.metadata,
                      Column('post_id', Integer, ForeignKey('posts.id')),
                      Column('keyword_id', Integer, ForeignKey('keywords.id')))

class BlogPost(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    headline = Column(String(256), nullable=False)
    body = Column(Text)

    keywords = relationship('Keyword', secondary=post_keywords, backref='posts')
    author = relationship(User, backref=backref('posts', lazy='dynamic'))

    def __init__(self, headline, body, author):
        self.author = author
        self.headline = headline
        self.body = body

    def __repr__(self):
        return  "BlogPost(%r %r %r)" % (self.headline, self.body, self.author)

class Keyword(Base):
    __tablename__ = 'keywords'

    id = Column(Integer, primary_key=True)
    keyword = Column(String(50), nullable=False, unique=True)

    def __init__(self, keyword):
        self.keyword = keyword


Base.metadata.create_all(engine)
#
# ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
# session.add(ed_user)
#
# session.add_all([User(name='wendy', fullname='Wendy Williams', password='foobar'),
#                  User(name='mary', fullname='Mary Contrary', password='xxg527'),
#                  User(name='fred', fullname='Fred Flinstone', password='blah')])

# our_user = session.query(User).filter_by(name='ed').first()
# print(our_user)


# for x, y in session.query(User.name, User.fullname).filter(~User.name.in_(['ed', 'wendy', 'jack'])):
#     print(x, y)

# jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
# jack.addresses = [Address(email_address='jack@google.com'),
#                   Address(email_address='j25@yahoo.com')]
#
# session.add(jack)


wendy = session.query(User).filter_by(name='wendy').one()
# post = BlogPost("Wendy's Blog Post", "This is a test", wendy)
# session.add(post)
# post.keywords.append(Keyword('wendy'))
# post.keywords.append(Keyword('firstpost'))
#
# session.commit()

# p = session.query(BlogPost).filter(BlogPost.author == wendy).filter(BlogPost.keywords.any(keyword='firstpost')).all()
# print(p)
#
# print(wendy.posts.all())

user1 = User()
user1.name = 'fdfd'
user1.fullname = "sdfd"
user1.password = "dfdfsdf"
print(user1)