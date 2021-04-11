from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"help pannuko oru 10 crores anupu ennaku 🤣"
    await message.reply_text(helptxt)
