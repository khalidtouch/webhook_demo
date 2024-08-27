import json 
import requests 

webhook_url = 'https://webhook.site/82a52c78-f1e0-4cd6-a722-e605a314461b'

data = {
    'name': 'Adams Brown',
    'address': '23 Orion Street',
    'location': '2334,345',
    'webhook_message': 'Webhooks are fun to use, wow!'
}

headers = {
    'Content-Type': 'application/json'
}

r = requests.post(webhook_url, data=json.dumps(data), headers=headers)
