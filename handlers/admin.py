from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from config_data.config import admin_ids
from aiogram.filters import Command, StateFilter

from utils.function.add_to_db import add_id_to_db, add_message_to_id
from utils.function.all_links import get_all_messages
from utils.function.delete_links import delete_all

admin_router = Router()


@admin_router.message(Command(commands=['add_id']))
async def handle_add_id_command(message: types.Message, state: FSMContext):
    if message.from_user.id in admin_ids:
        await message.reply('Отправьте мне цифру (ID).')
        await state.set_state('waiting_for_id')
    else:
        await message.reply('Вы не админ.')


@admin_router.message(F.text.regexp(r'^\d+$'), StateFilter('waiting_for_id'))
async def handle_admin_digit(message: types.Message, state: FSMContext):
    id = int(message.text)
    add_id_to_db(id)
    await state.update_data(id=id)
    await message.reply(f'ID {id} добапвлен в базу. Теперь отправьте ссылку на фильм.')
    await state.set_state('waiting_for_link')



@admin_router.message(StateFilter('waiting_for_link'))
async def handle_admin_link(message: types.Message, state: FSMContext):
    data = await state.get_data()
    id = data.get('id')
    if id:
        add_message_to_id(id, message.text)
        await message.reply(f'Ссылка добавлена к ID {id}.')
        await state.clear()
    else:
        await message.reply('Пожалуйста добавьте ID с помощью /add_id.')
        await state.clear()


@admin_router.message(Command(commands=['view']))
async def handle_view(message: types.Message):
    if message.from_user.id in admin_ids:
        all_links = get_all_messages()
        if not all_links:
            await message.reply('База данных пуста.')
            return

        response = "Содержание базы данных:\n\n"
        for record in all_links:
            id, link = record
            response += f"ID: {id}\nСсылка:\n{link}\n\n"
    else:
        await message.reply('Вы не админ.')


@admin_router.message(Command(commands=['delete']))
async def handle_delete_command(message: types.Message, state: FSMContext):
    if message.from_user.id in admin_ids:
        await message.reply('Отправьте ID для удаления.')
        await state.set_state('waiting_for_delete_id')
    else:
        await message.reply('Вы не админ.')


@admin_router.message(F.text.regexp(r'^\d+$'), StateFilter('waiting_for_delete_id'))
async def handle_delete_id(message: types.Message, state: FSMContext):
    id = int(message.text)
    delete_all(id)
    await message.reply(f'Все ссылки с ID {id} удалены.')
    await state.clear()
