from flask import Flask, request, jsonify , make_response 
from prediction import *
from database import *
from utilities import *

import datetime
import json

app = Flask("andrew")
accepted_passwords = ['THIS', 'SHOULD', 'HAVE', 'ALL', 'ACCEPTED', 'PASSWORDS']


# Takes a password in JSON format with key 'password' in exchange for a token in JSON
@app.route('/register', methods=['POST'])
def register():
    post_data = request.get_json()
    password = post_data['password']

    if password in accepted_passwords:
        access_token = generate_token()
        save_token(access_token)

        return make_response(jsonify(access_token=access_token), 200)
    else:
        return make_response(jsonify(error='Incorrect Password.'), 401)


# Views clusters or creates a cluster for a given token in JSON given a token with key 'token'
# the POST request body should also provide the keys 'tag', 'patterns' & 'responses'
# To view clusters, the token is attached in a query string. Example: '?token=TOKENSTRING'
@app.route('/cluster', methods=['GET', 'POST'])
def create_read_cluster():
    if request.method == 'GET':
        token = request.args.get('token')

        if not token_exists(token):
            return make_response(jsonify(error='Invalid Token.'), 401)
        
        clusters = get_clusters(token)

        return make_response(jsonify(clusters=clusters), 200)

    else: # POST request
        post_data = request.get_json()
        token = post_data['token']

        if not token_exists(token):
            return make_response(jsonify(error='Invalid Token.'), 401)
        
        if 'tag' not in post_data or 'patterns' not in post_data or 'responses' not in post_data:
             return make_response(jsonify(error='Invalid or incomplete data.'), 400)
        
        tag = post_data['tag']
        patterns = post_data['patterns']
        responses = post_data['responses']

        save_cluster(token, tag, patterns, responses)
        
        return make_response(jsonify(status='Cluster saved successfully.'), 200)


# Takes a token from the query string then trains the chatbot model using the token's stored clusters if any
@app.route('/train', methods=['GET'])
def train_model():
    token = request.args.get('token')

    if not token_exists(token):
        return make_response(jsonify(error='Invalid Token.'), 401)
    
    clusters = get_clusters(token) # I don't know the return format so this should be changed or tested first

    # PLACEHOLDER FOR A MODULARIZED TRAINING FUNCTION

    return make_response(jsonify(status='Model trained successfully.'), 200)


# Takes a message and token in JSON format with keys 'message' & 'token' in exchange for a reply in JSON
@app.route('/chat', methods=['POST'])
def chat():
    post_data = request.get_json()
    token = post_data['token']
    message = post_data['message']

    if token_exists(token)
        bot_response = chat(message, token)

        return jsonify(response=bot_response)
    else:
        return make_response(jsonify(error='Invalid Token.'), 401)


if __name__ == '__main__':
    app.run(debug=False)