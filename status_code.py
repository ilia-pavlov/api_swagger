import requests

r = requests.get('https://petstore.swagger.io')

print(r.status_code)
print(r.ok)
print(r.headers)