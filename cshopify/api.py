from requests import request
import json

class API():
    
    def __init__(self, store_name, access_token, api_version):
        self.store_name = store_name
        self.access_token = access_token
        self.version = api_version
        
    def validateJSON(jsonData):
        try:
            json.loads(jsonData)
        except ValueError as err:
            return False
        return True
    
    def __request(self, method, endpoint, params, data=None, **kwargs):
        
        url = f'https://{self.store_name}.myshopify.com/admin/api/{self.version}/{endpoint}.json'

        headers = {
            "X-Shopify-Access-Token" : self.access_token
        }
        
        if data is not None:
            headers['Content-Type'] = "application/json"
        
        print(url)
            
        return request(
            method=method,
            url=url,
            params=params,
            data=data,
            headers=headers,
            **kwargs
        )
        
    def get(self, endpoint, params=None):
        # Get request
        return self.__request('GET', endpoint, params=params)
            
    def post(self, endpoint, data, params=None):
        # Post request
        assert validateJSON(data), "input data type must be JSON"   
        return self.__request('POST', endpoint, data, params=params)
    
    def put(self, endpoint, data, params=None):
        # Put request
        assert validateJSON(data), "input data type must be JSON"        
        return self.__request('PUT', endpoint, data, params=params)
        
    def delete(self, endpoint, params=None):
        # Delete request
        return self.__request('DELETE', endpoint, params=params)