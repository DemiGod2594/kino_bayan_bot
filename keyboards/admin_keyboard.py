from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def keyboard_adm():

    admin = InlineKeyboardButton(text='Админ', callback_data='admin')
    user = InlineKeyboardButton(text='Пользователь', callback_data='user')
    keyboard_admin = InlineKeyboardBuilder()
    keyboard_admin.row(admin, user)

    return keyboard_admin.as_markup(resize_keyboard=True)
