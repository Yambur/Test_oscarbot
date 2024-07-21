from oscarbot.menu import Menu, Button
from oscarbot.response import TGResponse


def start(user):
    menu = Menu([
        Button("Начнем", callback="/start"),
    ])
    return TGResponse(
        message="Привет! Хочешь создать задачу? Тогда вперед!",
        menu=menu
    )


def create_task(user):
    menu = Menu([
        Button("Создаем задачу", callback="/create_task/"),
    ])
    return TGResponse(
        message="Задача создана! Поздравляю!",
        menu=menu
    )


def list_task(user):
    menu = Menu([
        Button("Список задач", callback="/list_task/"),
    ])
    return TGResponse(
        message="Вот список твоих задач!"
    )