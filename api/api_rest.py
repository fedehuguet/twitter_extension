#import os
from flask import Flask, request
from flask_restful import Resource, Api
from keys import consumer_key, consumer_secret, access_token, access_secret

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, id):
        return {
            'id': id,
            'name':todos[id]
            }

    def put(self, id):
        todos[id] = request.form['data']
        return {
            'id': id,
            'name':todos[id]
            }

api.add_resource(TodoSimple, '/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)