import requests
import json
from .config import base_url





def cancel_transaction(access_token, transaction_ref):

    url = "{}/test/transactions/{}".format(base_url, transaction_ref)

    payload = {
    
    }
    headers = {
        'authorization': 'Bearer {}'.format(access_token),
        'content-type': 'application/json'
    }


    response = requests.request("DELETE", url, headers=headers)

    return response.json()

"""
b'{"status":200,"message":"success","trade_status":"Success","transaction_ref":"s-x12daeadvd"}'

b'{"status":400,"errors":["This Investor does not exist"]}'
"""
