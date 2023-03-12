# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 

import random

from pyrogram import filters
from pyrogram.types import Message

from modules.config import BANNED_USERS
from modules.utils.helpers.filters import command
from modules import app
from modules.misc import db
from modules.utils.decorators import AdminRightsCheck


@app.on_message(
    command(["shuffle", "cshuffle"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def admins(Client, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text("**❌ 𝐄𝐫𝐫𝐨𝐫, 𝐖𝐫𝐨𝐧𝐠 𝐔𝐬𝐚𝐠𝐞 𝐎𝐟 𝐂𝐨𝐦𝐦𝐚𝐧𝐝❗...**")
    check = db.get(chat_id)
    if not check:
        return await message.reply_text("**❌ 𝐍𝐨𝐭𝐡𝐢𝐧𝐠 𝐢𝐧𝐬𝐢𝐝𝐞 𝐐𝐮𝐞𝐮𝐞 𝐓𝐨 𝐒𝐡𝐮𝐟𝐟𝐥𝐞❗...**")
    try:
        popped = check.pop(0)
    except:
        return await message.reply_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐒𝐡𝐮𝐟𝐟𝐥𝐞.\n\n𝐂𝐡𝐞𝐜𝐤 𝐐𝐮𝐞𝐮𝐞 :** /queue")
    check = db.get(chat_id)
    if not check:
        check.insert(0, popped)
        return await message.reply_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐒𝐡𝐮𝐟𝐟𝐥𝐞.\n\n𝐂𝐡𝐞𝐜𝐤 𝐐𝐮𝐞𝐮𝐞 :** /queue")
    random.shuffle(check)
    check.insert(0, popped)
    await message.reply_text(
        "**✅ 𝐐𝐮𝐞𝐮𝐞 𝐒𝐡𝐮𝐟𝐟𝐥𝐞𝐝 𝐁𝐲 {0}**\n\n**𝐂𝐡𝐞𝐜𝐤 𝐒𝐡𝐮𝐟𝐟𝐥𝐞𝐝 𝐐𝐮𝐞𝐮𝐞 :** /queue".format(message.from_user.first_name)
    )



# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 