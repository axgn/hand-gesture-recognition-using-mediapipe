import requests
import json

url = "http://127.0.0.1:5000/upload"

status = "open"

with open('template.json', 'r') as file:
    template_data = json.load(file)
    template_data["hand"] = status

requests.post(url=url,json=template_data)