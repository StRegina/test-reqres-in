import requests
def post_login_successful():
    pload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post('https://reqres.in/api/login', data=pload)
    if response.status_code == 200:
        return response.json()

def post_login_unsuccessful():
    pload = {"email": "peter@klaven"}
    response = requests.post('https://reqres.in/api/login', data=pload)
    if response.status_code == 400:
        return response.json()