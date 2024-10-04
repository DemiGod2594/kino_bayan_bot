from aiogram import types, Router, F
from utils.function.links import get_info_by_id
from aiogram.types import CallbackQuery


user_router = Router()

@user_router.callback_query(lambda call: call.data == "user")
async def user_start(callback: CallbackQuery):
    await callback.message.answer("Отправьте цифру для получения ссылки на фильм")
    await callback.message.edit_reply_markup(reply_markup=None)

@user_router.message(F.text.regexp(r'^\d+$'))
async def handle_digit(message: types.Message):
    id = int(message.text)
    link = get_info_by_id(id)
    await message.reply(link)

