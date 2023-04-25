import requests  # https://docs-python.ru/packages/modul-requests-python/poluchenie-otpravka-dannyh-vide-json/


class MyJsonFile:
    f = f"JSON: {requests.get('https://jsonplaceholder.typicode.com/todos/').json()}"

    # Для вывода в консоль Джанго используйте:
    # 1) python .\manage.py shell
    # 2) from json_my_hw import MyJsonFile
    # 3) print(MyJsonFile.f)
