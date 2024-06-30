import base64
import requests
import json
from typing import TypeVar, Union
from .util import util

# Environments
SANDBOX = 'SANDBOX'
PRODUCTION = 'PRODUCTION'

class oauth:
    '''
      Class to parse your keyset credentials and return an oauth authentication token, \n
    allow you to make API calls with eBay's APIs.

    Args:  
        environement (str): 'SANDBOX' or 'PRODUCTION' for sandbox or production keyset respectively.
        keyset (str): Name of your keyset.
        keysetConfigPath (str): Path to you keyset config file containing your keyset credentails.
    '''
    def __init__(
            self,
            environment: str,
            keyset: str,
            keysetConfigPath: str,
        ) -> None:
        self.environment = environment
        self.keyset = keyset
        self.keysetConfigPath = keysetConfigPath

    # Obtain OAuth token
    def get_authentication_token(self) -> str:
        '''
          Formats a post request to eBay's oauthentication API to receive an oauth token, \n
        The token is used for authenticating you application keyset.

        To see how to setup this pipeline for yourself, see the link below: \n
        https://developer.ebay.com/api-docs/static/oauth-client-credentials-grant.html

        Returns:
            Access token as a hashed string.
        '''
        # Format post request
        b64Credentials = self._configure_credentials()
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic ' + b64Credentials
        }
        body = {
            'grant_type': 'client_credentials',
            'scope': 'https://api.ebay.com/oauth/api_scope' # Only this default scope is needed for the Buy->Browse->search call. Other API calls might need additional scopes.
        }
        if self.environment == SANDBOX:
            oauthtokenUrl = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
        elif self.environment == PRODUCTION:
            oauthtokenUrl = "https://api.ebay.com/identity/v1/oauth2/token"
        else:
            raise ValueError("environment parameter must either 'SANDBOX' or 'PRODUCTION'.")
        # Post request to obtain OAuth token
        response = requests.post(oauthtokenUrl, headers=headers, data=body)
        response.raise_for_status() # Raise error if post request fails
        content = json.loads(response.content)
        return content['access_token']

    def _configure_credentials(self):
        ''' Format keyset credentials for POST request to eBay oauth API. '''
        credentialDict = self._load_authentication_credentials()
        if len(credentialDict) == 1:
            credentials = credentialDict[self.keyset]
            clientId = credentials[0]
            clientSecret = credentials[2] 
            # Format credentials according to ebay documentation
            credentials = clientId + ':' + clientSecret
            credentialsBytes = credentials.encode('ascii')
            b64CredentialsBytes = base64.b64encode(credentialsBytes)
            return b64CredentialsBytes.decode('ascii')
        else:
            raise Exception("Credential config not properly formatted, should only contain one keyset.")
        
    def _load_authentication_credentials(self) -> dict: 
        ''' Call credential util and load keyset credentials. '''
        return util(self.keyset, self.keysetConfigPath).credential_dict()
