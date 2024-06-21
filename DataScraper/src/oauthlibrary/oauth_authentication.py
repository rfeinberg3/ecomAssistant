#import os, sys
#sys.path.append('..')
import base64
import requests
import json
from oauthlibrary.credential_util import credential_util
from abstracts import Authentication as Authentication

class oauth_authentication(Authentication):
    def __init__(self, environment='sandbox', keyset_list=["DataScraper-ebay-config"]):
        self.environment = environment
        self.keyset_list = keyset_list

    # call credential util
    def _load_authentication_credentials(self): 
        config_path = '../src/config/account-credentials.json'
        environments = credential_util(self.keyset_list) # 
        credential_list = environments.load(config_path)
        return credential_list

    def _configure_credentials(self):
        credential_list = self._load_authentication_credentials()
        if len(credential_list) == 1:
            credentials = next(iter(credential_list.values())) 
            client_id = credentials[0]
            client_secret = credentials[1] 
            # Format credentials according to ebay documentation
            credentials = client_id + ':' + client_secret
            credentials_bytes = credentials.encode('ascii')
            b64_credentials_bytes = base64.b64encode(credentials_bytes)
            return b64_credentials_bytes.decode('ascii')
        else:
            raise Exception("Credential config not properly formatted, should only contain one keyset.")

    # Obtain OAuth token
    def get_authentication_token(self):
        """
        Be sure to include reference about the lines of code below.
        https://developer.ebay.com/api-docs/static/oauth-client-credentials-grant.html
        """
        # Format post request
        b64_credentials = self._configure_credentials()
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic ' + b64_credentials
        }
        body = {
            'grant_type': 'client_credentials',
            'scope': 'https://api.ebay.com/oauth/api_scope' # Only this default scope is needed for the Buy->Browse->search call. Other API calls might need additional scopes.
        }
        oauthtoken_url = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
        # Post request to obtain OAuth token
        response = requests.post(oauthtoken_url, headers=headers, data=body)
        response.raise_for_status() # Raise error if post request fails
        content = json.loads(response.content)
        return content['access_token'] 
