from flask import Flask


DEBUG=True
PORT=8000

app = Flask(__name__)

@app.route('/')
def hello_world():
  return "hello world!"

if __name__ == "__main__":
  app.run(debug=DEBUG, port=PORT)