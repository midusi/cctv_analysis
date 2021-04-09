import requests
import json
import os
from flask import Flask, jsonify, render_template, request, redirect

app = Flask(__name__)


#The .mp4 file must locate at this file folder
#change 'people3' for the name of the video
files = {'file': open('people3.mp4', 'rb')}
url = 'http://127.0.0.1:5000/model_request'


r = requests.post(url, files=files)
print(r.status_code)
print(r.text)