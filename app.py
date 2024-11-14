import urllib.parse, urllib.request, urllib.error, json
from flask import Flask
app = Flask(__name__)
@app.route('/')
def is_it_raining_in_seattle():
    rainheader = "Is it raining in Seattle? \n"
    with urllib.request.urlopen('https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
        is_it_raining_in_seattle = response.read().decode()

    if is_it_raining_in_seattle == "true":
        return rainheader + "<h1>Yes</h1>"
    else:
        return rainheader + "<h1>No</h1>"