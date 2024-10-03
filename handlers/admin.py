from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.markdown import text

from config_data.config import admin_ids
from aiogram.filters import Command
from utils.function.add_to_db import add_id_to_db, add_message_to_id
from utils.function.all_links import get_all_messages
from utils.function.delete_links import delete_all
from keyboards.main_keyboards import admin_keyboard

import io
from aiogram.types import FSInputFile, CallbackQuery

admin_router = Router()


class AddFilmFSM(StatesGroup):
    waiting_for_id = State()
    waiting_for_link = State()
    waiting_for_delete = State()

@admin_router.message(Command(commands=["admin"]))
async def show_admin_panel(message: types.Message):
    if message.from_user.id in admin_ids:
        await message.reply("Админ-панель:", reply_markup=admin_keyboard())
    else:
        await message.reply("У вас нет прав для использования этой команды.")


@admin_router.callback_query(lambda call: call.data == "add")
async def handle_add_id(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Отправьте мне цифру (ID)")
    await state.set_state(AddFilmFSM.waiting_for_id)


@admin_router.message(F.text.regexp(r'^\d+$'), AddFilmFSM.waiting_for_id)
async def handle_admin_digit(message: types.Message, state: FSMContext):
    id = int(message.text)
    add_id_to_db(id)
    await message.reply(f'ID {id} добапвлен в базу. Теперь отправьте ссылку на фильм.')
    await state.update_data(id=id)
    await state.set_state(AddFilmFSM.waiting_for_link)


@admin_router.message(AddFilmFSM.waiting_for_link)
async def handle_admin_link(message: types.Message, state: FSMContext):
    data = await state.get_data()
    id = data.get('id')
    if id:
        add_message_to_id(id, message.text)
        await message.reply(f'Ссылка добавлена к ID {id}.')
    else:
        await message.reply('Пожалуйста добавьте ID с помощью /add_id.')
        await state.clear()


@admin_router.callback_query(lambda call: call.data =='view')
async def handle_view(callback: CallbackQuery):
    all_links = get_all_messages()
    if not all_links:
        await callback.message.reply('База данных пуста.')
        return

    response = "Содержание базы данных:\n\n"
    for record in all_links:
        id, link = record
        response += f"ID: {id}\nСсылка:\n{link}\n\n"
    if len(response) > 4096:
        file_data = io.StringIO(response)
        file_data.seek(0)
        await callback.reply_document(
            FSInputFile(file_data, filename='links.txt'),
            caption="Содержимое базы данных"
        )
    else:
        await callback.message.reply(response)


@admin_router.callback_query(lambda call: call.data == "delete")
async def handle_delete_message(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Отправьте ID, которое нужно удалить")
    await state.set_state(AddFilmFSM.waiting_for_delete)


@admin_router.message(F.text.regexp(r'^\d+$'), AddFilmFSM.waiting_for_delete)
async def handle_delete_id(message: types.Message, state: FSMContext):
    id = int(message.text)
    delete_all(id)
    await message.reply(f'Все ссылки с ID {id} удалены.')
    await state.clear()

