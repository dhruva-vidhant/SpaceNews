from flask import Flask

app = Flask(__name__)




@app.route('/<json>')
def index(json):
    file_object = open("email.json", "w")
    file_object.write(json)

@app.route('/')
def read():
  reader = open("email.json", "r")
  return reader.read()

app.run(host='0.0.0.0', port=81)
