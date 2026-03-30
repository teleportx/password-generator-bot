from aiogram import Router

from . import start
from . import emoji

router = Router()

router.include_router(start.router)
router.include_router(emoji.router)
