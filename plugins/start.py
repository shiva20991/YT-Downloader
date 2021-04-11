from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Support Channel", url="https://t.me/Trvpn")],
        [InlineKeyboardButton(
            "Support Group", url="https://t.me/tamilrockersvpn")]
    ])
    welcomed = f"Hi! <b>{message.from_user.first_name}</b>\n/help duke lover  😋."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
