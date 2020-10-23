import requests
import json
from .config import base_url
from accounts.models import ApiToken


def update_investor(api_token, id_, title, surname, first_name, 
                    other_names, gender, phone, 
                    date_of_birth, email_address,
                    address, country, state, 
                    nationality, city, 
                    bank_account_number, 
                    bank_account_name,
                    bank_code, 
                    branch_code, acc_type,
                    company_name, 
                    next_of_kin_name):

    url = "{}/test/partners/investor/{}".format(base_url, id_)
    payload = {
        "personal":{
            "title": title,
            "surname": surname,
            "firstname": first_name,
            "othernames": other_names,
            "gender": gender,
            "phone": phone,
            "date_of_birth": date_of_birth,
            "email_address": email_address
        },
        "location":{
            "address": address,
            "country": country,
            "nationality": nationality,
            "state": state,
            "city": city
        },
        "financial":{
            "bank_account_number": bank_account_number,
            "bank_account_name": bank_account_name,
            "bank_code": bank_code,
            "branch_code": branch_code,
            "acc_type": acc_type
        },
        "employment":{
            "companyName": company_name
        },
        "next_of_kin":{
            "name": next_of_kin_name
        }
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
