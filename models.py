from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase('data.sqlite')

class User(UserMixin, Model):
  username=CharField(unique=True)
  email=CharField(unique=True)
  password=CharField()
  city=CharField()

  class Meta:
    database = DATABASE

class Like_Restaurant(Model):
  restaurant_id: CharField()
  address: CharField()
  picture: CharField()
  user_id: ForeignKeyField(User, backref="liked_restaurants")

  class Meta:
    database = DATABASE

class Dislike_Restaurant(Model):
  restaurant_id: CharField()
  user_id: ForeignKeyField(User, backref="dislike_restaurant")

  class Meta:
    database = DATABASE

class Friend(Model):
  user_id1: ForeignKeyField(User, backref='friend')
  user_id2: ForeignKeyField(User, backref='friend')

  class Meta:
    database = DATABASE

def initialize():
  DATABASE.connect()

  DATABASE.create_tables([User], safe=True)
  print('connected to database')

  DATABASE.close()