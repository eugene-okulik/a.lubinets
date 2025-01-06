import json
import requests
import allure
from endpoits.endpoint import Endpoint


class ApiGet(Endpoint):
    @allure.step('Show all objects')
    def show_all_objects(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()
        print(json.dumps(self.json, indent=4))
        return self.response
