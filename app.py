from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS #comment this on deployment
from ApiHandler import ApiHandler

app = Flask(__name__, static_url_path='', static_folder='health-watch/build')
CORS(app) #comment this on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(ApiHandler, '/flask/ml')
