from flask import Flask, request, jsonify , make_response 
import datetime
from prediction import *


import json


app=Flask(__name__);







@app.route('/messaging', methods =['GET','POST'])
def chatService():
    clientMessage = request.get_json();

    print clientMessage['Message'];
    botResponse = chat(clientMessage['Message']);
    return botResponse;




















if __name__ == '__main__':
    app.run(debug=True)