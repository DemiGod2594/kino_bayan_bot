from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from config_data.config import token


default=DefaultBotProperties(parse_mode='HTML')
bot = Bot(token=token)
dp = Dispatcher(storage=MemoryStorage())

