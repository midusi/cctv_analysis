import requests
import json
import os
from flask import Flask, jsonify, render_template, request, redirect


app = Flask(__name__)

@app.route("/client_response", methods=['POST'])
def client_response():
    if request.method == "POST":
        f = request.json
        print(f)
    return 'ok'


