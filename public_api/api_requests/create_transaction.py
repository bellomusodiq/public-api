import requests
import json
import random
import string
from .config import base_url


def generate_random_string():
    choices = string.ascii_letters + string.digits 
    string_ = ''
    for _ in range(20):
        string_ += random.choice(choices)
    return string_


url = "{}/test/transactions".format(base_url)



def create_transaction(access_token, investor_id, instructions, 
    trade_date_limit, trade_action, trade_price_limit, trade_effective_date,
    trade_units, stock_code):

    payload = {
    "investor_id":investor_id,
    "transaction_ref":"s-{}".format(generate_random_string()),
    "cscs_number": "67393940",
    "instructions": instructions,
    "trade_date_limit": trade_date_limit,
    "trade_effective_date": trade_effective_date,
    "trade_action": trade_action,
    "trade_price_limit": str(trade_price_limit),
    "trade_units": str(trade_units),
    "stock_code": stock_code,
    "trade_account_type":"INVESTOR"
    }
    headers = {
        'authorization': 'Bearer {}'.format(access_token),
        'content-type': 'application/json'
    }


    response = requests.request("POST", url, headers=headers, data = json.dumps(payload))

    return response.json()

"""
b'{"status":200,"message":"success","trade_status":"Success","transaction_ref":"s-x12daeadvd"}'

b'{"status":400,"errors":["This Investor does not exist"]}'
"""
