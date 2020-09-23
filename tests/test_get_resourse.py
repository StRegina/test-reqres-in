import requests
from utils.api_client import ReqresApiClient

class TestGetResourse():

    def test_get_single_resourse(self, api_client):
        response = api_client.get_resourse(2)
        assert response.status_code == 200

    def test_get_single_resourse_not_found(self, api_client):
        response = api_client.get_resourse(23)
        assert response.status_code == 404

    def test_get_list_resourse(self, api_client):
        response = api_client.get_resourse(None)
        assert response.status_code == 404