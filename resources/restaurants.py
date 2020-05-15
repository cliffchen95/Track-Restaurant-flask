import models

Like_Restaurant = models.Like_Restaurant
Dislike_Restaurant = models.Dislike_Restaurant

from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from playhouse.shortcuts import model_to_dict
restaurants = Blueprint('restaurants', 'restaurants')

@restaurants.route('/', methods=['POST', 'GET'])
@login_required
def restaurant():
  if request.method == 'POST':
    if request.headers['like'] == 'true':
      payload = request.get_json()
      new_liked = Like_Restaurant.create(
        restaurant_id=payload['id'],
        name=payload['name'],
        address=payload['address'],
        picture=payload['picture'],
        user_id=current_user.id,
        url=payload['url'],
        cuisine=payload['cuisine']
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

  if request.method == 'GET':
    liked_ones = Like_Restaurant.select().where( Like_Restaurant.user_id == current_user.id )
    likes = [model_to_dict(like) for like in liked_ones]
    for like in likes:
      (like['user_id']).pop('password')
    disliked_ones = Dislike_Restaurant.select().where( Dislike_Restaurant.user_id == current_user.id )
    dislikes = [model_to_dict(dislike) for dislike in disliked_ones]
    for dislike in dislikes:
      (dislike['user_id']).pop('password')
    return jsonify(
      data={ "like_restaurants": likes, "dislike_restaurants": dislikes },
      message=f"Found {len(likes)} likes and {len(dislikes)} dislikes",
      status=200
    ), 200

