from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.inline import games_inline_keyboard

common_router = Router()



@common_router.message(Command('start'))
async def process_start_command(message: Message):
    await message.answer(text='Выберите одну из игр', reply_markup=games_inline_keyboard)

