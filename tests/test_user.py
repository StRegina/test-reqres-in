import requests
from utils.api_client import ReqresApiClient

class TestUser():

    def test_get_list_users(self, api_client):
        response = api_client.get_user_page(page_id = 2)
        assert response.status_code == 200

    def test_get_single_users(self, api_client):
        response = api_client.get_user(user_id = 2)
        assert response.status_code == 200

    def test_get_single_users_not_found(self, api_client):
        response = api_client.get_user(user_id = 23)
        assert response.status_code == 404

    def test_delete_user(self, api_client):
        response = api_client.get_user(user_id = 2)
        assert response.status_code == 200

    def test_get_delayed_response(self, api_client):
        response = api_client.get_delayed_answer(seconds = 3)
        assert response.status_code == 200

    def test_post_create(self, api_client):
        response = api_client.post_user(user_data = {"name": "morpheus", "job": "leader"})
        assert response.status_code == 201

    def test_patch_update(self, api_client):
        response = api_client.patch_update(user_id = 2, user_data = {"name": "morpheus", "job": "zion resident"})
        assert response.status_code == 200

    def test_put_update(self, api_client):
        response = api_client.put_user(user_id = 2, user_data = {"name": "morpheus", "job": "zion resident"})
        assert response.status_code == 200