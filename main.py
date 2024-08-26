import asyncio

from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram import Bot, Dispatcher, types, F
from config_data.config import Config, load_config
# from handlers import user_handlers
# from utils.db.storage import
from aiogram.filters import CommandStart


config: Config = load_config()

dp = Dispatcher()

kb_builder = ReplyKeyboardBuilder()

user_message = KeyboardButton(text='Пользователь')
admin_message = KeyboardButton(text='Админ')

kb_builder.row(user_message, admin_message, width=1)

keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True,
)


@dp.message(CommandStart())
async def cmd_start(message: types.Message):

    await message.answer('''Привет!\nЯ кино-бот канала КиноБаян. Здесь собраны все фильмы, которые представлены у нас 
на канале. Для справки отправьте команду /help! ''',
                         reply_markup=keyboard)


@dp.message(F.text == 'Пользователь')
async def user_mode(message: types.Message):

    cid = message.chat.id
    if cid in config.tg_bot.admin_ids:
        config.tg_bot.admin_ids.remove(cid)

    await message.answer('Включен пользовательский режим.', reply_markup=ReplyKeyboardRemove())
    await message.delete()

@dp.message(F.text == 'Админ')
async def admin_mode(message: types.Message):

    cid = message.chat.id
    if cid not in config.tg_bot.admin_ids:
        await message.answer("Вы не админ", reply_markup=ReplyKeyboardRemove())
        await message.delete()
    else:
        await message.answer('Включен админский режим.', reply_markup=ReplyKeyboardRemove())
        await message.delete()


async def main() -> None:
    bot = Bot(token=config.tg_bot.token)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
