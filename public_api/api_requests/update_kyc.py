import requests
import json
from .config import base_url
from accounts.models import ApiToken


def update_kyc(api_token, id_, files):

    url = "{}/test/partners/investor/{}/kyc".format(base_url, id_)
    payload = {

    }
    files = {
        "files": files
    }
    headers = {
        'authorization': 'Bearer {}'.format(api_token),
        'content-type': 'application/json'
    }


    response = requests.request("PUT", url, headers=headers, data = json.dumps(payload))

    return response.json()

"""
b'{"status":201,"data":{"status":"Active","investor_no":7445770,"investor_id":"4d44fa7d-dbf7-4164-af87-156eb9ecdc1f"}}'

b'{"status":400,"errors":["This investor\'s BVN already exists on our platform"]}'
"""
