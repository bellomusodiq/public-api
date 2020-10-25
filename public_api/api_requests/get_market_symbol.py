import requests
import json
from .config import base_url

# category = trade, price

def get_market_symbol(access_token, category='trade'):
    print(category)
    url = "{}/market/symbols?category={}".format(base_url, category)

    payload = {
        
    }
    headers = {
        'authorization': 'Bearer {}'.format(access_token),
        'content-type': 'application/json'
    }


    response = requests.request("GET", url, headers=headers, data = json.dumps(payload))

    return response.json()

"""
b'{"status":500,"errors":["Internal server error"]}'
"""
