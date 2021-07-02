import requests

""" data = {
    "id": 0,
    "username": "Terry",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
  } """

data = {"username": "Rocky", "email": "creat+user@ipa.cpm"}

r = requests.post('https://petstore.swagger.io/v2/user', json=data)

print(r.text)

r = requests.get('https://petstore.swagger.io/v2/user/Rocky')

print(r.json())