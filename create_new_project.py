from os import system
from shutil import move
from start_project import start_project

project_name = input("Введите имя проекта: ")
system(f"django-admin startproject {project_name}")

num_of_apps = input("Сколько хотить приложений создать? (целое число) >>>  ")
while type(num_of_apps) != int:
    try:
        num_of_apps = int(num_of_apps)
    except ValueError:
        num_of_apps = input("Вы ввели не число! Введите число! "
                            "Сколько хотить приложений создать? >>>  ")

for i in range(1, num_of_apps + 1):
    app_name = input(f"Введите имя приложения номер {i}: ")
    system(f"python {project_name}/manage.py startapp {app_name}")
    move(app_name, f"./{project_name}")

start_project(project_name)
