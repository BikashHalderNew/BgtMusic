# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 

from pyrogram import filters
from pyrogram.types import Message

from modules.config import BANNED_USERS, adminlist
from modules.utils.helpers.filters import command
from modules import app
from modules.utils.database import (delete_authuser, get_authuser,
                                       get_authuser_names,
                                       save_authuser)
from modules.utils.decorators import AdminActual, language
from modules.utils.formatters import int_to_alpha


@app.on_message(
    command(["auth"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminActual
async def auth(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("**🥀 𝐑𝐞𝐩𝐥𝐲 𝐓𝐨 𝐚 𝐔𝐬𝐞𝐫'𝐬 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐎𝐫 𝐆𝐢𝐯𝐞 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞/𝐔𝐬𝐞𝐫 𝐈𝐃 ✨ ...**")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        user_id = message.from_user.id
        token = await int_to_alpha(user.id)
        from_user_name = message.from_user.first_name
        from_user_id = message.from_user.id
        _check = await get_authuser_names(message.chat.id)
        count = len(_check)
        if int(count) == 20:
            return await message.reply_text("**🥀 𝐘𝐨𝐮 𝐂𝐚𝐧 𝐎𝐧𝐥𝐲 𝐇𝐚𝐯𝐞 𝟐𝟎 𝐔𝐬𝐞𝐫𝐬\n𝐢𝐧 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝 𝐔𝐬𝐞𝐫𝐬\n𝐋𝐢𝐬𝐭 (𝐀𝐔𝐋) ✨ ...**")
        if token not in _check:
            assis = {
                "auth_user_id": user.id,
                "auth_name": user.first_name,
                "admin_id": from_user_id,
                "admin_name": from_user_name,
            }
            get = adminlist.get(message.chat.id)
            if get:
                if user.id not in get:
                    get.append(user.id)
            await save_authuser(message.chat.id, token, assis)
            return await message.reply_text("**✅ 𝐀𝐝𝐝𝐞𝐝 𝐓𝐨 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝 𝐔𝐬𝐞𝐫𝐬\n𝐋𝐢𝐬𝐭 𝐎𝐟 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ✨ ...**")
        else:
            await message.reply_text("**✅ 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐢𝐧 𝐓𝐡𝐞 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝\n𝐔𝐬𝐞𝐫𝐬 𝐋𝐢𝐬𝐭 💞 ...**")
        return
    from_user_id = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    user_name = message.reply_to_message.from_user.first_name
    token = await int_to_alpha(user_id)
    from_user_name = message.from_user.first_name
    _check = await get_authuser_names(message.chat.id)
    count = 0
    for smex in _check:
        count += 1
    if int(count) == 20:
        return await message.reply_text("**🥀 𝐘𝐨𝐮 𝐂𝐚𝐧 𝐎𝐧𝐥𝐲 𝐇𝐚𝐯𝐞 𝟐𝟎 𝐔𝐬𝐞𝐫𝐬\n𝐢𝐧 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝 𝐔𝐬𝐞𝐫𝐬\n𝐋𝐢𝐬𝐭 (𝐀𝐔𝐋) ✨ ...**")
    if token not in _check:
        assis = {
            "auth_user_id": user_id,
            "auth_name": user_name,
            "admin_id": from_user_id,
            "admin_name": from_user_name,
        }
        get = adminlist.get(message.chat.id)
        if get:
            if user_id not in get:
                get.append(user_id)
        await save_authuser(message.chat.id, token, assis)
        return await message.reply_text("**✅ 𝐀𝐝𝐝𝐞𝐝 𝐓𝐨 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝 𝐔𝐬𝐞𝐫𝐬\n𝐋𝐢𝐬𝐭 𝐎𝐟 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ✨ ...**")
    else:
        await message.reply_text("**✅ 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐢𝐧 𝐓𝐡𝐞 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝\n𝐔𝐬𝐞𝐫𝐬 𝐋𝐢𝐬𝐭 💞 ...**")


@app.on_message(
    command(["unauth"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminActual
async def unauthusers(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("**🥀 𝐑𝐞𝐩𝐥𝐲 𝐓𝐨 𝐚 𝐔𝐬𝐞𝐫'𝐬 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐎𝐫 𝐆𝐢𝐯𝐞 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞/𝐔𝐬𝐞𝐫 𝐈𝐃 ✨ ...**")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        token = await int_to_alpha(user.id)
        deleted = await delete_authuser(message.chat.id, token)
        get = adminlist.get(message.chat.id)
        if get:
            if user.id in get:
                get.remove(user.id)
        if deleted:
            return await message.reply_text("**✅ 𝐑𝐞𝐦𝐨𝐯𝐞𝐝 𝐅𝐫𝐨𝐦 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝\n𝐔𝐬𝐞𝐫𝐬 𝐋𝐢𝐬𝐭 𝐎𝐟 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ✨ ...**")
        else:
            return await message.reply_text("**❌ 𝐓𝐚𝐫𝐠𝐞𝐭𝐞𝐝 𝐔𝐬𝐞𝐫 𝐢𝐬 𝐍𝐨𝐭 𝐀𝐧 \n𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝 𝐔𝐬𝐞𝐫❗...**")
    user_id = message.reply_to_message.from_user.id
    token = await int_to_alpha(user_id)
    deleted = await delete_authuser(message.chat.id, token)
    get = adminlist.get(message.chat.id)
    if get:
        if user_id in get:
            get.remove(user_id)
    if deleted:
        return await message.reply_text("**✅ 𝐑𝐞𝐦𝐨𝐯𝐞𝐝 𝐅𝐫𝐨𝐦 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝\n𝐔𝐬𝐞𝐫𝐬 𝐋𝐢𝐬𝐭 𝐎𝐟 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ✨ ...**")
    else:
        return await message.reply_text("**❌ 𝐓𝐚𝐫𝐠𝐞𝐭𝐞𝐝 𝐔𝐬𝐞𝐫 𝐢𝐬 𝐍𝐨𝐭 𝐀𝐧 \n𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝 𝐔𝐬𝐞𝐫❗...**")


@app.on_message(
    command(["authusers"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def authusers(client, message: Message, _):
    _playlist = await get_authuser_names(message.chat.id)
    if not _playlist:
        return await message.reply_text("**❌ 𝐍𝐨 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝 𝐔𝐬𝐞𝐫𝐬 𝐅𝐨𝐮𝐧𝐝\n𝐢𝐧 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩❗...**")
    else:
        j = 0
        mystic = await message.reply_text("**🔃 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭, 𝐅𝐞𝐭𝐜𝐡𝐢𝐧𝐠 𝐀𝐥𝐥\n𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝 𝐔𝐬𝐞𝐫𝐬 ✨ ...**")
        text = "**🤖 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝 𝐔𝐬𝐞𝐫𝐬 𝐋𝐢𝐬𝐭 [𝐀𝐔𝐋]:**\n\n"
        for note in _playlist:
            _note = await get_authuser(message.chat.id, note)
            user_id = _note["auth_user_id"]
            admin_id = _note["admin_id"]
            admin_name = _note["admin_name"]
            try:
                user = await app.get_users(user_id)
                user = user.first_name
                j += 1
            except Exception:
                continue
            text += f"{j}➤ {user}[`{user_id}`]\n"
            text += f"**┗ 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲:-** {admin_name}[`{admin_id}`]\n\n"
        await mystic.delete()
        await message.reply_text(text)
        
        
        
        
# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 