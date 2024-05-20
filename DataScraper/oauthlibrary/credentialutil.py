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
# Will most likely completely refactor this and remove the licensing.

import yaml, json
import logging

class credentialutil():
    """
    credential_list: dictionary key=string, value=credentials
    """
    def __init__(self, environments=None):
        self._credential_list = {}
        self.environments = environments

    def load(self, app_config_path):
        logging.info("Loading credential configuration file at: %s", app_config_path)
        with open(app_config_path, 'r') as f:
            if app_config_path.endswith('.yaml') or app_config_path.endswith('.yml'):
                content = yaml.load(f)
            elif app_config_path.endswith('.json'):
                content = json.loads(f.read())
            else:
                raise ValueError('Configuration file need to be in JSON or YAML')
            self._iterate(content)
        return self._credential_list  

    def _iterate(self, content):
        for key in content:
            logging.debug("Environment attempted: %s", key)
            if key in self.environments:     
                client_id = content[key]['appid']
                dev_id = content[key]['devid']
                client_secret = content[key]['certid']
                ru_name = content[key]['redirecturi']
                app_info = (client_id, client_secret, dev_id, ru_name)
                self._credential_list = {key: app_info}
 
    
    
