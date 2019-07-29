import requests
from utils.users import get_user, get_users
from utils.get_tok import get_token

TOKEN = get_token()


def telegram_bot_sendtext(message, bot_chatid):
    send_text = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&parse_mode=Markdown&text={}'.format(TOKEN, bot_chatid, message)
    response = requests.get(send_text)
    return response.json()


def send_it():
    message = "Hello darkness my old friend..."
    users = get_users()
    for user in users:
        user_id = get_user(user)
        bot_chatid = str(user_id)
        telegram_bot_sendtext(message, bot_chatid)


# schedule.every(3).to(6).minutes.do(send_it)

