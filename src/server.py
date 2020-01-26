from flask import Flask, request, jsonify , make_response 
import datetime
from prediction import *
from database import *

import json


app = Flask("andrew")


@app.route('/chat', methods =['POST'])
def chatService():
    clientMessage = request.get_json()
    print (clientMessage)
    print (clientMessage['Message'])
    botResponse = chat(clientMessage['Message'])
    return botResponse


if __name__ == '__main__':
    app.run(debug=False)