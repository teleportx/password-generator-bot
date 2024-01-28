import string
from os import environ

from dotenv import load_dotenv

load_dotenv()


class Telegram:
    token = environ.get('TOKEN')


class Generation:
    letters = string.ascii_letters + string.digits + r"!#$%&()*+-.:<=>?@[]^_{|}~"

    max_password_length = 512
    default_length = 64


Generation.letters = Generation.letters.replace('`', '').replace('\\', '')
