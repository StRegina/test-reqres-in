import requests
def test_delete_user():
    response = requests.delete('https://reqres.in/api/users/2')
    if response.status_code == 204:
        return response.json()