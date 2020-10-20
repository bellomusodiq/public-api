import requests
import json
from .config import base_url

# category = topgainers, toplosers, news

def get_investors(access_token, id_=None):
    url = "{}/test/partners/investors".format(base_url)
    
    if id_:
        url = "{}/test/partners/investors/{}".format(base_url, id_)

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
