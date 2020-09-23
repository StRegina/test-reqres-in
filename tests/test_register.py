import requests
from utils.api_client import ReqresApiClient

class TestRegister():

    def test_post_register_successful(self, api_client):
        response = api_client.register(data = {"email": "eve.holt@reqres.in", "password": "pistol"})
        assert response.status_code == 200

    def test_post_register_unsuccessful(self, api_client):
        response = api_client.register(data = {"email": "sydney@fife"})
        assert response.status_code == 400