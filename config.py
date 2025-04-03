
import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "your-bot-token")
    API_ID = int(os.getenv("API_ID", 123456))  # Replace with your Telegram API ID
    API_HASH = os.getenv("API_HASH", "your-api-hash")  # Replace with your Telegram API Hash
    MONGO_URI = os.getenv("MONGO_URI", "your-mongodb-uri")  # MongoDB connection string
    ADMINS = list(map(int, os.getenv("ADMINS", "123456789").split()))  # Admin User IDs
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001234567890"))  # Channel for logging
    FILE_STORE_CHANNEL = int(os.getenv("FILE_STORE_CHANNEL", "-1009876543210"))  # Channel where files are stored
    PUBLIC_FILE_STORE = bool(os.getenv("PUBLIC_FILE_STORE", False))  # Allow public file storing

config = Config()
