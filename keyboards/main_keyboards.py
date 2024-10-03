from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def admin_keyboard():

    add_link = InlineKeyboardButton(text='Добавить ссылку', callback_data='add')
    delete = InlineKeyboardButton(text='Удалить ссылку', callback_data='delete')
    view = InlineKeyboardButton(text='Посмотреть базу', callback_data='view')

    keyboard = InlineKeyboardBuilder()
    keyboard.row(add_link, delete, view)

    return keyboard.as_markup(resize_keyboard=True)

