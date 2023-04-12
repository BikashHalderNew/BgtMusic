# Power𝐞𝐝 By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 

from pyrogram import filters
from pyrogram.types import Message

from modules.config import BANNED_USERS
from modules import app
from modules.core.call import Aditya
from modules.utils.helpers.filters import command
from modules.utils.database import is_music_playing, music_on
from modules.utils.decorators import AdminRightsCheck


@app.on_message(
    filters.command(["resume", "cresume"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text("**❌ 𝐄𝐫𝐫𝐨𝐫, 𝐖𝐫𝐨𝐧𝐠 𝐔𝐬𝐚𝐠𝐞 𝐎𝐟 𝐂𝐨𝐦𝐦𝐚𝐧𝐝❗...**")
    if await is_music_playing(chat_id):
        return await message.reply_text("**🔊 𝐁𝐠𝐭 𝐌𝐮𝐬𝐢𝐜 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 ✨ ...**")
    await music_on(chat_id)
    await Aditya.resume_stream(chat_id)
    await message.reply_text(
        "**⏸ 𝐑𝐞𝐬𝐮𝐦𝐞𝐝 🌷 ...**\n\n⎿𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐁𝐲 > {}".format(message.from_user.mention)
    )



# Power𝐞𝐝 By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 
