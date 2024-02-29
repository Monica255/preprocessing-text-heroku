from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

import preprocess

class status (Resource):
    def get(self):
        try:
            return {'data': 'Api is Running'}
        except:
            return {'data': 'An Error Occurred during fetching Api'}


class Sum(Resource):
    def get(self):
        data = request.json
            # Extract the 'text' field
        text = data.get('text', 'Default Text')
        text = preprocess.preprocess_text(text)
        return jsonify({'data': text})


api.add_resource(status, '/')
api.add_resource(Sum, '/api')

if __name__ == '__main__':
    app.run()