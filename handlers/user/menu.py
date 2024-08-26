from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from filters.is_admin import IsAdmin
from filters.is_user import IsUser
from loader import dp


links = 'Ссылки'

settings = 'Настройки'
questions = 'Вопросы'


@dp.message(IsAdmin(), commands='menu')
async def admin_menu(message: Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(settings, questions)

    await message.answer('Меню', reply_markup=markup)


@dp.message(IsUser(), commands='menu')
async def user_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(links)

    await message.answer('Меню', reply_markup=markup)