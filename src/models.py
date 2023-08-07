import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(20)) 
    firstname = Column(String(20)) 
    lastname = Column(String(20)) 
    email = Column(String(50))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(20), ForeignKey('user.id'))
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(20))
    url = Column(String(250))
    post_id= Column(String(20), ForeignKey('post.id'))
    post = relationship(Post)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(20))
    post_id= Column(String(20), ForeignKey('post.id'))
    post = relationship(Post)
    author_id= Column(String(20), ForeignKey('user.id'))
    author = relationship(User)
    
class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(String(20), ForeignKey('user.id'))
    user_from = relationship(User)
    user_to_id = Column(String(20), ForeignKey('user.id'))
    user_to = relationship(User)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
