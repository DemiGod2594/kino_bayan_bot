from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ContentType, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove
from aiogram.filters.callback_data import CallbackData
from aiogram.types.chat import SendChatAction
from handlers.user.menu import settings
from filters.is_admin import IsAdmin
from loader import dp, db, bot
from utils.function.add_to_db import add_id_to_db, add_message_to_id



@dp.message(lambda message: message.text.isdigit())
async def handle_digit(message: types.Message):
    id = int(message.text)
    add_id_to_db(id)
    await message.answer(f'ID {id} добавлен в базу данных. Теперь отправьте мне ссылку на видео для добавления в базу')


@dp.message(lambda message: not message.text.isdigit())
async def handle_message(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    last_id = await state.get_data()
    if last_id:
        id = last_id.get('id')
        add_message_to_id(id, message.text)
        await message.answer(f'Сообщение добавлено к ID {id}.')
    else:
        await message.answer('Пожалуйста, сначала отправьте мне цифру (ID).')


@dp.message(IsAdmin(), F.text == settings)
async def settings(message: types.Message):
    await message.reply('Отправьте цифруб чтобы добавить ID в базу данных, затем отправьте ссылку на видео для '
                        'добавления в базу')