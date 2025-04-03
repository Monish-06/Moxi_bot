from flask import Flask

app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot is running!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
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
