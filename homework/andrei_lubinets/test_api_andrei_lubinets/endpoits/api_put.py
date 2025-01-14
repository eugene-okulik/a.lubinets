import requests
import allure
from endpoits.endpoint import Endpoint


class ApiPut(Endpoint):
    @allure.step('Complete modification of object data')
    def put_a_object(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/{object_id}',
                                     json=payload,
                                     headers=headers
                                     )
        self.json = self.response.json()
        return self.response
