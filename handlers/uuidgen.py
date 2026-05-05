import uuid

from aiogram import Router
from aiogram import types
from aiogram.filters import Command

router = Router()


@router.message(Command("uuid"))
async def handle_uuid(message: types.Message):
    await message.reply(f'`{uuid.uuid4()}`')

