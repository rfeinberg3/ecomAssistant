# -*- coding: utf-8 -*-
"""
Copyright 2019 eBay Inc.
 
Licensed under the Apache License, Version 2.0 (the "License");
You may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,

WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

See the License for the specific language governing permissions and
limitations under the License.
"""
# I used the general framework of eBays credentialutil.py program but cut out all unused functions. I also refactored it as class object with an init fucntion. 

import json

class credential_util():
    """
    credential_list: dictionary key=string, value=credentials
    """
    def __init__(self, environments):
        self.environments = environments

    def load(self, app_config_path):
        with open(app_config_path, 'r') as file:
            if app_config_path.endswith('.json'):
                content = json.loads(file.read())
            else:
                raise ValueError('Configuration file needs to be a JSON file')
            credential_dict = self._iterate(content)
        return credential_dict

    def _iterate(self, content):
        for key in content:
            if key in self.environments:     
                client_id = content[key]['appid']
                dev_id = content[key]['devid']
                client_secret = content[key]['certid']
                ru_name = content[key]['redirecturi']
                app_info = (client_id, client_secret, dev_id, ru_name)
                return {key: app_info}
 
    
    
