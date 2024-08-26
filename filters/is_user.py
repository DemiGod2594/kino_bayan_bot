from aiogram.types import Message
from aiogram.filters import BaseFilter

from config_data.config import load_config, Config


class IsUser(BaseFilter):

    async def check(self, message: Message):
        config: Config = load_config()
        return message.from_user.id not in config.tg_bot.admin_ids
