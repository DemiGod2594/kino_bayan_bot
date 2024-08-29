from aiogram import types, Router, F
from utils.function.links import get_info_by_id
from config_data.config import admin_ids
user_router = Router()


@user_router.message(F.text.regexp(r'^\d+$') & ~F.from_user.id.in_(admin_ids))
async def handle_digit(message: types.Message):
    id = int(message.text)
    link = get_info_by_id(id)
    await message.reply(link)
