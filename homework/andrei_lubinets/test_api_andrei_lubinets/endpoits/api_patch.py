import requests
import allure
from endpoits.endpoint import Endpoint


class ApiPatch(Endpoint):

    @allure.step('Partial modification of object data')
    def patch_a_object(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(f'{self.url}/{object_id}',
                                       json=payload,
                                       headers=headers
                                       )
        self.json = self.response.json()
        return self.response
