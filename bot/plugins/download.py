from ..utubebot import UtubeBot
from pyrogram.types import Message
from pyrogram import filters
from pyromod import listen
from pySmartDL import SmartDL


@UtubeBot.on_message(filters.command("download"))
async def Upload(client: UtubeBot, message: Message):
     chat_id = message.chat.id

     link = await client.ask(chat_id, 'Send me video link', parse_mode='Markdown')    
     if await is_cancel(message, link.text):
        return
     link = link.text
     download = SmartDL(link, progress_bar=False)
     download.start()
     video = download.get_dest()
     await client.send_video(chat_id=chat_id, video=video)
