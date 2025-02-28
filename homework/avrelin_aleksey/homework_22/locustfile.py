from locust import task, HttpUser
import random


# url = 'https://jsonplaceholder.typicode.com'
class MemeUser(HttpUser):
    token = None

    # def on_start(self):
    #
    #     response = self.client.post("/authorize", json={"name": "Aleksey"})
    #     self.token = response.json()["token"]

    @task
    def get_all_memes(self):
        self.client.get("/posts")

    @task
    def get_one_memes(self):
        self.client.get("/posts/1")

    @task
    def get_random_memes(self):
        self.client.get(f"/posts/{random.choice([21, 33, 44, 55, 66, 77, 88, 99])}")
