from pyrogram import Client, filters
from database.filters import add_filter, get_filter

def register_handlers(bot: Client):
    @bot.on_message(filters.command("addfilter") & filters.private)
    async def add_new_filter(client, message):
        args = message.text.split(" ", 1)
        if len(args) < 2:
            return await message.reply("Usage: /addfilter keyword - reply_text")
        
        keyword, reply_text = args[1].split(" - ", 1)
        add_filter(keyword, reply_text)
        await message.reply(f"Filter '{keyword}' added successfully!")

    @bot.on_message(filters.text & filters.private)
    async def check_filter(client, message):
        reply = get_filter(message.text)
        if reply:
            await message.reply(reply)
