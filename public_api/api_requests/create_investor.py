import requests
import json
from .config import base_url
from accounts.models import ApiToken

url = "{}/test/partners/investors".format(base_url)

def create_investor(api_token, title, surname, first_name, 
                    other_names, gender, phone, 
                    date_of_birth, email_address, home_phone,
                    address, country, state, 
                    nationality, state_of_origin, city, 
                    lga, bank_account_number, bank_name, 
                    bank_account_name,
                    bank_code, bvn, company_name, employment_type, occupation, identity_type, identity_number, expiry_date,
                    politically_exposed, next_of_kin_name, next_of_kin_address, next_of_kin_email, next_of_kin_phone_number, next_of_kin_relationship):
    print(api_token)
    payload = {
        "personal":{
            "title": title,
            "surname": surname,
            "first_name": first_name,
            "other_names": other_names,
            "gender": gender,
            "phone": phone,
            "date_of_birth": date_of_birth,
            "email_address": email_address,
            "home_phone": home_phone
        },
        "location":{
            "address": address,
            "country": country,
            "state": state,
            "nationality": nationality,
            "state_of_origin": state_of_origin,
            "city": city,
            "lga": lga
        },
        "financial":{
            "bank_account_number": bank_account_number,
            "bank_account_name": bank_account_name,
            "bank_name": bank_name,
            "bank_code": bank_code,
            "bvn": bvn
        },
        "employment":{
            "company_name": company_name,
            "employment_type": employment_type,
            "occupation": occupation
        },
        "kyc":{
            "identity_type": identity_type,
            "identity_number": identity_number,
            "expiry_date": expiry_date,
            "politically_exposed": politically_exposed
        },
        "next_of_kin":{
            "name": next_of_kin_name,
            "address": next_of_kin_address,
            "email": next_of_kin_email,
            "phone_number": next_of_kin_phone_number,
            "relationship": next_of_kin_relationship
        }
    }
    headers = {
        'authorization': 'Bearer {}'.format(api_token),
        'content-type': 'application/json'
    }


    response = requests.request("POST", url, headers=headers, data = json.dumps(payload))

    return response.json()

"""
b'{"status":201,"data":{"status":"Active","investor_no":7445770,"investor_id":"4d44fa7d-dbf7-4164-af87-156eb9ecdc1f"}}'

b'{"status":400,"errors":["This investor\'s BVN already exists on our platform"]}'
"""
