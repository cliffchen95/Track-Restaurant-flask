from flask import Flask
from flask_login import LoginManager
import models

from resources.users import users

DEBUG=True
PORT=8000

app = Flask(__name__)
app.secret_key = "somekey"

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
  try:
    print("loading the following user")
    user = models.User.get_by_id(user_id)
    return user
  except models.DoesNotExist:
    return None
    
app.register_blueprint(users, url_prefix='/api/v1/users')

@app.route('/')
def hello_world():
  return "hello world!"

if __name__ == "__main__":
  models.initialize()
  app.run(debug=DEBUG, port=PORT)