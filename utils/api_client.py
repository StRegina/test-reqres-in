# Добавляем в консоль по очереди
# from api_client import ReqresApiClient - папка в котором хранится документ и сам документ
# client=ReqresApiClient() - создаем клиента
# resp=client.get_delayed_response(тут передеть значения через запятую) - у каждой функции свой метод

import requests
class ReqresApiClient():

    def __init__(self):
        self.base_path = 'https://reqres.in/api/'

    def request(self, method:str, path:str, data = None):
        url = self.base_path + path
        response = requests.request(method, url, data = None)
        return response

    def get_resourse(self, resourse_id: int):
        response = self.request(method = 'GET', path = f'unknown/{resourse_id}')
        return response

    def login(self, login_data: dict):
        #pload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        response = self.request(method = 'POST', path = f'login', data = login_data)
        return response

    def register(self, register_data: dict):
        #pload = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = self.request(method = 'POST', path = f'register', data = register_data)
        return response

    def get_user_page(self, page_id: int):
        response = self.request(method = 'GET', path = f'users?page={page_id}')
        return response

    def get_user(self, user_id: int):
        response = self.request('GET', f'users/{user_id}')
        return response

    def put_user(self, user_id: int, user_data: dict):
        #pload = {"name": "morpheus", "job": "zion resident"}
        response = self.request(method = 'PUT', path = f'users/{user_id}', data = user_data)
        return response

    def post_user(self, user_data: dict):
        #pload = {"name": "morpheus", "job": "leader"}
        response = self.request(method = 'POST', path = f'users', data = user_data)
        return response

    def patch_update(self, user_id: int, user_data: dict):
        #pload = {"name": "morpheus", "job": "zion resident"}
        response = self.request(method = 'PATCH', path = f'users/{user_id}', data = user_data)
        return response

    def get_delayed_answer(self, seconds: int):
        response = self.request(method = 'GET', path = f'users?delay={seconds}')
        return response
