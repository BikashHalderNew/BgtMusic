# Powered By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 

from pyrogram import filters
from pyrogram.types import Message

from modules.config import BANNED_USERS
from modules import app
from modules.core.call import Aditya
from modules.utils.helpers.filters import command
from modules.utils.database import is_music_playing, music_off
from modules.utils.decorators import AdminRightsCheck


@app.on_message(
    filters.command(["pause", "cpause"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text("**❌ 𝐄𝐫𝐫𝐨𝐫, 𝐖𝐫𝐨𝐧𝐠 𝐔𝐬𝐚𝐠𝐞 𝐎𝐟 𝐂𝐨𝐦𝐦𝐚𝐧𝐝❗...**")
    if not await is_music_playing(chat_id):
        return await message.reply_text("**🔈𝐁𝐠𝐭 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐏𝐚𝐮𝐬𝐞𝐝 ✨ ...**")
    await music_off(chat_id)
    await Aditya.pause_stream(chat_id)
    await message.reply_text(
        "**▶️ 𝐏𝐚𝐮𝐬𝐞𝐝 🌷 ...**\n\n⎿𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐁𝐲 > {}".format(message.from_user.mention)
    )


# Powered By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 
