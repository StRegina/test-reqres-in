import requests
def get_single_resourse():
    response = requests.get('https://reqres.in/api/unknown/2')
    if response.status_code == 200:
        return response.json()

def get_single_resourse_not_found():
    response = requests.get('https://reqres.in/api/unknown/23')
    if response.status_code == 404:
        return response.json()

def get_list_resourse():
    response = requests.get('https://reqres.in/api/unknown')
    if response.status_code == 200:
        return response.json()