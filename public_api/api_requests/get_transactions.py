import requests
import json
import random
import string
from .config import base_url



url = "{}/test/transactions".format(base_url)



def get_transactions(access_token, start_date=None, end_date=None):
    print(start_date, end_date)
    headers = {
        'authorization': 'Bearer {}'.format(access_token),
        'content-type': 'application/json'
    }

    payload = {
    }

    if start_date:
        payload['start_date'] = start_date
    if end_date:
        payload['end_date'] = end_date

    response = requests.request("GET", url, headers=headers, params=payload)

    return response.json()

"""
b'{"status":200,"message":"success","trade_status":"Success","transaction_ref":"s-x12daeadvd"}'

b'{"status":400,"errors":["This Investor does not exist"]}'
"""
