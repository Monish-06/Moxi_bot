from pyrogram import Client, filters
from database.filestore import save_file, get_file

def register_handlers(bot: Client):
    @bot.on_message(filters.document | filters.video | filters.audio)
    async def store_file(client, message):
        file_id = message.document.file_id if message.document else message.video.file_id if message.video else message.audio.file_id
        save_file(file_id, message)
        await message.reply(f"File saved! Access it with /get {file_id}")

    @bot.on_message(filters.command("get"))
    async def retrieve_file(client, message):
        args = message.text.split(" ", 1)
        if len(args) < 2:
            return await message.reply("Usage: /get file_id")
        
        file_id = args[1]
        file = get_file(file_id)
        if file:
            await message.reply_document(file["file_id"], caption="Here is your file.")
        else:
            await message.reply("File not found.")
