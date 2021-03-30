import requests

req = requests.get('https://images.squarespace-cdn.com/content/5b4e1bf64611a0bf2f92025f/1532287344279-PZPG9ZVYB8BGX1W5HATC/python-logo.jpg?content-type=image%2Fjpeg')

with open('python_logo.png', 'wb') as f:
    f.write(req.content)