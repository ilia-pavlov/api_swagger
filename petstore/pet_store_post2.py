import requests

data = {
    "id": 3472204455,
    "username": "Boby",
    "firstName": "Boby",
    "lastName": "Bobinson",
    "email": "boby@life.net",
    "password": "yes",
    "phone": "no_phones",
    "userStatus": 0
  }
r = requests.post('https://petstore.swagger.io/v2/user/createWithArray', data=data)

print(r)