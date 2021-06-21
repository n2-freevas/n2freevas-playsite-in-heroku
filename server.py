from flask import Flask, render_template, Blueprint
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse

# import outside route file
from apis import api
app = Flask(__name__)
CORS(app)
api = Api(app)

app.register_blueprint(api.app, url_prefix = "/api")

@app.route('/', methods=["GET"])
def root():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('react.html')

@app.route('/hello')
def hello():
    return "Hello!"


if __name__ == "__main__":
    app.run()