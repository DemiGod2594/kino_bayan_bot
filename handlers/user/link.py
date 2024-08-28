from utils.function.links import get_info_by_id
from aiogram import types, F
from filters.is_user import IsUser
from handlers.user.menu import links
from loader import dp


@dp.message(lambda message: message.text.isdigit())
async def handle_digit(message: types.Message):
    id = int(message.text)
    link = get_info_by_id(id)
    await message.reply(link)


@dp.message(IsUser(), F.text == links)
async def links(message: types.Message):
    await message.reply("Отправьте цифру, чтобы получить ссылку на видео")