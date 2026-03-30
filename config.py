import string
from os import environ

from dotenv import load_dotenv

load_dotenv()


class Telegram:
    token = environ['TOKEN']
    bot_api_server = environ.get('TELEGRAM_BOT_API_SERVER')


class Generation:
    letters = string.ascii_letters + string.digits

    max_password_length = 512
    default_length = 64
