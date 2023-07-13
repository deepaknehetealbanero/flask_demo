# main.py
from flask import Flask, request
from pymongo import MongoClient


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://localhost:27017"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    client = client.deepak_api_test

    return client

def get_data_from_db(state):
    client = get_database()
    state = str(state)
    data = client.test_api.find_one({"State": {"$in": [state]}})
    return data

from markupsafe import escape

app = Flask(__name__)
@app.route('/basic_api/flask_rest_api')

def run_test_api():
    return 'flask_rest_api'

@app.route('/basic_api/entities', methods=['GET', 'POST'])
def entities():
    if request.method == "GET":
        state = request.args.get('State')
        data = get_data_from_db(state)
        print(data)
        return {
            'message': "Data Requested: " + str(data),
            'method': request.method
        }
    if request.method == "POST":
        return {
            'message': 'This endpoint should create an entity',
            'method': request.method,
		'body': request.json
        }