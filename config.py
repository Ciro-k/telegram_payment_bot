import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    PROVIDER_TOKEN = os.getenv('PROVIDER_TOKEN')
    ADMIN_ID = int(os.getenv('ADMIN_ID', 0))
    COMMISSION_PERCENT = float(os.getenv('COMMISSION_PERCENT', 1.0))
    
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN не найден!")
    if not PROVIDER_TOKEN:
        raise ValueError("PROVIDER_TOKEN не найден!")
    if ADMIN_ID == 0:
        raise ValueError("ADMIN_ID не задан!")
