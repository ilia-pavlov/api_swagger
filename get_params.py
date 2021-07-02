import requests

payload = {'page': 2, 'count': 25}
r = requests.get('http://httpbin.org/get', params=payload)

# print(r.text)
print(r.url)

print(r.json()['args'])

# for data in r.json()['args']:
    # print()
