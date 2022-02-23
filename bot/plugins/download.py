from ..utubebot import UtubeBot
from pyrogram.types import Message
from pyrogram import filters, Client
from pySmartDL import SmartDL


@UtubeBot.on_message(filters.command("download"))
async def Upload(client: Client, message: Message):
     chat_id = message.chat.id
     if len(message.command) == 1:
        await message.reply_text("No link!")
        return
     link = message.command[1]     
     download = SmartDL(link, progress_bar=True)
     download.start()
     video = download.get_dest()
     await client.send_video(chat_id=chat_id, video=video)
