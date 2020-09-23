# Добавляем в консоль по очереди
# from api_client import ReqresApiClient - папка в котором хранится документ и сам документ
# client=ReqresApiClient() - создаем клиента
# resp=client.get_delayed_response(тут передеть значения через запятую) - у каждой функции свой метод

import requests
class ReqresApiClient():

    def __init__(self):
        self.base_path = 'https://reqres.in/api/'

    def request(self, method:str, path:str, data=None):
        url = self.base_path + path
        response = requests.request(method, url)
        return response

    def get_resourse(self, resourse_id: int):
        response = self.request('GET', 'unknown/{resourse_id}')
        return response

    def login(self, data: dict):
        #pload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        response = self.request('POST','login', data)
        return response

    def register(self, data: dict):
        #pload = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = self.request('POST','register', data)
        return response

    def users(self, user_id: int, data: dict):
        #pload = {"name": "morpheus", "job": "zion resident"}
        response = self.request('PUT','users/{user_id}', data)
        return response

    def delayed(self, delayed_id: int, data: dict):
        response = self.request('GET', 'users?delay={delayed_id}')
        return response

    def users_page(self, page_id: int, data: dict):
        response = self.request('GET', 'users?page={page_id}')
        return response