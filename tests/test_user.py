import requests
from utils.api_client import ReqresApiClient

class TestUser():

    def test_get_list_users(self, api_client):
        response = api_client.users_page(page_id = 2, data = None)
        assert response.status_code == 200

    def test_get_single_users(self, api_client):
        response = api_client.users(user_id = 2, data = None)
        assert response.status_code == 200

    def test_get_single_users_not_found(self, api_client):
        response = api_client.users(user_id = 23, data = None)
        assert response.status_code == 404

    def test_delete_user(self, api_client):
        response = api_client.users(user_id = 2, data = None)
        assert response.status_code == 200

    def test_get_delayed_response(self, api_client):
        response = api_client.delayed(delayed_id = 3, data = None)
        assert response.status_code == 200

    def test_post_create(self, api_client):
        response = api_client.users(data = {"name": "morpheus", "job": "leader"})
        assert response.status_code == 201

    def test_patch_update(self, api_client):
        response = api_client.users(user_id = 2, data = {"name": "morpheus", "job": "zion resident"})
        assert response.status_code == 200

    def test_put_update(self, api_client):
        response = api_client.users(user_id = 2, data = {"name": "morpheus", "job": "zion resident"})
        assert response.status_code == 200