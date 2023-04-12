# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

from modules import config
from modules.config import BANNED_USERS
from modules.utils.helpers.filters import command
from modules import YouTube, app
from modules.core.call import Aditya
from modules.misc import db
from modules.utils.database import get_loop
from modules.utils.decorators import AdminRightsCheck
from modules.utils.inline.play import (stream_markup,
                                          telegram_markup)
from modules.utils.stream.autoclear import auto_clean
from modules.utils.thumbnails import gen_thumb


@app.on_message(
    filters.command(["skip", "cskip"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def skip(cli, message: Message, _, chat_id):
    if not len(message.command) < 2:
        loop = await get_loop(chat_id)
        if loop != 0:
            return await message.reply_text("**🥀 𝐏𝐥𝐞𝐚𝐬𝐞, 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐃𝐢𝐬𝐚𝐛𝐥𝐞 𝐋𝐨𝐨𝐩 𝐏𝐥𝐚𝐲 ✨ ...**")
        state = message.text.split(None, 1)[1].strip()
        if state.isnumeric():
            state = int(state)
            check = db.get(chat_id)
            if check:
                count = len(check)
                if count > 2:
                    count = int(count - 1)
                    if 1 <= state <= count:
                        for x in range(state):
                            popped = None
                            try:
                                popped = check.pop(0)
                            except:
                                return await message.reply_text(
                                    "**❌𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐒𝐤𝐢𝐩 𝐓𝐨 𝐒𝐩𝐞𝐜𝐢𝐟𝐢𝐜 𝐒𝐨𝐧𝐠 ✨ ...\n\n✅ 𝐂𝐡𝐞𝐜𝐤 𝐋𝐞𝐟𝐭 𝐐𝐮𝐞𝐮𝐞 𝐁𝐲 »** /queue"
                                )
                            if popped:
                                if (
                                    config.AUTO_DOWNLOADS_CLEAR
                                    == str(True)
                                ):
                                    await auto_clean(popped)
                            if not check:
                                try:
                                    await message.reply_text(
                                        "**🥀 𝐄𝐦𝐩𝐭𝐲 𝐐𝐮𝐞𝐮𝐞, 𝐋𝐞𝐚𝐯𝐢𝐧𝐠\n𝐅𝐫𝐨𝐦 𝐕𝐂 ✨...**".format(
                                            message.from_user.first_name
                                        )
                                    )
                                    await Aditya.stop_stream(chat_id)
                                except:
                                    return
                                break
                    else:
                        return await message.reply_text(
                            "**❌ 𝐍𝐨𝐭 𝐄𝐧𝐨𝐮𝐠𝐡 𝐓𝐫𝐚𝐜𝐤𝐬 𝐢𝐧 𝐐𝐮𝐞𝐮𝐞 𝐅𝐨𝐫 𝐓𝐡𝐞 𝐕𝐚𝐥𝐮𝐞 𝐆𝐢𝐯𝐞𝐧 𝐁𝐲 𝐘𝐨𝐮. 🥀 𝐏𝐥𝐞𝐚𝐬𝐞 𝐂𝐡𝐨𝐨𝐬𝐞 𝐍𝐮𝐦𝐛𝐞𝐫𝐬 𝐁𝐞𝐭𝐰𝐞𝐞𝐧 1 𝐚𝐧𝐝 {0} ✨ ...**".format(count)
                        )
                else:
                    return await message.reply_text("**✅ 𝐀𝐭𝐥𝐞𝐚𝐬𝐭 𝟐 𝐒𝐨𝐧𝐠𝐬 𝐍𝐞𝐞𝐝𝐞𝐝 𝐢𝐧 𝐐𝐮𝐞𝐮𝐞 𝐓𝐨 𝐒𝐤𝐢𝐩 𝐓𝐨 𝐚 𝐒𝐩𝐞𝐜𝐢𝐟𝐢𝐜 𝐍𝐮𝐦𝐛𝐞𝐫. 𝐂𝐡𝐞𝐜𝐤 𝐐𝐮𝐞𝐮𝐞 𝐁𝐲 »** /queue")
            else:
                return await message.reply_text("**🚫 𝐐𝐮𝐞𝐮𝐞𝐝 𝐋𝐢𝐬𝐭 𝐢𝐬 𝐄𝐦𝐩𝐭𝐲❗...**")
        else:
            return await message.reply_text("**✅ 𝐏𝐥𝐞𝐚𝐬𝐞 𝐔𝐬𝐞 𝐍𝐮𝐦𝐞𝐫𝐢𝐜 𝐍𝐮𝐦𝐛𝐞𝐫𝐬 𝐅𝐨𝐫 𝐒𝐩𝐞𝐜𝐢𝐟𝐢𝐜 𝐒𝐨𝐧𝐠𝐬, 𝐋𝐢𝐤𝐞 𝟏, 𝟐, 𝟑 𝐎𝐫 𝟒 𝐄𝐭𝐜 ✨ **...")
    else:
        check = db.get(chat_id)
        popped = None
        try:
            popped = check.pop(0)
            if popped:
                if config.AUTO_DOWNLOADS_CLEAR == str(True):
                    await auto_clean(popped)
            if not check:
                await message.reply_text(
                    "**🥀 𝐄𝐦𝐩𝐭𝐲 𝐐𝐮𝐞𝐮𝐞, 𝐋𝐞𝐚𝐯𝐢𝐧𝐠\n𝐅𝐫𝐨𝐦 𝐕𝐂 ✨...**".format(message.from_user.first_name)
                )
                try:
                    return await Aditya.stop_stream(chat_id)
                except:
                    return
        except:
            try:
                await message.reply_text(
                    "**🥀 𝐄𝐦𝐩𝐭𝐲 𝐐𝐮𝐞𝐮𝐞, 𝐋𝐞𝐚𝐯𝐢𝐧𝐠\n𝐅𝐫𝐨𝐦 𝐕𝐂 ✨...**".format(message.from_user.first_name)
                )
                return await Aditya.stop_stream(chat_id)
            except:
                return
    queued = check[0]["file"]
    title = (check[0]["title"]).title()
    user = check[0]["by"]
    streamtype = check[0]["streamtype"]
    videoid = check[0]["vidid"]
    status = True if str(streamtype) == "video" else None
    if "live_" in queued:
        n, link = await YouTube.video(videoid, True)
        if n == 0:
            return await message.reply_text(
                "**🥀 𝐒𝐤𝐢𝐩𝐩𝐢𝐧𝐠 𝐄𝐫𝐫𝐨𝐫, 𝐒𝐨 𝐏𝐥𝐞𝐚𝐬𝐞\n𝐒𝐤𝐢𝐩 𝐀𝐠𝐚𝐢𝐧 ✨ ...**".format(title)
            )
        try:
            await Aditya.skip_stream(chat_id, link, video=status)
        except Exception:
            return await message.reply_text("**🥀 𝐒𝐤𝐢𝐩𝐩𝐢𝐧𝐠 𝐄𝐫𝐫𝐨𝐫, 𝐒𝐨 𝐏𝐥𝐞𝐚𝐬𝐞\n𝐒𝐤𝐢𝐩 𝐀𝐠𝐚𝐢𝐧 ✨ ...**")
        button = telegram_markup(_, chat_id)
        img = await gen_thumb(videoid)
        run = await message.reply_photo(
            photo=img,
            caption="**💥 ❰𝐁𝐢𝐤𝐚𝐬𝐡✘𝐏𝐥𝐚𝐲𝐞𝐫❱ 💿 𝐍𝐨𝐰 💞\n🔊 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 😍 𝐎𝐏 🥀 ...**".format(
                user,
                f"https://t.me/{app.username}?start=info_{videoid}",
            ),
            reply_markup=InlineKeyboardMarkup(button),
        )
        db[chat_id][0]["mystic"] = run
        db[chat_id][0]["markup"] = "tg"
    elif "vid_" in queued:
        mystic = await message.reply_text(
            "**✅ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐍𝐞𝐱𝐭 𝐒𝐨𝐧𝐠\n𝐅𝐫𝐨𝐦 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 💞 ...**", disable_web_page_preview=True
        )
        try:
            file_path, direct = await YouTube.download(
                videoid,
                mystic,
                videoid=True,
                video=status,
            )
        except:
            return await mystic.edit_text("**🥀 𝐒𝐤𝐢𝐩𝐩𝐢𝐧𝐠 𝐄𝐫𝐫𝐨𝐫, 𝐒𝐨 𝐏𝐥𝐞𝐚𝐬𝐞\n𝐒𝐤𝐢𝐩 𝐀𝐠𝐚𝐢𝐧 ✨ ...**")
        try:
            await Aditya.skip_stream(chat_id, file_path, video=status)
        except Exception:
            return await mystic.edit_text("**🥀 𝐒𝐤𝐢𝐩𝐩𝐢𝐧𝐠 𝐄𝐫𝐫𝐨𝐫, 𝐒𝐨 𝐏𝐥𝐞𝐚𝐬𝐞\n𝐒𝐤𝐢𝐩 𝐀𝐠𝐚𝐢𝐧 ✨ ...**")
        button = stream_markup(_, videoid, chat_id)
        img = await gen_thumb(videoid)
        run = await message.reply_photo(
            photo=img,
            caption="**💥 ❰𝐁𝐢𝐤𝐚𝐬𝐡✘𝐏𝐥𝐚𝐲𝐞𝐫❱ 💿 𝐍𝐨𝐰 💞\n🔊 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 😍 𝐎𝐏 🥀 ...**".format(
                user,
                f"https://t.me/{app.username}?start=info_{videoid}",
            ),
            reply_markup=InlineKeyboardMarkup(button),
        )
        db[chat_id][0]["mystic"] = run
        db[chat_id][0]["markup"] = "stream"
        await mystic.delete()
    elif "index_" in queued:
        try:
            await Aditya.skip_stream(chat_id, videoid, video=status)
        except Exception:
            return await message.reply_text("**🥀 𝐒𝐤𝐢𝐩𝐩𝐢𝐧𝐠 𝐄𝐫𝐫𝐨𝐫, 𝐒𝐨 𝐏𝐥𝐞𝐚𝐬𝐞\n𝐒𝐤𝐢𝐩 𝐀𝐠𝐚𝐢𝐧 ✨ ...**")
        button = telegram_markup(_, chat_id)
        run = await message.reply_photo(
            photo=config.STREAM_IMG_URL,
            caption="**💥 ❰𝐁𝐢𝐤𝐚𝐬𝐡✘𝐏𝐥𝐚𝐲𝐞𝐫❱ 💿 𝐍𝐨𝐰 💞\n🔊 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 😍 𝐎𝐏 🥀 ...**".format(user),
            reply_markup=InlineKeyboardMarkup(button),
        )
        db[chat_id][0]["mystic"] = run
        db[chat_id][0]["markup"] = "tg"
    else:
        try:
            await Aditya.skip_stream(chat_id, queued, video=status)
        except Exception:
            return await message.reply_text("**🥀 𝐒𝐤𝐢𝐩𝐩𝐢𝐧𝐠 𝐄𝐫𝐫𝐨𝐫, 𝐒𝐨 𝐏𝐥𝐞𝐚𝐬𝐞\n𝐒𝐤𝐢𝐩 𝐀𝐠𝐚𝐢𝐧 ✨ ...**")
        if videoid == "telegram":
            button = telegram_markup(_, chat_id)
            run = await message.reply_photo(
                photo=config.TELEGRAM_AUDIO_URL
                if str(streamtype) == "audio"
                else config.TELEGRAM_VIDEO_URL,
                caption="**💥 ❰𝐁𝐢𝐤𝐚𝐬𝐡✘𝐏𝐥𝐚𝐲𝐞𝐫❱ 💿 𝐍𝐨𝐰 💞\n🔊 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 😍 𝐎𝐏 🥀 ...**".format(
                    title, check[0]["dur"], user
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
        elif videoid == "soundcloud":
            button = telegram_markup(_, chat_id)
            run = await message.reply_photo(
                photo=config.SOUNCLOUD_IMG_URL
                if str(streamtype) == "audio"
                else config.TELEGRAM_VIDEO_URL,
                caption="**💥 ❰𝐁𝐢𝐤𝐚𝐬𝐡✘𝐏𝐥𝐚𝐲𝐞𝐫❱ 💿 𝐍𝐨𝐰 💞\n🔊 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 😍 𝐎𝐏 🥀 ...**".format(
                    title, check[0]["dur"], user
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
        else:
            button = stream_markup(_, videoid, chat_id)
            img = await gen_thumb(videoid)
            run = await message.reply_photo(
                photo=img,
                caption="**💥 ❰𝐁𝐢𝐤𝐚𝐬𝐡✘𝐏𝐥𝐚𝐲𝐞𝐫❱ 💿 𝐍𝐨𝐰 💞\n🔊 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 😍 𝐎𝐏 🥀 ...**".format(
                    user,
                    f"https://t.me/{app.username}?start=info_{videoid}",
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "stream"




# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 
