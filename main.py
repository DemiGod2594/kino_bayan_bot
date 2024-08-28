import asyncio

from aiogram import types
from aiogram.filters import Command
from loader import bot, dp, db
from handlers.admin import admin_router
from handlers.digit import user_router


db.create_tables()

dp.include_router(admin_router)
dp.include_router(user_router)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer('''Привет!\nЯ кино-бот канала КиноБаян. Здесь собраны все фильмы, которые представлены у нас 
на канале. Отправьте цифру для получения ссылки на фильм ''')


async def main() -> None:

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
