from os import system
from make_freeze import freeze_venv

venv = input("Введите название нового виртуального окружения: ")
activate = r"\Scripts\activate"

system(f"python -m venv {venv}")
system(f"{venv}{activate}")
freeze_venv(venv)
system("python.exe -m pip install --upgrade pip")
system("pip install django")
