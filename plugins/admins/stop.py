# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 

from pyrogram import filters
from pyrogram.types import Message

from modules.config import BANNED_USERS
from modules.utils.helpers.filters import command
from modules import app
from modules.core.call import Aditya
from modules.utils.database import set_loop
from modules.utils.decorators import AdminRightsCheck


@app.on_message(
    filters.command(["stop", "end", "x", "cstop", "cend"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text("**❌ 𝐄𝐫𝐫𝐨𝐫, 𝐖𝐫𝐨𝐧𝐠 𝐔𝐬𝐚𝐠𝐞 𝐎𝐟 𝐂𝐨𝐦𝐦𝐚𝐧𝐝❗...**")
    await Aditya.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        "**❌ 𝐒𝐭𝐨𝐩𝐩𝐞𝐝 ❌ ...**".format(message.from_user.mention)
    )


# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 
