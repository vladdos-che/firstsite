from os import system


def freeze_venv(venv_name):
    activate = r"\Scripts\activate"
    system(f"{venv_name}{activate}")
    system("pip freeze > requirements.txt")


if __name__ == "__main__":
    any_venv_name = input('Введите название виртуального окружения, которое нужно "зафризить": ')
    freeze_venv(any_venv_name)
