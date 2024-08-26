from aiogram.types import Message
from aiogram.filters import BaseFilter
from config_data.config import load_config, Config
from config_data import config

class IsAdmin(BaseFilter):

    async def check(self, message: Message):

        user = message.from_user.id
        if user not in config.ADMIN_IDS:
            await message.answer('Только для администраторов')
        return user in config.ADMIN_IDS


