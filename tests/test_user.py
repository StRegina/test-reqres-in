import requests
def test_get_list_users():
    response = requests.get('https://reqres.in/api/users?page=2')
    if response.status_code == 200:
        return response.json()

def test_get_single_users():
    response = requests.get('https://reqres.in/api/users/2')
    if response.status_code == 200:
        return response.json()

def test_get_single_users_not_found():
    response = requests.get('https://reqres.in/api/users/23')
    if response.status_code == 404:
        return response.json()

def test_delete_user():
    response = requests.delete('https://reqres.in/api/users/2')
    if response.status_code == 200:
        return response.json()

def test_get_delayed_response():
    response = requests.get('https://reqres.in/api/users?delay=3')
    if response.status_code == 200:
        return response.json()

def test_post_create():
    pload = {"name": "morpheus", "job": "leader"}
    response = requests.post('https://reqres.in/api/users', data=pload)
    if response.status_code == 201:
        return response.json()

def test_patch_update():
    pload = {"name": "morpheus", "job": "zion resident"}
    response = requests.patch('https://reqres.in/api/users/2', data=pload)
    if response.status_code == 200:
        return response.json()

def test_put_update():
    pload = {"name": "morpheus", "job": "zion resident"}
    response = requests.put('https://reqres.in/api/users/2', data=pload)
    if response.status_code == 200:
        return response.json()