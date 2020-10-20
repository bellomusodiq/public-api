import requests
import json
from .config import base_url

# category = topgainers, toplosers, news

def get_market_data(access_token, category='topgainers'):
    url = "{}/market/news?category={}".format(base_url, category)

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
