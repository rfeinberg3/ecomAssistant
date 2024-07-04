import json

class Util():
    '''
      Extracts the list of keyset credentials from your app config file. \n
    You can generate a keyset on eBay's developer page here: https://developer.ebay.com/my/keys. \n
    You must place your keysets into the keyset_config.json file with the following format: \n
    { \n
    "Keyset-Name": 
        {
        "appid": "Client-ID",
        "devid": "Developer-ID",
        "certid": "Client-SecretKey",
        "redirecturi": "Redirect-URI" \n
        }
    }

    Args:  
        keyset (str): Name of your keyset
        keysetConfigPath (str): Path to you keyset config file containing your keyset credentails.
            format: Path/To/Your/keyset_config.json
    '''
    def __init__(self, keyset: str, keysetConfigPath: str) -> None:
        self.keyset = keyset
        self.keysetConfigPath = keysetConfigPath

    def credential_dict(self) -> dict:
        '''
          Loads json file and parses your self.keyset credentials \n 
        from the keyset_config.json file.

        Returns:
            A dictionary with key="name_of_keyset", value=tuple(credentials).
        '''
        with open(self.keysetConfigPath, 'r') as file:
            if self.keysetConfigPath.endswith('.json'):
                content = json.loads(file.read())
            else:
                raise ValueError('Configuration file needs to be a JSON file')
            credentialDict = self._iterate(content)
        return credentialDict

    def _iterate(self, content: json) -> dict:
        '''
          Iterate through the keyset config file to find its credentials.
        
        Args:
            content: json object with keyset credentials
        Returns:
            A dictionary with key="name_of_keyset", value=tuple(credentials). 
        '''
        for key in content:
            if key in [self.keyset]:     
                clientId = content[key]['appid']
                devId = content[key]['devid']
                clientSecret = content[key]['certid']
                ruName = content[key]['redirecturi']
                credentialInfo = (clientId, devId, clientSecret, ruName)
                return {key: credentialInfo}
 
    
    
