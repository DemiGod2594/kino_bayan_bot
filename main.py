import asyncio

from aiogram import types
from aiogram.filters import Command
from loader import bot, dp
from handlers.admin import admin_router
from handlers.digit import user_router
from utils.db.storage import init_db
from aiogram.types import BotCommand
from config_data.config import admin_ids


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    if message.from_user.id in admin_ids:
        await message.answer('''Привет!\nЯ кино-бот канала КиноБаян. Здесь собраны все фильмы, которые представлены у нас
        на канале. Отправьте цифру для получения ссылки на фильм ''')




async def main():

    init_db()

    dp.include_router(admin_router)
    dp.include_router(user_router)

    await bot.set_my_commands([
        BotCommand(command='start', description='Команда для начала работы'),
        BotCommand(command='add_id', description='Добавить новый ID. Для администраторов'),
        BotCommand(command='view', description='Посмотреть содержание базы данных. Для администраторов'),
        BotCommand(command='delete', description='Удалить запись по ID. Для администраторов'),
        BotCommand(command='view_users', description='Посмотреть кто пользовался ботом. Для администраторов')
    ])

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
