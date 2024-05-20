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
 
    
    