from oscar_bot.views import start, create_task, list_task
from oscarbot.router import route

routes = [
    route('/start', start),
    route('/create_task/', create_task),
    route('/list_task/', list_task),
]