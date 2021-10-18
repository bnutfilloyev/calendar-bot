from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp(), state="*")
async def bot_help(message: types.Message):
    text = ("Buyruqlar ro'yxati: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/calendar - Kalendarni ko'rish",
            "",
            "Bot yaratuvchisi @yoshlik_media")
    
    await message.answer("\n".join(text))
