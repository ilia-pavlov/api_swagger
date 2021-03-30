import requests

r = requests.get('https://petstore.swagger.io')

print(r)
print(dir(r))
print(help(r))

print(r.text)
