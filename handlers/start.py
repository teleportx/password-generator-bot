import asyncio
import secrets
from random import randint

from aiogram import Router
from aiogram import types
from aiogram.filters import Command, CommandObject

import config

router = Router()


@router.message(Command("start"))
async def start(message: types.Message, command: CommandObject):
    length = config.Generation.default_length

    if command.args is not None and command.args[0].isnumeric():
        length = int(command.args)
        length = min(config.Generation.max_password_length, length)

    password = ''.join(secrets.choice(config.Generation.letters) for _ in range(length))

    msg = await message.reply(f'This message will be deleted after 15 second!\nYour password:\n`{password}`')

    await asyncio.sleep(15)
    await msg.delete()


@router.message(Command("randport"))
async def random_port(message: types.Message, command: CommandObject):
    l = 1024
    r = 49151
    if command.args == 'd':
        r = 65535

    elif command.args == 'a':
        l = 0
        r = 65535

    await message.reply(f'Your random port: `{randint(l, r)}`')
