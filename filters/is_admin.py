from aiogram.types import Message
from aiogram.filters import BaseFilter
from config_data.config import load_config, Config

config: Config = load_config()

class IsAdmin(BaseFilter):

    async def check(self, message: Message):

        user = message.from_user.id
        if user not in config.tg_bot.admin_ids:
            await message.answer('Только для администраторов')
        return user in config.tg_bot.admin_ids


