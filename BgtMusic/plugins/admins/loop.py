# Powered By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 

from pyrogram import filters
from pyrogram.types import Message

from modules.config import BANNED_USERS
from modules import app
from modules.utils.helpers.filters import command
from modules.utils.database.memorydatabase import (get_loop,
                                                      set_loop)
from modules.utils.decorators import AdminRightsCheck


@app.on_message(
    command(["loop", "cloop"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def admins(cli, message: Message, _, chat_id):
    usage = "**✅ 𝐔𝐬𝐚𝐠𝐞:**\n/loop [enable/disable] 𝐎𝐫 [Number between 1-10]\n\n**❗ 𝐄𝐱𝐚𝐦𝐩𝐥𝐞:** /loop 5"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    if state.isnumeric():
        state = int(state)
        if 1 <= state <= 10:
            got = await get_loop(chat_id)
            if got != 0:
                state = got + state
            if int(state) > 10:
                state = 10
            await set_loop(chat_id, state)
            return await message.reply_text(
                "**✅ 𝐋𝐨𝐨𝐩 𝐄𝐧𝐚𝐛𝐥𝐞𝐝 𝐁𝐲 {0} 𝐅𝐨𝐫 {1} 𝐓𝐢𝐦𝐞𝐬. 𝐁𝐨𝐭 𝐖𝐢𝐥𝐥 𝐍𝐨𝐰 𝐑𝐞𝐩𝐞𝐚𝐭 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 𝐌𝐮𝐬𝐢𝐜 𝐎𝐧 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 𝐅𝐨𝐫 {1} 𝐓𝐢𝐦𝐞𝐬**".format(
                    message.from_user.first_name, state
                )
            )
        else:
            return await message.reply_text("**🥀 𝐏𝐥𝐞𝐚𝐬𝐞 𝐔𝐬𝐞 𝐍𝐮𝐦𝐛𝐞𝐫𝐬 𝐁𝐞𝐭𝐰𝐞𝐞𝐧 𝟏-𝟏𝟎 𝐅𝐨𝐫 𝐋𝐨𝐨𝐩 𝐏𝐥𝐚𝐲 ✨ ...**")
    elif state.lower() == "enable":
        await set_loop(chat_id, 10)
        return await message.reply_text(
            "**✅ 𝐋𝐨𝐨𝐩 𝐄𝐧𝐚𝐛𝐥𝐞𝐝 𝐁𝐲 {0} 𝐅𝐨𝐫 {1} 𝐓𝐢𝐦𝐞𝐬. 𝐁𝐨𝐭 𝐖𝐢𝐥𝐥 𝐍𝐨𝐰 𝐑𝐞𝐩𝐞𝐚𝐭 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 𝐌𝐮𝐬𝐢𝐜 𝐎𝐧 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 𝐅𝐨𝐫 {1} 𝐓𝐢𝐦𝐞𝐬**".format(message.from_user.first_name, state)
        )
    elif state.lower() == "disable":
        await set_loop(chat_id, 0)
        return await message.reply_text("**✅ 𝐋𝐨𝐨𝐩 𝐏𝐥𝐚𝐲 𝐇𝐚𝐬 𝐁𝐞𝐞𝐧\n𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝 ✨ ...**")
    else:
        return await message.reply_text(usage)


# Powered By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 