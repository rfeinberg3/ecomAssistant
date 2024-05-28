from abc import ABC, abstractmethod

class Authentication(ABC):

    @abstractmethod
    def __init__(self, **environment_specifications):
        pass

    @abstractmethod
    def _load_authentication_credentials(self):
        ''' Returns list of credentials. '''
        pass

    @abstractmethod
    def _configure_credentials(self):
        ''' Returns credentials formatted as needed for authentication.  '''
        pass

    @abstractmethod
    def get_authentication_token(self):
        ''' Formats post request and returns authentication token. '''