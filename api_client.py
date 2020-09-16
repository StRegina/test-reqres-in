# Добавляем в консоль по очереди
# from api_client import ReqresApiClient - папка в котором хранится документ и сам документ
# client=ReqresApiClient() - создаем клиента
# resp=client.get_delayed_response(тут передеть значения) - у каждой функции свой метод
import requests
class ReqresApiClient():

    def __init__(self):
        self.base_path = 'https://reqres.in/api/'

    def request(self, method:str, path:str, data=None):
        url = self.base_path + path
        response = requests.request(method, url)
        return response

    def get_delayed_response(self, delayed_id: int):
        response = self.request('GET', 'users?delay={delayed_id}')
        return response

    def get_list_resourse(self):
        response = self.request('GET', 'unknown')
        return response

    def get_list_users(self, page_id: int):
        response = self.request('GET', 'users?page={page_id}')
        return response

    def get_single_resourse(self, resourse_id: int):
        response = self.request('GET', 'unknown/{resourse_id}')
        return response

    def get_single_resourse_not_found(self, resourse_id: int):
        response = self.request('GET', 'unknown/{resourse_id}')
        return response

    def get_single_users(self, user_id: int):
        response = self.request('GET', 'users/{user_id}')
        return response

    def get_single_users_not_found(self, user_id: int):
        response = self.request('GET', 'users/{user_id}')
        return response

    def delete_user(self, user_id: int):
        response = self.request('DELETE', 'users/{user_id}')
        return response

    def post_create(self, data: str):
        #pload = {"name": "morpheus", "job": "leader"}
        response = self.request('POST','users', data)
        return response

    def post_login_successful(self, data: str):
        #pload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        response = self.request('POST','login', data)
        return response

    def post_login_unsuccessful(self, data: str):
        #pload = {"email": "peter@klaven"}
        response = self.request('POST','login', data)
        return response

    def post_register_successful(self, data: str):
        #pload = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = self.request('POST','register', data)
        return response

    def post_register_unsuccessful(self, data: str):
        #pload = {"email": "sydney@fife"}
        response = self.request('POST','register', data)
        return response

    def put_create(self, user_id: int, data: str):
        #pload = {"name": "morpheus", "job": "zion resident"}
        response = self.request('PUT','users/{user_id}', data)
        return response

    def patch_update(self, user_id: int, data: str):
        #pload = {"name": "morpheus", "job": "zion resident"}
        response = self.request('PATCH','users/{user_id}', data)
        return response