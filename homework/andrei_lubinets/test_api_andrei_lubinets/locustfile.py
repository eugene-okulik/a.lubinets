from locust import task, HttpUser
from endpoits.endpoint import Endpoint


class ObjectUser(HttpUser, Endpoint):
    id = None
    token = None

    def on_start(self):
        response = self.client.post('/object',
                                    json={'data': {'color': 'yellow', 'size': 'large'}, "name": "My bike"},
                                    headers=self.headers
                                    )
        self.id = response.json()['id']

# оставил для примера авторизации
    # def on_start(self):
    #     response = self.client.post(
    #         '/authorize',
    #         json={'login': 'Andrei',
    #         'password': '1241fsdg',
    #         'admin': false
    #         }
    #     )
    #     self.token = response.json()['token']

    @task(5)
    def get_all_objects(self):
        self.client.get('/object')

    @task(4)
    def get_one_object(self):
        self.client.get('/object/1')

    @task(3)
    def patch_object(self):
        payload = {'data': {'color': 'yellow', 'size': 'large'}, "name": "My car"}
        self.client.patch(f'/object/{self.id}',
                          json=payload,
                          headers=self.headers
                          )

    @task(2)
    def put_object(self):
        payload = {'data': {'color': 'red', 'size': 'big'}, "name": "My yacht"}
        self.client.put(f'/object/{self.id}',
                        json=payload,
                        headers=self.headers
                        )

    @task
    def delete_object(self):
        self.client.delete(f'/object/{self.id}')
