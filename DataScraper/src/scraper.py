import os, sys
sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))
import requests
import base64
import json
from oauthlibrary.credentialutil import credentialutil

# Get Credentials
def get_credentials():
    config_path = os.path.join(os.path.split(__file__)[0], 'config' ,'account-credentials.json')
    environments = credentialutil(["DataScraper-ebay-config"])
    credential_dict = environments.load(config_path)
    return credential_dict       

# Obtain OAuth token
def get_oauth_token(client_id, client_secret):
    """
    Be sure to include reference about the lines of code below.
    https://developer.ebay.com/api-docs/static/oauth-client-credentials-grant.html
    """
    credentials = client_id + ':' + client_secret
    credentials_bytes = credentials.encode('ascii')
    b64_credentials_bytes = base64.b64encode(credentials_bytes)
    b64_credentials = b64_credentials_bytes.decode('ascii')
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + b64_credentials
    }
    body = {
        'grant_type': 'client_credentials',
        'scope': 'https://api.ebay.com/oauth/api_scope'
    }
    oauthtoken_url = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
    response = requests.post(oauthtoken_url, headers=headers, data=body)
    response.raise_for_status()
    content = json.loads(response.content)
    return content['access_token']

# Search for items
def search_items(oauth_token, keyword):
    """
    Be sure to include reference about the lines of code below.
    https://developer.ebay.com/api-docs/buy/browse/resources/item_summary/methods/search
    """
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + oauth_token
    }
    params = {
        'q': keyword, # Item type to search for.
        'limit': 3  # Number of items to return.
    }
    api_url = 'https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search'
    response = requests.get(api_url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    credentials = next(iter(get_credentials().values()))
    client_id, client_secret = credentials[0], credentials[1]
    oauth_token = get_oauth_token(client_id, client_secret)

    results = search_items(oauth_token, "Apple")

    # Print the search results
    print(json.dumps(results, indent=4))