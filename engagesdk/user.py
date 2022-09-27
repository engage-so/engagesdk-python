import re
from engagesdk.base import EngageBase
from engagesdk.error import EngageError


class UserResource(EngageBase):

    """
    :param data: The data to identify the user with
    :type data: dict
    """
    @classmethod
    def identify(cls, data):
        if not data:
            raise EngageError("Pass valid data to identify customer")
        
        if 'id' not in data:
            raise EngageError("Pass a valid ID")

        if 'email' in data:
            # verify email
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if (not re.fullmatch(regex, data['email'])):
                raise EngageError("The email address is not valid")
        
        formatted_data = UserResource.format_user_data(data)
        id = formatted_data.pop('id')
        url = f'/users/{id}'
        print(EngageBase)

        return cls().requests.put(url, data=formatted_data)

    """
    Add user attributes

    :param data: The data to identify the user with
    :type data: dict
    """
    @classmethod
    def add_attribute(cls, uid, data):
        if not data:
            raise EngageError("Pass valid data to identify customer")
        

        if 'email' in data:
            # verify email
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if (not re.fullmatch(regex, data['email'])):
                raise EngageError("The email address is not valid")
        
        formatted_data = UserResource.format_user_data(data)
        url = f'/users/{uid}'
        
        return cls().requests.put(url, data=formatted_data)
    
    """
    Add user attributes

    :param data: The data to identify the user with
    :type data: dict
    """
    @classmethod
    def track(cls, uid, data):
        if not data or not (isinstance(data, str) or isinstance(data, dict)):
            raise EngageError("Please pass in an event string or object")
        
        if isinstance(data, str):
            formatted_data = {
                'event': data,
                'value': True
            }
        else:
            if not 'event' in data:
                raise EngageError("Event must be present in data")
            formatted_data = {
                'properties': {}
            }
            standard = ['event', 'value', 'timestamp']
            for attr in data:
                if attr in standard:
                    formatted_data.update({attr: data[attr]})
                    continue
                if attr == 'properties':
                    continue
                formatted_data['properties'].update({attr: data[attr]})
            
            if 'properties' in data:
                formatted_data['properties'].update(data['properties'])

            if not formatted_data['properties']:
                del formatted_data['properties']
        
        url = f'/users/{uid}/events'

        return cls().requests.post(url, data=formatted_data)
        
    
    """
    Takes in Data and formats it to fit engage standard and meta attribute structure
    :param data: The data to be formatted
    :type data: dict
    """
    @staticmethod
    def format_user_data(data):
        standard_attributes = ['id','email','number','first_name','last_name','device_token','device_platform','created_at']
        formatted_data = {
            'meta': {}
        }
        for attr in data:
            if attr in standard_attributes:
                formatted_data.update({attr: data[attr]})
                continue
            if attr == 'meta':
                continue
            formatted_data['meta'].update({attr: data[attr]})
        
        if 'meta' in data:
            formatted_data['meta'].update(data['meta'])

        if not formatted_data['meta']:
            del formatted_data['meta']
        
        return formatted_data