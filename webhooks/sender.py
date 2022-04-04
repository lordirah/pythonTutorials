import json

import requests

webhook_url = "http://127.0.0.1:5000/webhook"

data = {'name': 'Hariharan', 'address': 'test address'}

r = requests.post(
    webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'}
)
