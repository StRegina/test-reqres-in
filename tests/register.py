import requests
def post_register_successful():
    pload = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = requests.post('https://reqres.in/api/register', data=pload)
    if response.status_code == 200:
        return response.json()

def post_register_unsuccessful():
    pload = {"email": "sydney@fife"}
    response = requests.post('https://reqres.in/api/register', data=pload)
    if response.status_code == 400:
        return response.json()