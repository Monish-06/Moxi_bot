import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # Telegram Bot Token
    API_ID = int(os.getenv("API_ID"))  # Telegram API ID
    API_HASH = os.getenv("API_HASH")  # Telegram API Hash
    MONGO_URL = os.getenv("MONGO_URL")  # MongoDB URL
    OWNER_ID = int(os.getenv("OWNER_ID"))  # Bot Owner ID
    FILE_STORE_CHANNEL = int(os.getenv("FILE_STORE_CHANNEL"))  # File store channel ID
    PUBLIC_FILE_STORE = os.getenv("PUBLIC_FILE_STORE", "True") == "True"  # Public access toggle
