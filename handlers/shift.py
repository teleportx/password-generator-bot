from aiogram import Router, F, types

router = Router()


@router.message(F.text.isnumeric())
async def handle_shift(message: types.Message):
    uid = int(message.text)
    short_id = str(uid).replace("-100", "")
    shift = int(-1 * pow(10, len(short_id) + 2))
    shifted = shift - uid

    await message.reply(f'Your shifted id: `{shifted}`')
