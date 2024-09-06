from dotenv import load_dotenv
import os

load_dotenv()

token = os.environ.get('BOT_TOKEN')
admin_ids = list(map(int, os.environ.get('ADMIN_IDS', '').split(',')))
