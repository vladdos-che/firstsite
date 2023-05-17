from os import system


def start_project(project_name):
    system(f"python {project_name}/manage.py runserver")


if __name__ == "__main__":
    project_name_start = input("Введите папку в которой у вас хронится проект, который нужно запустить: ")
    start_project(project_name_start)
