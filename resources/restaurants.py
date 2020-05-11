import models

Like_Restaurant = models.Like_Restaurant
Dislike_Restaurant = models.Dislike_Restaurant

from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from playhouse.shortcuts import model_to_dict
restaurants = Blueprint('restaurants', 'restaurants')

@restaurants.route('/', methods=['GET'])
def restaurant():
  return "hello restaurant"