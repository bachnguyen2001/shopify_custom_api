from requests import request
import json


class API:
    def __init__(self, store_name, access_token, api_version):
        self.store_name = store_name
        self.access_token = access_token
        self.version = api_version

    def validateJSON(self, data):
        return isinstance(data, dict)

    def __request(self, method, endpoint, data=None, params=None, **kwargs):
        url = f"https://{self.store_name}.myshopify.com/admin/api/{self.version}/{endpoint}.json"

        headers = {"X-Shopify-Access-Token": self.access_token}

        if data is not None:
            headers["Content-Type"] = "application/json"


        return request(
            method=method, url=url, params=params, json=data, headers=headers, **kwargs
        )

    def get(self, endpoint, params=None):
        # Get request
        return self.__request("GET", endpoint, params=params)

    def post(self, endpoint, data, params=None):
        # Post request
        assert self.validateJSON(data), "input data type must be JSON"
        return self.__request("POST", endpoint, data)

    def put(self, endpoint, data, params=None):
        # Put request
        assert self.validateJSON(data), "input data type must be JSON"
        return self.__request("PUT", endpoint, data)

    def delete(self, endpoint, params=None):
        # Delete request
        return self.__request("DELETE", endpoint)
