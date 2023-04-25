import requests  # https://docs-python.ru/packages/modul-requests-python/poluchenie-otpravka-dannyh-vide-json/

f = requests.get('https://jsonplaceholder.typicode.com/todos/')
f.json()
