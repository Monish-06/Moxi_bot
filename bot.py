from pyrogram import Client
from config import Config
from handlers import filters_handler, filestore_handler

bot = Client(
    "MoxiBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# Import handlers
filters_handler.register_handlers(bot)
filestore_handler.register_handlers(bot)

if __name__ == "__main__":
    print("Bot is running...")
    bot.run()
