import json
from bson import json_util
from markupsafe import escape
from flask import Flask, request
from pymongo import MongoClient


def get_database():
    # MongoDB connection URL
    CONNECTION_STRING = "mongodb://localhost:27017"

    # Create a connection using MongoClient
    client = MongoClient(CONNECTION_STRING)

    client = client.deepak_api_test

    return client

def get_data_from_db(state):
    client = get_database()
    state = str(state)
    data = client.test_api.find_one({"State": {"$in": [state]}})
    return data

app = Flask(__name__)
@app.route('/basic_api/flask_rest_api')

def run_test_api():
    return 'flask_rest_api'

def insert_data_to_db(data):
    client = get_database()
    response = client.test_api.insert_many(data)
    insert_cnt = len(response.inserted_ids)
    return str(insert_cnt) + ' records inserted in DB successfully'

def delete_data_from_db(status):
    client = get_database()
    response = client.test_api.delete_many({"Status": {"$in": [status]}})
    del_cnt = response.deleted_count
    return str(del_cnt) + ' records deleted from DB successfully'

@app.route('/basic_api/entities', methods=['GET', 'POST', 'DELETE'])
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
        data = request.json
        print(data['in_data'])
        status_msg = insert_data_to_db(data['in_data'])
        return {
            'message': status_msg,
            'method': request.method
        }
    if request.method == "DELETE":
        status = request.args.get(('Status'))
        print(status)
        status_msg = delete_data_from_db(status)
        return {
            'message': status_msg,
            'method': request.method
        }