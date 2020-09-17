import requests
def patch_update():
    pload = {"name": "morpheus", "job": "zion resident"}
    response = requests.patch('https://reqres.in/api/users/2', data=pload)
    if response.status_code == 200:
        return response.json()

def put_update():
    pload = {"name": "morpheus", "job": "zion resident"}
    response = requests.put('https://reqres.in/api/users/2', data=pload)
    if response.status_code == 200:
        return response.json()