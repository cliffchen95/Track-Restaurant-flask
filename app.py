from flask import Flask, jsonify
from flask_login import LoginManager
from flask_cors import CORS
import models

from resources.users import users
from resources.restaurants import restaurants

DEBUG=True
PORT=8000

app = Flask(__name__)
app.secret_key = "somekey"

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
  try:
    user = models.User.get_by_id(user_id)
    return user
  except models.DoesNotExist:
    return None

@login_manager.unauthorized_handler
def unauthorized():
  return jsonify(
    data={
      'error': 'User not logged in'
    },
    message="You must be logged in to access that resource",
    status=401
  ), 401

CORS(users, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(restaurants, url_prefix='/api/v1/restaurants')

@app.route('/')
def hello_world():
  return "hello world!"

if __name__ == "__main__":
  models.initialize()
  app.run(debug=DEBUG, port=PORT)