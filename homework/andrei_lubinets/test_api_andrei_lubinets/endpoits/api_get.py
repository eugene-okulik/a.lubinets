import requests
import allure
from endpoits.endpoint import Endpoint


class ApiGet(Endpoint):
    @allure.step('Show all posts')
    def show_all_posts(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()
        print(self.response.text)
        return self.response
