import requests
import engagesdk as api
class Borg:
    """Borg class making class attributes global"""
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class EngageBase(Borg):
    """Base Class used across defined."""

    def __init__(self, **kwargs):
        Borg.__init__(self)
        public_key = kwargs.get('public_key')
        secret_key = kwargs.get('secret_key')
        arguments = dict(api_url=api.API_URL, username = public_key, password = secret_key)
        
        if not hasattr(self, 'requests'):
            req = EngageRequests(**arguments)
            self._shared_state.update(requests=req)


class EngageRequests:

    def __init__(self, api_url, username, password) -> None:
        self.API_BASE_URL = f'{api_url}'
        self.AUTH = (username, password)

    """
    Make a request to the Engage API
	
    :param method: request method to use from the Request library
    :type: func
    :param url: resource url to send the request to
    :type: string
    """
    def _request(self, method, url, **kwargs):
        data = kwargs.get('data')
        qs = kwargs.get('qs')

        response = method(
            self.API_BASE_URL + url,
            json=data, auth= self.AUTH,
            params=qs
        )
        return response.json()

    """
    get a resource
	
    :param endpoint: resource endpoint
    :type: string
    """
    def get(self, endpoint, **kwargs):
        """get a resource.
        args:
            endpoint: resource endpoint.
        """
        return self._request(requests.get, endpoint, **kwargs)

    """
    Post a resource
	
    :param endpoint: resource endpoint
    :type: string
    """
    def post(self, endpoint, **kwargs):
        return self._request(requests.post, endpoint, **kwargs)

    """
    Put a resource
	
    :param endpoint: resource endpoint
    :type: string
    """
    def put(self, endpoint, **kwargs):
        return self._request(requests.put, endpoint, **kwargs)
    
    """
    Delete a resource
	
    :param endpoint: resource endpoint
    :type: string
    """
    def delete(self, endpoint, **kwargs):
        return self._request(requests.delete, endpoint, **kwargs)