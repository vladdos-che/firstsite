import requests

f = requests.get('https://jsonplaceholder.typicode.com/todos/')
f.json()
