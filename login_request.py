import requests

r = requests.get('http://httpbin.org/basic-auth/corey/testing',
                 auth=('corey', 'testing'),
                 timeout=3)  # timeout for in case of latency

print(r)
print(r.text)




