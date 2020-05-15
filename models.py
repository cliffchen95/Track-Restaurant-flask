from peewee import *
from flask_login import UserMixin
import os
from playhouse.db_url import connect

if 'ON_HEROKU' in os.environ: 
  DATABASE = connect(os.environ.get('DATABASE_URL')) 
else:
  DATABASE = SqliteDatabase('data.sqlite')

class User(UserMixin, Model):
  username = CharField(unique=True)
  email = CharField(unique=True)
  password = CharField()
  city = CharField()

  class Meta:
    database = DATABASE

class Like_Restaurant(Model):
  restaurant_id= CharField()
  address = CharField()
  city = CharField()
  picture = CharField()
  user_id = ForeignKeyField(User, backref="liked_restaurants")
  url = CharField()
  name = CharField()
  cuisine = CharField()
  
  class Meta:
    database = DATABASE

class Dislike_Restaurant(Model):
  restaurant_id = CharField()
  user_id = ForeignKeyField(User, backref="dislike_restaurant")

  class Meta:
    database = DATABASE

class Friend(Model):
  user_id1 = ForeignKeyField(User, backref='friend')
  user_id2 = ForeignKeyField(User, backref='friend')

  class Meta:
    database = DATABASE

class Request(Model):
  user_from = ForeignKeyField(User, backref='from')
  user_to = ForeignKeyField(User, backref='to')
  info = CharField()

  class Meta:
    database = DATABASE

def initialize():
  DATABASE.connect()

  DATABASE.create_tables([User, Like_Restaurant, Dislike_Restaurant, Request, Friend], safe=True)
  print('connected to database')

  DATABASE.close()