import models

Like_Restaurant = models.Like_Restaurant
Dislike_Restaurant = models.Dislike_Restaurant

from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from playhouse.shortcuts import model_to_dict
restaurants = Blueprint('restaurants', 'restaurants')

@restaurants.route('/', methods=['POST'])
@login_required
def restaurant():
  if request.method == 'POST':
    if request.headers['like'] == 'true':
      payload = request.get_json()
      new_liked = Like_Restaurant.create(
        restaurant_id=payload['id'],
        address=payload['address'],
        picture=payload['picture'],
        user_id=current_user.id
      )
      new = model_to_dict(new_liked)
      new['user_id'].pop('password')

      return jsonify(
        data=new,
        message=f"Successfully liked restaurant with id {payload['id']}",
        status=201
      ), 201
    else:
      payload = request.get_json()
      new_disliked = Dislike_Restaurant.create(
        restaurant_id=payload['id'],
        user_id=current_user.id
      )
      new = model_to_dict(new_disliked)
      new['user_id'].pop('password')

      return jsonify(
        data=new,
        message=f"Successfully disliked restaurant with id {payload['id']}",
        status=201
      ), 201


