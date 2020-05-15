import models

User = models.User

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required
from playhouse.shortcuts import model_to_dict
users = Blueprint('users', 'users')

@users.route('/update', methods=['PATCH'])
@login_required
def user_update():
  user = User.get_by_id(current_user.id)
  payload = request.get_json()
  query = User.update({
    User.city: payload['city']
  }).where(User.id == current_user.id)
  query.execute()
  return jsonify(
    data={},
    message=f"updated user with id {current_user.id}",
    status=200
  ), 200

@users.route('/register', methods=['POST'])
def user_register():
    payload = request.get_json()
    payload['username'] = payload['username'].lower()

    try:
      User.select().where((User.username == payload['username']) | (User.email == payload['email'])).get()
      return jsonify(
        data={},
        message=f"The username or email already exists",
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
@login_required
def user_logout():
  logout_user()
  return jsonify(
    data={},
    message="Successfully logged out",
    status=200
  ), 200

@users.route('/login', methods=['POST'])
def user_login():
  if not current_user.is_authenticated:
    payload = request.get_json()
    payload['username'] = payload['username'].lower()

    try:
      user = User.get(User.username == payload['username'])
      user_dict = model_to_dict(user)
      if check_password_hash(user_dict['password'], payload['password']):
        login_user(user)
        user_dict.pop('password')
        return jsonify(
          data=user_dict,
          message=f"Successfully logged in {user_dict['username']}",
          status=200
        ), 200
      else:
        return jsonify(
          data={},
          message='Username does not exist or incorrect password',
          status=401
        ), 401

    except models.DoesNotExist:
      return jsonify(
        data={},
        message='Username does not exist or incorrect password',
        status=401
      ), 401
  else:
    user = model_to_dict(current_user)
    user.pop('password')
    return jsonify(
      data=user,
      message=f"You are currently logged in as {user['username']}",
      status=412
    ), 412
