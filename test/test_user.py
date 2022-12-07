import json
import httpretty
from engagesdk.engage import Engage


from engagesdk.error import EngageError
from engagesdk.user import UserResource
from test.test_base import TestBase

class TestUserResource(TestBase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.client = Engage(api_key='56ksonew', secret_key='Miwokd=wjeros')
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_format_user_object_meta_passed(self):
        data = {
            'meta': {
                'state': 'Enugu'
            },
            'first_name': 'franc',
            'last_name': 'emeka',
            'age': 40,
            'plan': 'growth',
            'is_account': True
        }
        result_data = UserResource.format_user_data(data)
        self.assertDictEqual(result_data, {
            'first_name': 'franc',
            'last_name': 'emeka',
            'is_account': True,
            'meta': {
                'age': 40,
                'state': 'Enugu',
                'plan': 'growth'
            }
        })
    
    def test_user_object_throws_error_when_list_not_array(self):
        data = {
            'meta': {
                'state': 'Enugu'
            },
            'first_name': 'franc',
            'last_name': 'emeka',
            'age': 40,
            'plan': 'growth',
            'lists': ''
        }
        with self.assertRaises(EngageError) as context:
            result_data = UserResource.format_user_data(data)
            
        self.assertTrue('Please pass an array of lists' in str(context.exception))

    """
    Test the user identify
    """
    @httpretty.activate
    def test_identify_user(self):
        uid = 'u34'
        data = {
            'id': uid,
            'first_name': 'franc',
            'last_name': 'emeka',
            'email': 'francemeka@gmail.com',
            'age': 30
        }
        expected_body = {
            'first_name': 'franc',
            'last_name': 'emeka',
            'email': 'francemeka@gmail.com',
            'meta' : {
                'age': 30
            }
        }
        def request_callback(request, uri, response_headers):
            content_type = request.headers.get('Content-Type')
            assert request.parsed_body == expected_body, 'unexpected body: {}'.format(str(request.parsed_body))
            assert content_type == 'application/json', 'expected application/json but received Content-Type: {}'.format(content_type)
            return [200, response_headers, json.dumps({'status': 'ok'})]
        
        httpretty.register_uri(
            httpretty.PUT,
            self.build_url(url= f'/users/{uid}'),
            body=request_callback
        )
        res = self.client.users.identify(data)
        self.assertTrue(res['status'])
    
    """
    Test user identify throws error when no data is passed
    """
    @httpretty.activate
    def test_identify_user(self):
        with self.assertRaises(EngageError) as context:
            res = self.client.users.identify(data={})
        
        self.assertTrue('Pass valid data to identify customer' in str(context.exception))
    
    """
    Test the user update attribute
    """
    @httpretty.activate
    def test_user_add_attribute(self):
        uid = 'u34'
        data = {
            'first_name': 'franc',
            'last_name': 'emeka',
            'email': 'francemeka@gmail.com',
            'meta': {
                'age': 40
            }
        }
        def request_callback(request, uri, response_headers):
            content_type = request.headers.get('Content-Type')
            assert request.parsed_body == data, 'unexpected body: {}'.format(str(request.parsed_body))
            assert content_type == 'application/json', 'expected application/json but received Content-Type: {}'.format(content_type)
            return [200, response_headers, json.dumps({'status': 'ok'})]
        
        httpretty.register_uri(
            httpretty.PUT,
            self.build_url(url= f'/users/{uid}'),
            body=request_callback
        )
        res = self.client.users.add_attribute(uid, data)
        self.assertTrue(res['status'])
    
    """
    Test user track event
    """
    @httpretty.activate
    def test_user_track_event_string(self):
        uid = 'u34'
        data = {
            'event': 'paid',
            'value': True
        }
        def request_callback(request, uri, response_headers):
            content_type = request.headers.get('Content-Type')
            assert request.parsed_body == data, 'unexpected body: {}'.format(str(request.parsed_body))
            assert content_type == 'application/json', 'expected application/json but received Content-Type: {}'.format(content_type)
            return [200, response_headers, json.dumps({'status': 'ok'})]
        
        httpretty.register_uri(
            httpretty.POST,
            self.build_url(url= f'/users/{uid}/events'),
            body=request_callback
        )
        res = self.client.users.track(uid, 'paid')
        self.assertTrue(res['status'])
    
    """
    Test user track event dictionary
    """
    @httpretty.activate
    def test_user_track_event_dict(self):
        uid = 'u34'
        data = {
            'event': 'paid',
            'currency': 'USD',
            'properties': {
                'plan': 'growth',
            },
            'timestamp': '2020-05-30T09:30:10Z'
        }

        expected_data = {
            'event': 'paid',
            'properties': {
                'plan': 'growth',
                'currency': 'USD'
            },
            'timestamp': '2020-05-30T09:30:10Z'
        }
        def request_callback(request, uri, response_headers):
            content_type = request.headers.get('Content-Type')
            assert request.parsed_body == expected_data, 'unexpected body: {}'.format(str(request.parsed_body))
            assert content_type == 'application/json', 'expected application/json but received Content-Type: {}'.format(content_type)
            return [200, response_headers, json.dumps({'status': 'ok'})]
        
        httpretty.register_uri(
            httpretty.POST,
            self.build_url(url= f'/users/{uid}/events'),
            body=request_callback
        )
        res = self.client.users.track(uid, data)
        self.assertTrue(res['status'])
    
    """
    Test user add to account
    """
    @httpretty.activate
    def test_user_add_to_account(self):
        uid = 'u34'
        aid = 'u10'
        data = {
            "accounts":[
                {
                    "id": aid,
                    "role": "developer"
                }
            ],
        }
        def request_callback(request, uri, response_headers):
            content_type = request.headers.get('Content-Type')
            assert request.parsed_body == data, 'unexpected body: {}'.format(str(request.parsed_body))
            assert content_type == 'application/json', 'expected application/json but received Content-Type: {}'.format(content_type)
            return [200, response_headers, json.dumps({'status': 'ok'})]
        
        httpretty.register_uri(
            httpretty.POST,
            self.build_url(url= f'/users/{uid}/accounts'),
            body=request_callback
        )
        res = self.client.users.add_to_account(user_id= uid, account_id= aid, role="developer")
        self.assertTrue(res['status'])
    
    """
    Test user remove from account
    """
    @httpretty.activate
    def test_user_remove_from_account(self):
        uid = 'u34'
        aid = 'u10'

        def request_callback(request, uri, response_headers):
            content_type = request.headers.get('Content-Type')
            return [200, response_headers, json.dumps({'status': 'ok'})]
        
        httpretty.register_uri(
            httpretty.DELETE,
            self.build_url(url= f'/users/{uid}/accounts/{aid}'),
            body=request_callback
        )
        res = self.client.users.remove_from_account(user_id= uid, account_id= aid)
        self.assertTrue(res['status'])
    
    """
    Test user change account role
    """
    @httpretty.activate
    def test_change_user_role(self):
        uid = 'u34'
        aid = 'u10'
        data = {
            "role": "developer"
        }
        def request_callback(request, uri, response_headers):
            content_type = request.headers.get('Content-Type')
            assert request.parsed_body == data, 'unexpected body: {}'.format(str(request.parsed_body))
            assert content_type == 'application/json', 'expected application/json but received Content-Type: {}'.format(content_type)
            return [200, response_headers, json.dumps({'status': 'ok'})]
        
        httpretty.register_uri(
            httpretty.PUT,
            self.build_url(url= f'/users/{uid}/accounts/{aid}'),
            body=request_callback
        )
        res = self.client.users.change_account_role(user_id= uid, account_id= aid, role="developer")
        self.assertTrue(res['status'])
    
    """
    Test convert to account
    """
    @httpretty.activate
    def test_convert_to_account(self):
        uid = 'u34'
        data = {
            "type": "account"
        }
        def request_callback(request, uri, response_headers):
            content_type = request.headers.get('Content-Type')
            assert request.parsed_body == data, 'unexpected body: {}'.format(str(request.parsed_body))
            assert content_type == 'application/json', 'expected application/json but received Content-Type: {}'.format(content_type)
            return [200, response_headers, json.dumps({'status': 'ok'})]
        
        httpretty.register_uri(
            httpretty.POST,
            self.build_url(url= f'/users/{uid}/convert'),
            body=request_callback
        )
        res = self.client.users.convert_to_account(user_id= uid)
        self.assertTrue(res['status'])
    
    """
    Test convert to customer
    """
    @httpretty.activate
    def test_convert_to_customer(self):
        uid = 'u34'
        data = {
            "type": "customer"
        }
        def request_callback(request, uri, response_headers):
            content_type = request.headers.get('Content-Type')
            assert request.parsed_body == data, 'unexpected body: {}'.format(str(request.parsed_body))
            assert content_type == 'application/json', 'expected application/json but received Content-Type: {}'.format(content_type)
            return [200, response_headers, json.dumps({'status': 'ok'})]
        
        httpretty.register_uri(
            httpretty.POST,
            self.build_url(url= f'/users/{uid}/convert'),
            body=request_callback
        )
        res = self.client.users.convert_to_customer(user_id= uid)
        self.assertTrue(res['status'])
    
    """
    Test user add account throws error when user id is empty
    """
    @httpretty.activate
    def test_add_account_empty_user_id(self):
        with self.assertRaises(EngageError) as context:
            res = self.client.users.add_to_account(user_id="",account_id="us3", role="developer")
        
        self.assertTrue('User id missing' in str(context.exception))
    
    """
    Test user add account throws error when role is not string
    """
    @httpretty.activate
    def test_add_account_role_has_to_be_string(self):
        with self.assertRaises(EngageError) as context:
            res = self.client.users.add_to_account(user_id="u4",account_id="us3", role=[''])
        
        self.assertTrue('The role has to be a string' in str(context.exception))
    

