import requests

r = requests.get('https://petstore.swagger.io/v2/swagger.json')

print('Swagger main page')
print(r)

r = requests.get('https://s3-prod.adage.com/s3fs-public/iStock-1094806232.jpg')  # capture puppy picture
with open('pappy.png', 'wb') as f:
    f.write(r.content)

body = {
    "id": 3472204455,
    "username": "Tororoto",
    "firstName": "BobyLove",
    "lastName": "Bobinson",
    "email": "boby@life.net",
    "password": "yes",
    "phone": "no_phones",
    "userStatus": 0
}

url = 'https://petstore.swagger.io/v2/user'
r = requests.post(url, json=body, timeout=3)
if r.ok is True:
    print('User was created')
else:
    print('nope!')
print(r.status_code)

r = requests.get('https://petstore.swagger.io/v2/user/Tororoto')
print(r.json())

payload = {'username': 'Tororoto', 'password': 'yes'}
r = requests.get('https://petstore.swagger.io/v2/user/login', params=payload)

print(r.url)
print(r.status_code)
print(r.json())