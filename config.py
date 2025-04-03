import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "your-telegram-bot-token")
    API_ID = int(os.getenv("API_ID", "your-api-id"))
    API_HASH = os.getenv("API_HASH", "your-api-hash")
    MONGO_URI = os.getenv("MONGO_URI", "your-mongo-db-uri")
    OWNER_ID = int(os.getenv("OWNER_ID", "your-telegram-user-id"))
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-100xxxxxxxxx"))  # Telegram Channel ID
    FILE_STORE_CHANNEL = int(os.getenv("FILE_STORE_CHANNEL", "-100xxxxxxxxx"))  # Channel where files will be stored
    PUBLIC_FILE_STORE = os.getenv("PUBLIC_FILE_STORE", "True").lower() == "true"
