from aiogram import types
import calendar
from loader import dp
from states.UserState import Form


@dp.message_handler(commands='calendar')
async def send_calendar(msg: types.Message):
    await msg.answer("Kalendarni ko'rish uchun avval oy raqamini keyin esa yil raqamini yuboring.\n\ne.g: Iyul 2021 -> 07.2021")
    await Form.Calendar.set()

@dp.message_handler(state=Form.Calendar)
async def get_calendar(msg: types.Message):
    data = msg.text
    month, year = data.split('.')
    await msg.answer(f"<code>{calendar.month(int(year), int(month))}</code>")