from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode
from utils.db.storage import DatabaseManager

from config_data.config import Config, load_config

config: Config = load_config()

bot = Bot(token=config.tg_bot.token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
db = DatabaseManager('config_data/database.db')
