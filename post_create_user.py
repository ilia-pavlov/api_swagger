import requests

payload = {'username': 'corey', 'password': 'testing'}
r = requests.post('http://httpbin.org/post', data=payload)

print(r.text)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
r_dict = r.json()
print(r_dict['form'])