from main.models import Task

"""
Создал для примера!
Не юзабельно!
"""


def create_quick_task(title, description, author):
    task = Task(title=title, description=description, author=author)
    task.save()
    return task


def list_all_tasks():
    tasks = Task.objects.all()
    task_list = []
    for task in tasks:
        task_list.append(f"Title: {task.title}, Description: {task.description}")
    return task_list
