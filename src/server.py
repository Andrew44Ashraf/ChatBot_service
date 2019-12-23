from flask import Flask, request, jsonify , make_response 
import datetime
from prediction import *


import json


app=Flask("andrew");







@app.route('/messaging', methods =['GET','POST'])
def chatService():
    clientMessage = request.get_json();
    print (clientMessage)
    print (clientMessage['Message'])
    botResponse = chat(clientMessage['Message']);
    return botResponse;




















if __name__ == '__main__':
    app.run(debug=False)