from oscarbot.response import TGResponse


def handler(user, text):
    message = 'Я не знаю такой команды'
    user.want_action = 'oscar_bot.do_something'
    user.save()

    return TGResponse(
        message=message,
    )
