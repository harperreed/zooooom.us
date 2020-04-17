#!/usr/bin/python3

import requests
import json
import subprocess

def fetch_config():
    url = "https://zooooom.us/config.json"
    response = requests.get(url)
    contents = response.text
    config = json.loads(contents)
    return config

config = fetch_config()
urls = config["videos"]
for u in urls:
    result = subprocess.run(["/usr/local/bin/mediastreamvalidator", u])
    if result.returncode != 0:
        print("**** broken: " + u + " ******")
