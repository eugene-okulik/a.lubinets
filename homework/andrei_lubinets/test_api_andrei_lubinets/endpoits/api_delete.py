import requests
import allure
from endpoits.endpoint import Endpoint


class ApiDelete(Endpoint):

    @allure.step('Delete a object by id')
    def delete_a_object(self, object_id):
        self.response = requests.delete(f'{self.url}/{object_id}')
        print(f"Object with id {object_id} has been deleted")
