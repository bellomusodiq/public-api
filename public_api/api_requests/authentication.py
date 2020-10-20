import requests
from .config import base_url

url = "{}/token".format(base_url)


def auth():

    payload = {
        'grant_type': 'client_credentials',
        'scope': 'profile'
    }
    headers = {

    }


    response = requests.request("POST", url, headers=headers, data = payload, auth=('74kqfkms6vmv9th85pdsadv70b3g', '392777cec9b74da78a0b66e56ece058e'))

    print(response.text.encode('utf8'))
    return response.json()

    """
    b'{"status":403,"errors":["You do not have access to this resource"]}'
    """