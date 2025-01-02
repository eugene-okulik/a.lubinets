import requests
import allure
from endpoits.endpoint import Endpoint


class ApiPut(Endpoint):
    @allure.step('Complete modification of post data')
    def put_a_post(self, post_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/{post_id}',
                                     json=payload,
                                     headers=headers
                                     )
        self.json = self.response.json()
        return self.response
