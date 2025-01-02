import requests
import allure
from endpoits.endpoint import Endpoint


class ApiDelete(Endpoint):
    @allure.step('Delete a post by id')
    def delete_a_post(self, post_id):
        self.response = requests.delete(f'{self.url}/{post_id}')
        self.json = self.response.json()
        print(f"Object with id {post_id} has been deleted")
        return self.response
