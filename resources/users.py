import models

User = models.User

from flask import Blueprint

users = Blueprint('users', 'users')

@users.route('/', methods=['GET'])
def user():
  return "user connected"