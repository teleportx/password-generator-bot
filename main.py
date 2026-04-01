import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer

import config
import handlers

logging.basicConfig(level=logging.INFO)

werkzeug = logging.getLogger('werkzeug')
werkzeug.setLevel(logging.WARN)

aiogram_event = logging.getLogger('aiogram.event')
aiogram_event.setLevel(logging.WARN)


def get_bot_api_session():
    if config.Telegram.bot_api_server is None:
        return None

    return AiohttpSession(
        api=TelegramAPIServer(
            base=f'{config.Telegram.bot_api_server}/bot{{token}}/{{method}}',
            file=f'{config.Telegram.bot_api_server}/file{{path}}',
        )
    )


async def main():
    bot = Bot(token=config.Telegram.token, default=DefaultBotProperties(parse_mode='markdown'), session=get_bot_api_session())
    config.Telegram.bot = bot

    dp = Dispatcher()

    dp.include_router(handlers.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
