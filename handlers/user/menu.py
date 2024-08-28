from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from filters.is_admin import IsAdmin
from filters.is_user import IsUser
from loader import dp

settings = 'Настройки'
questions = 'Вопросы'

user_builder = ReplyKeyboardBuilder()
admin_builder = ReplyKeyboardBuilder()

links = KeyboardButton(text='Ссылки')
settings = KeyboardButton(text='Настройки')
questions = KeyboardButton(text='Вопросы')

user_builder.row(links)
admin_builder.row(settings, questions, width=1)

keyboaard: ReplyKeyboardMarkup = user_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)

kb: ReplyKeyboardMarkup = admin_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True,
)


@dp.message(IsAdmin(), commands='menu')
async def admin_menu(message: Message):
    await message.answer('Меню', reply_markup=kb)


@dp.message(IsUser(), commands='menu')
async def user_menu(message: Message):
    await message.answer('Меню', reply_markup=keyboaard)
