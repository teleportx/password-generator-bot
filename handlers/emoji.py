from aiogram import Router, types, F

router = Router()


@router.message(F.entities[0].type == 'custom_emoji')
async def handle_custom_emoji(message: types.Message):
    await message.reply(f'Custom Emoji ID: `{message.entities[0].custom_emoji_id}`')
