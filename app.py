from flask import Flask,request,jsonify
from twilio.twiml.voice_response import VoiceResponse,Gather

import urllib.request
import random    

import math
from twilio.rest import Client
import json 
from geopy.geocoders import Nominatim
import os
import requests
from googletrans import Translator



account_sid = "ACb254bdb23ab7f07ab90ddf0f00386c2a"
auth_token = "cdea39faf231e78fd7cd60090875db0b"
client = Client(account_sid, auth_token)



orderAudio = ""

en  = {
        'message1':'Welcome to  Med Care',
        'message2':'In last 24hrs 9,87,909 people got 1st dose vaccination,  13,09,348 people got second dose of vaccination , making a total dose of 22,97,257 . ',
        'message3':'Please wear Mask and wash your hands regularly.',
        'message4':'Please follow  the guildlines of government and maintain social distancing',     
    }   



app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello():
    return "Hello world"


@app.route('/index',methods=['GET','POST'])
def index():
    response = VoiceResponse()
    response.say(en['message1'],voice='Polly.Aditi',language="hi-IN")
    response.say(en['message2'],voice='Polly.Aditi',language="hi-IN")
    response.say(en['message3'],voice='Polly.Aditi',language="hi-IN")
    response.say(en['message4'],voice='Polly.Aditi',language="hi-IN")
    return str(response)

if __name__ == '__main__':
    app.run(debug = True)