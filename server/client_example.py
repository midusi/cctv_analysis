import requests
import json

url = 'http://127.0.0.1:5000/model_request'
files = {'file': open('people3.mp4', 'rb')}

r = requests.post(url, files=files)
print(r.status_code)
print(r.text)