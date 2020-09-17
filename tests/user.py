import requests
def get_list_users():
    response = requests.get('https://reqres.in/api/users?page=2')
    if response.status_code == 200:
        return response.json()

def get_single_users():
    response = requests.get('https://reqres.in/api/users/2')
    if response.status_code == 200:
        return response.json()

def get_single_users_not_found():
    response = requests.get('https://reqres.in/api/users/23')
    if response.status_code == 404:
        return response.json()

def delete_user():
    response = requests.delete('https://reqres.in/api/users/2')
    if response.status_code == 200:
        return response.json()

