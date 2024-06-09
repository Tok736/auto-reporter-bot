from aiogram import Router
from aiogram.types import Message


router = Router()

@router.message()
async def echo(message: Message):
    """ Echo handler """

    await message.answer(
        message.text
    )

