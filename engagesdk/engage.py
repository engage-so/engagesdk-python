from engagesdk.base import EngageBase
from engagesdk.error import EngageError
from engagesdk.user import UserResource


class Engage:
   def __init__(self, api_key='', secret_key='') -> None:
        if not api_key or not secret_key:
            raise EngageError("Please pass valid API and Secret Key")
        EngageBase(public_key = api_key, secret_key = secret_key) 

        self.users = UserResource