import models

User = models.User

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash
from flask_login import login_user, current_user, logout_user
from playhouse.shortcuts import model_to_dict
users = Blueprint('users', 'users')

@users.route('/', methods=['GET'])
def user():
  return "user connected"

@users.route('/register', methods=['POST'])
def user_register():
    payload = request.get_json()
    payload['username'] = payload['username'].lower()

    try:
      User.get(User.username == payload['username'])
      return jsonify(
        data={},
        message=f"A user with username {payload['username']} already exists",
        status=401
      ), 401
      User.get(User.email == payload['email'])
      return jsonify(
      data={},
        message=f"A user with email {payload['email']} already exists",
        status=401
      ), 401
    except models.DoesNotExist:
      pw_hash = generate_password_hash(payload['password'])

      created_user = User.create(
        username=payload['username'],
        email=payload['email'],
        password=pw_hash, 
        city=payload['city']
      )
      login_user(created_user)

      created_user_dict = model_to_dict(created_user)
      created_user_dict.pop('password')

      return jsonify(
        data=created_user_dict,
        message=f"Successfully registered user {created_user_dict['username']}",
        status=201
      ), 201



@users.route('/logout', methods=['GET'])
def user_logout():
  if current_user.is_authenticated:
    logout_user()
    return jsonify(
      data={},
      message="Successfully logged out",
      status=200
    ), 200
  else:
    return jsonify(
      data={},
      message="No user is logged in",
      status=412
    ), 412
