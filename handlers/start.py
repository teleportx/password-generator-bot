import asyncio
import secrets
from xml.etree import ElementTree

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

    msg = await message.reply(f'This message will be deleted after 15 second!\nYour password:\n`{password}`',
                              parse_mode='markdown')

    await asyncio.sleep(15)
    await msg.delete()
