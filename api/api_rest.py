#import os
import tweepy
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
from flask import Flask, request
from flask_restful import Resource, Api
from keys import consumer_key, consumer_secret, access_token, access_secret

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

app = Flask(__name__)
api = Api(app)
api_tweepy = tweepy.API(auth)

class Search(Resource):
    def put(self, id):
        query = request.form['data']
        twitter_stream.filter(track=[query])
        return {
            'id': id,
            'name':'Succesful query!'
            }

class MyListener(StreamListener):
    def __init__(self):
        self.counter = 0
        self.limit = 10
    
    def on_data(self, data):
        try:
            with open('tweet_history.json', 'a') as f:
                f.write(data)
                self.counter += 1
                if self.counter < self.limit:
                    return True
                else:
                    twitter_stream.disconnect()
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
api.add_resource(Search, '/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)