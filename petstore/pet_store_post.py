import requests

r = requests.get('https://petstore.swagger.io/v2/swagger.json')

print('Swagger main page')
print(r)

r = requests.get('https://s3-prod.adage.com/s3fs-public/iStock-1094806232.jpg')

with open('pappy.png', 'wb') as f:
    f.write(r.content)

# r = requests.post('https://petstore.swagger.io/v2/pet/999/uploadImage')
# print(r.json())  !!! before uploading pics need to create pet

body = {
    "id": 3472204455,
    "username": "Boby",
    "firstName": "Boby",
    "lastName": "Bobinson",
    "email": "boby@life.net",
    "password": "yes",
    "phone": "no_phones",
    "userStatus": 0
}
url = 'https://petstore.swagger.io/v2/user/createWithArray'
r = requests.post(url=url, data=body, timeout=3)
if r.ok is True:
    print('user was created')
else:
    print('nope!')
print(r.status_code)

r = requests.get('https://petstore.swagger.io/v2/user/Boby')
print(r)
