from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from config_data.config import ADMIN_IDS

from utils.function.add_to_db import add_id_to_db, add_message_to_id

admin_router = Router()


@admin_router.message(F.from_user.id == ADMIN_IDS, F.text.regexp(r'^\d+$'))
async def handle_admin_digit(message: types.Message, state: FSMContext):
    id = int(message.text)
    add_id_to_db(id)
    await state.update_data(id=id)
    await message.reply(f'ID {id} добапвлен в базу. Теперь отправьте ссылку на фильм.')


@admin_router.message(F.from_user.id == ADMIN_IDS, F.text)
async def handle_admin_link(message: types.Message, state: FSMContext):
    data = await state.get_data()
    id = data.get('id')
    if id:
        add_message_to_id(id, message.text)
        await message.reply(f'Ссылка добавлена к ID {id}.')
    else:
        await message.reply('Пожалуйста, сначала отправьте мне цифру (ID).')
