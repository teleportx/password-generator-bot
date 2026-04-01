from aiogram import Router

from . import start
from . import emoji
from . import shift

router = Router()

router.include_router(start.router)
router.include_router(emoji.router)
router.include_router(shift.router)
