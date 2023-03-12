# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 

from pyrogram import filters
from pyrogram.types import Message

from modules.config import BANNED_USERS
from modules import YouTube, app
from modules.core.call import Aditya
from modules.utils.helpers.filters import command
from modules.misc import db
from modules.utils import AdminRightsCheck, seconds_to_min



@app.on_message(
    command(["seek", "cseek", "seekback", "cseekback"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def seek_comm(cli, message: Message, _, chat_id):
    if len(message.command) == 1:
        return await message.reply_text("**✅ 𝐔𝐬𝐬𝐚𝐠𝐞:**\n/seek 𝐎𝐫 /seekback [𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 𝐢𝐧 𝐒𝐞𝐜𝐨𝐧𝐝𝐬]")
    query = message.text.split(None, 1)[1].strip()
    if not query.isnumeric():
        return await message.reply_text("**✅ 𝐏𝐥𝐞𝐚𝐬𝐞 𝐔𝐬𝐞 𝟏𝟎-𝟐𝟎-𝟑𝟎 𝐒𝐞𝐜𝐨𝐧𝐝 𝐅𝐨𝐫 𝐒𝐞𝐞𝐤𝐢𝐧𝐠 ✨ ...**")
    playing = db.get(chat_id)
    if not playing:
        return await message.reply_text("**🚫 𝐐𝐮𝐞𝐮𝐞𝐝 𝐋𝐢𝐬𝐭 𝐢𝐬 𝐄𝐦𝐩𝐭𝐲❗...**")
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await message.reply_text("**🤖 𝐒𝐨𝐫𝐫𝐲 𝐘𝐨𝐮 𝐂𝐚𝐧'𝐭 𝐒𝐞𝐞𝐤 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐒𝐭𝐫𝐞𝐚𝐦. 𝐈𝐭 𝐂𝐚𝐧 𝐎𝐧𝐥𝐲 𝐁𝐞 𝐒𝐤𝐢𝐩𝐩𝐞𝐝 𝐎𝐫 𝐒𝐭𝐨𝐩𝐩𝐞𝐝.**")
    file_path = playing[0]["file"]
    if "index_" in file_path or "live_" in file_path:
        return await message.reply_text("**🤖 𝐒𝐨𝐫𝐫𝐲 𝐘𝐨𝐮 𝐂𝐚𝐧'𝐭 𝐒𝐞𝐞𝐤 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐒𝐭𝐫𝐞𝐚𝐦. 𝐈𝐭 𝐂𝐚𝐧 𝐎𝐧𝐥𝐲 𝐁𝐞 𝐒𝐤𝐢𝐩𝐩𝐞𝐝 𝐎𝐫 𝐒𝐭𝐨𝐩𝐩𝐞𝐝.**")
    duration_played = int(playing[0]["played"])
    duration_to_skip = int(query)
    duration = playing[0]["dur"]
    if message.command[0][-2] == "c":
        if (duration_played - duration_to_skip) <= 10:
            return await message.reply_text(
                "**✅ 𝐏𝐥𝐞𝐚𝐬𝐞 𝐆𝐢𝐯𝐞 𝐋𝐨𝐰 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 𝐓𝐨 𝐒𝐞𝐞𝐤 [𝟏𝟎-𝟑𝟎 𝐒𝐞𝐜𝐨𝐧𝐝𝐬] 💞 ...\n\n𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐏𝐥𝐚𝐲𝐞𝐝 {0} 𝐌𝐢𝐧𝐬 𝐎𝐮𝐭 𝐎𝐟 {1} 𝐌𝐢𝐧𝐬**".format(
                    seconds_to_min(duration_played), duration
                )
            )
        to_seek = duration_played - duration_to_skip + 1
    else:
        if (
            duration_seconds - (duration_played + duration_to_skip)
        ) <= 10:
            return await message.reply_text(
                "**✅ 𝐏𝐥𝐞𝐚𝐬𝐞 𝐆𝐢𝐯𝐞 𝐋𝐨𝐰 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 𝐓𝐨 𝐒𝐞𝐞𝐤 [𝟏𝟎-𝟑𝟎 𝐒𝐞𝐜𝐨𝐧𝐝𝐬] 💞 ...\n\n𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐏𝐥𝐚𝐲𝐞𝐝 {0} 𝐌𝐢𝐧𝐬 𝐎𝐮𝐭 𝐎𝐟 {1} 𝐌𝐢𝐧𝐬**".format(
                    seconds_to_min(duration_played), duration
                )
            )
        to_seek = duration_played + duration_to_skip + 1
    mystic = await message.reply_text("**🔃 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭, 💿 𝐒𝐞𝐞𝐤𝐢𝐧𝐠 𝐎𝐧𝐆𝐨𝐢𝐧𝐠 𝐒𝐭𝐫𝐞𝐚𝐦 💞 ....**")
    if "vid_" in file_path:
        n, file_path = await YouTube.video(playing[0]["vidid"], True)
        if n == 0:
            return await message.reply_text("**🤖 𝐒𝐨𝐫𝐫𝐲 𝐘𝐨𝐮 𝐂𝐚𝐧'𝐭 𝐒𝐞𝐞𝐤 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐒𝐭𝐫𝐞𝐚𝐦. 𝐈𝐭 𝐂𝐚𝐧 𝐎𝐧𝐥𝐲 𝐁𝐞 𝐒𝐤𝐢𝐩𝐩𝐞𝐝 𝐎𝐫 𝐒𝐭𝐨𝐩𝐩𝐞𝐝.**")
    try:
        await Aditya.seek_stream(
            chat_id,
            file_path,
            seconds_to_min(to_seek),
            duration,
            playing[0]["streamtype"],
        )
    except:
        return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐒𝐞𝐞𝐤 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐒𝐭𝐫𝐞𝐚𝐦 ✨ ...**")
    if message.command[0][-2] == "c":
        db[chat_id][0]["played"] -= duration_to_skip
    else:
        db[chat_id][0]["played"] += duration_to_skip
    await mystic.edit_text(
        "**✅ 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐒𝐞𝐞𝐤𝐞𝐝 𝐒𝐭𝐫𝐞𝐚𝐦 𝐓𝐨 {0} 𝐌𝐢𝐧𝐬 ✨ ...**".format(seconds_to_min(to_seek))
    )



# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 