from server.controllers.PseudocodeToC import PseudocodeToC
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

app = Flask(__name__)

CORS(app)

api = Api(app)

@app.route('/')
def index():
    return '200 OK'

api.add_resource(PseudocodeToC, '/pseudocode-to-c')

if __name__ == '__main__':
    app.run(debug=True)