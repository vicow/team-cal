from flask import Flask, render_template, json
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from bson import json_util

def mongo_json(data):
    return json.dumps(data, default=json_util.default)


app = Flask(__name__)
api = Api(app)


app.config['MONGO_DBNAME'] = "team-cal"
app.config['MONGO_HOST'] = "192.168.99.100"
app.config['MONGO_PORT'] = 27017

mongo = PyMongo(app)

class Event(Resource):
    def get(self, event_id):
        event = mongo.db.event.find_one_or_404({'_id': event_id})
        print(event)
        return mongo_json({'event': event})

api.add_resource(Event, '/event/<ObjectId:event_id>')

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)