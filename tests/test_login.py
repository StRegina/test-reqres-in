import requests
from utils.api_client import ReqresApiClient

class TestLogin():

    def test_post_login_successful(self, api_client):
        response = api_client.login(login_data = {"email": "eve.holt@reqres.in", "password": "cityslicka"})
        assert response.status_code == 200

#    def test_post_login_unsuccessful(self, api_client):
#        response = api_client.login(login_data = {"email": "peter@klaven"})
#        assert response.status_code == 400