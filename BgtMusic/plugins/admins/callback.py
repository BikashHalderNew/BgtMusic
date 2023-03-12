# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 

import random

from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup

from modules.config import (AUTO_DOWNLOADS_CLEAR, BANNED_USERS,
                    SOUNCLOUD_IMG_URL, STREAM_IMG_URL,
                    TELEGRAM_AUDIO_URL, TELEGRAM_VIDEO_URL, adminlist)
from modules import YouTube, app
from modules.core.call import Aditya
from modules.misc import SUDOERS, db
from modules.utils.database import (is_active_chat,
                                       is_music_playing, is_muted,
                                       is_nonadmin_chat, music_off,
                                       music_on, mute_off, mute_on,
                                       set_loop)
from modules.utils.decorators.language import languageCB
from modules.utils.formatters import seconds_to_min
from modules.utils.inline.play import (panel_markup_1,
                                          panel_markup_2,
                                          panel_markup_3,
                                          stream_markup,
                                          telegram_markup)
from modules.utils.stream.autoclear import auto_clean
from modules.utils.thumbnails import gen_thumb

wrong = {}


@app.on_callback_query(filters.regex("PanelMarkup") & ~BANNED_USERS)
@languageCB
async def markup_panel(client, CallbackQuery: CallbackQuery, _):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    videoid, chat_id = callback_request.split("|")
    chat_id = CallbackQuery.message.chat.id
    buttons = panel_markup_1(_, videoid, chat_id)
    try:
        await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except:
        return
    if chat_id not in wrong:
        wrong[chat_id] = {}
    wrong[chat_id][CallbackQuery.message.message_id] = False


@app.on_callback_query(filters.regex("MainMarkup") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, CallbackQuery, _):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    videoid, chat_id = callback_request.split("|")
    if videoid == str(None):
        buttons = telegram_markup(_, chat_id)
    else:
        buttons = stream_markup(_, videoid, chat_id)
    chat_id = CallbackQuery.message.chat.id
    try:
        await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except:
        return
    if chat_id not in wrong:
        wrong[chat_id] = {}
    wrong[chat_id][CallbackQuery.message.message_id] = True


@app.on_callback_query(filters.regex("Pages") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, CallbackQuery, _):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    state, pages, videoid, chat = callback_request.split("|")
    chat_id = int(chat)
    pages = int(pages)
    if state == "Forw":
        if pages == 0:
            buttons = panel_markup_2(_, videoid, chat_id)
        if pages == 2:
            buttons = panel_markup_1(_, videoid, chat_id)
        if pages == 1:
            buttons = panel_markup_3(_, videoid, chat_id)
    if state == "Back":
        if pages == 2:
            buttons = panel_markup_2(_, videoid, chat_id)
        if pages == 1:
            buttons = panel_markup_1(_, videoid, chat_id)
        if pages == 0:
            buttons = panel_markup_3(_, videoid, chat_id)
    try:
        await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except:
        return


downvote = {}
downvoters = {}


@app.on_callback_query(filters.regex("ADMIN") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    command, chat = callback_request.split("|")
    chat_id = int(chat)
    if not await is_active_chat(chat_id):
        return await CallbackQuery.answer(
            "❌ 𝐁𝐨𝐭 𝐢𝐬 𝐍𝐨𝐭 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠\n𝐎𝐧 𝐕𝐂❗...", show_alert=True
        )
    mention = CallbackQuery.from_user.mention
    is_non_admin = await is_nonadmin_chat(
        CallbackQuery.message.chat.id
    )
    if not is_non_admin:
        if CallbackQuery.from_user.id not in SUDOERS:
            admins = adminlist.get(CallbackQuery.message.chat.id)
            if not admins:
                return await CallbackQuery.answer(
                    "❌ 𝐀𝐝𝐦𝐢𝐧 𝐋𝐢𝐬𝐭 𝐍𝐨𝐭 𝐅𝐨𝐮𝐧𝐝\n\n𝐏𝐥𝐞𝐚𝐬𝐞 𝐑𝐞𝐥𝐨𝐚𝐝 𝐀𝐝𝐦𝐢𝐧𝐥𝐢𝐬𝐭 𝐕𝐢𝐚 /admincache 𝐎𝐫 /reload", show_alert=True
                )
            else:
                if CallbackQuery.from_user.id not in admins:
                    return await CallbackQuery.answer(
                        "🤖 𝐒𝐨𝐫𝐫𝐲 𝐘𝐨𝐮 𝐃𝐨𝐧'𝐭 𝐇𝐚𝐯𝐞 𝐌𝐚𝐧𝐚𝐠𝐞 𝐕𝐂 𝐏𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧 ✨ ...", show_alert=True
                    )
    if command == "Pause":
        if not await is_music_playing(chat_id):
            return await CallbackQuery.answer(
                "🔈 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐏𝐚𝐮𝐬𝐞𝐝 ✨ ...", show_alert=True
            )
        await CallbackQuery.answer()
        await music_off(chat_id)
        await Aditya.pause_stream(chat_id)
        await CallbackQuery.message.reply_text(
            "**▶️ 𝐏𝐚𝐮𝐬𝐞𝐝 🌷 ...**".format(mention)
        )
    elif command == "Resume":
        if await is_music_playing(chat_id):
            return await CallbackQuery.answer(
                "🔊 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 ✨ ...", show_alert=True
            )
        await CallbackQuery.answer()
        await music_on(chat_id)
        await Aditya.resume_stream(chat_id)
        await CallbackQuery.message.reply_text(
            "**⏸ 𝐑𝐞𝐬𝐮𝐦𝐞𝐝 🌷 ...**".format(mention)
        )
    elif command == "Stop" or command == "End":
        await CallbackQuery.answer()
        await Aditya.stop_stream(chat_id)
        await set_loop(chat_id, 0)
        await CallbackQuery.message.reply_text(
            "**❌ 𝐒𝐭𝐨𝐩𝐩𝐞𝐝 ❌ ...**".format(mention)
        )
    elif command == "Mute":
        if await is_muted(chat_id):
            return await CallbackQuery.answer(
                "🔇 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐌𝐮𝐭𝐞𝐝 🌷 ...", show_alert=True
            )
        await CallbackQuery.answer()
        await mute_on(chat_id)
        await Aditya.mute_stream(chat_id)
        await CallbackQuery.message.reply_text(
            "**🔇 𝐌𝐮𝐭𝐞𝐝 🌷 ...**".format(mention)
        )
    elif command == "Unmute":
        if not await is_muted(chat_id):
            return await CallbackQuery.answer(
                "🔊 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 ✨ ...", show_alert=True
            )
        await CallbackQuery.answer()
        await mute_off(chat_id)
        await Aditya.unmute_stream(chat_id)
        await CallbackQuery.message.reply_text(
            "**🔊 𝐔𝐧𝐦𝐮𝐭𝐞𝐝 🌷 ...**".format(mention)
        )
    elif command == "Loop":
        await CallbackQuery.answer()
        await set_loop(chat_id, 3)
        await CallbackQuery.message.reply_text(
            "**✅ 𝐋𝐨𝐨𝐩 𝐄𝐧𝐚𝐛𝐥𝐞𝐝 𝐁𝐲 {0} 𝐅𝐨𝐫 {1} 𝐓𝐢𝐦𝐞𝐬. 𝐁𝐨𝐭 𝐖𝐢𝐥𝐥 𝐍𝐨𝐰 𝐑𝐞𝐩𝐞𝐚𝐭 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 𝐌𝐮𝐬𝐢𝐜 𝐎𝐧 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 𝐅𝐨𝐫 {1} 𝐓𝐢𝐦𝐞𝐬**".format(mention, 3)
        )
    elif command == "Shuffle":
        check = db.get(chat_id)
        if not check:
            return await CallbackQuery.answer(
                "**❌ 𝐍𝐨𝐭𝐡𝐢𝐧𝐠 𝐢𝐧𝐬𝐢𝐝𝐞 𝐐𝐮𝐞𝐮𝐞 𝐓𝐨 𝐒𝐡𝐮𝐟𝐟𝐥𝐞❗...**", show_alert=True
            )
        try:
            popped = check.pop(0)
        except:
            return await CallbackQuery.answer(
                _["admin_22"], show_alert=True
            )
        check = db.get(chat_id)
        if not check:
            check.insert(0, popped)
            return await CallbackQuery.answer(
                "❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐒𝐡𝐮𝐟𝐟𝐥𝐞.\n\n𝐂𝐡𝐞𝐜𝐤 𝐐𝐮𝐞𝐮𝐞 : /queue", show_alert=True
            )
        await CallbackQuery.answer()
        random.shuffle(check)
        check.insert(0, popped)
        await CallbackQuery.message.reply_text(
            "**✅ 𝐐𝐮𝐞𝐮𝐞 𝐒𝐡𝐮𝐟𝐟𝐥𝐞𝐝 𝐁𝐲 {0}**\n\n**𝐂𝐡𝐞𝐜𝐤 𝐒𝐡𝐮𝐟𝐟𝐥𝐞𝐝 𝐐𝐮𝐞𝐮𝐞 :** /queue".format(mention)
        )
    elif command == "Skip":
        check = db.get(chat_id)
        txt = f"**✅ 𝐒𝐤𝐢𝐩𝐩𝐞𝐝 𝐁𝐲 {mention}**"
        popped = None
        try:
            popped = check.pop(0)
            if popped:
                if AUTO_DOWNLOADS_CLEAR == str(True):
                    await auto_clean(popped)
            if not check:
                await CallbackQuery.edit_message_text(
                    f"**✅ 𝐒𝐤𝐢𝐩𝐩𝐞𝐝 𝐁𝐲 {mention}**"
                )
                await CallbackQuery.message.reply_text(
                    "**🥀 𝐄𝐦𝐩𝐭𝐲 𝐐𝐮𝐞𝐮𝐞, 𝐋𝐞𝐚𝐯𝐢𝐧𝐠\n𝐅𝐫𝐨𝐦 𝐕𝐂 ✨...**".format(mention)
                )
                try:
                    return await Aditya.stop_stream(chat_id)
                except:
                    return
        except:
            try:
                await CallbackQuery.edit_message_text(
                    f"**✅ 𝐒𝐤𝐢𝐩𝐩𝐞𝐝 𝐁𝐲 {mention}**"
                )
                await CallbackQuery.message.reply_text(
                    "**🥀 𝐄𝐦𝐩𝐭𝐲 𝐐𝐮𝐞𝐮𝐞, 𝐋𝐞𝐚𝐯𝐢𝐧𝐠\n𝐅𝐫𝐨𝐦 𝐕𝐂 ✨...**".format(mention)
                )
                return await Aditya.stop_stream(chat_id)
            except:
                return
        await CallbackQuery.answer()
        queued = check[0]["file"]
        title = (check[0]["title"]).title()
        user = check[0]["by"]
        streamtype = check[0]["streamtype"]
        videoid = check[0]["vidid"]
        status = True if str(streamtype) == "video" else None
        db[chat_id][0]["played"] = 0
        if "live_" in queued:
            n, link = await YouTube.video(videoid, True)
            if n == 0:
                return await CallbackQuery.message.reply_text(
                    "**🥀 𝐒𝐤𝐢𝐩𝐩𝐢𝐧𝐠 𝐄𝐫𝐫𝐨𝐫, 𝐒𝐨 𝐏𝐥𝐞𝐚𝐬𝐞\n𝐒𝐤𝐢𝐩 𝐀𝐠𝐚𝐢𝐧 ✨ ...**".format(title)
                )
            try:
                await Aditya.skip_stream(chat_id, link, video=status)
            except Exception:
                return await CallbackQuery.message.reply_text(
                    "**🥀 𝐒𝐤𝐢𝐩𝐩𝐢𝐧𝐠 𝐄𝐫𝐫𝐨𝐫, 𝐒𝐨 𝐏𝐥𝐞𝐚𝐬𝐞\n𝐒𝐤𝐢𝐩 𝐀𝐠𝐚𝐢𝐧 ✨ ...**"
                )
            button = telegram_markup(_, chat_id)
            img = await gen_thumb(videoid)
            run = await CallbackQuery.message.reply_photo(
                photo=img,
                caption="**💥 ❰𝐀𝐝𝐢𝐭𝐲𝐚✘𝐏𝐥𝐚𝐲𝐞𝐫❱ 💿 𝐍𝐨𝐰 💞\n🔊 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 😍 𝐎𝐏 🥀 ...**".format(
                    user,
                    f"https://t.me/{app.username}?start=info_{videoid}",
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
            await CallbackQuery.edit_message_text(txt)
        elif "vid_" in queued:
            mystic = await CallbackQuery.message.reply_text(
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
                await Aditya.skip_stream(
                    chat_id, file_path, video=status
                )
            except Exception:
                return await mystic.edit_text("**🥀 𝐒𝐤𝐢𝐩𝐩𝐢𝐧𝐠 𝐄𝐫𝐫𝐨𝐫, 𝐒𝐨 𝐏𝐥𝐞𝐚𝐬𝐞\n𝐒𝐤𝐢𝐩 𝐀𝐠𝐚𝐢𝐧 ✨ ...**")
            button = stream_markup(_, videoid, chat_id)
            img = await gen_thumb(videoid)
            run = await CallbackQuery.message.reply_photo(
                photo=img,
                caption="**💥 ❰𝐁𝐢𝐤𝐚𝐬𝐡✘𝐏𝐥𝐚𝐲𝐞𝐫❱ 💿 𝐍𝐨𝐰 💞\n🔊 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 😍 𝐎𝐏 🥀 ...**".format(
                    user,
                    f"https://t.me/{app.username}?start=info_{videoid}",
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "stream"
            await CallbackQuery.edit_message_text(txt)
            await mystic.delete()
        elif "index_" in queued:
            try:
                await Aditya.skip_stream(
                    chat_id, videoid, video=status
                )
            except Exception:
                return await CallbackQuery.message.reply_text(
                    "**🥀 𝐒𝐤𝐢𝐩𝐩𝐢𝐧𝐠 𝐄𝐫𝐫𝐨𝐫, 𝐒𝐨 𝐏𝐥𝐞𝐚𝐬𝐞\n𝐒𝐤𝐢𝐩 𝐀𝐠𝐚𝐢𝐧 ✨ ...**"
                )
            button = telegram_markup(_, chat_id)
            run = await CallbackQuery.message.reply_photo(
                photo=STREAM_IMG_URL,
                caption="**💥❰𝐁𝐢𝐤𝐚𝐬𝐡✘𝐏𝐥𝐚𝐲𝐞𝐫❱ 💿 𝐍𝐨𝐰 💞\n🔊 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 😍 𝐎𝐏 🥀 ...**".format(user),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
            await CallbackQuery.edit_message_text(txt)
        else:
            try:
                await Aditya.skip_stream(chat_id, queued, video=status)
            except Exception:
                return await CallbackQuery.message.reply_text(
                    "**🥀 𝐒𝐤𝐢𝐩𝐩𝐢𝐧𝐠 𝐄𝐫𝐫𝐨𝐫, 𝐒𝐨 𝐏𝐥𝐞𝐚𝐬𝐞\n𝐒𝐤𝐢𝐩 𝐀𝐠𝐚𝐢𝐧 ✨ ...**"
                )
            if videoid == "telegram":
                button = telegram_markup(_, chat_id)
                run = await CallbackQuery.message.reply_photo(
                    photo=TELEGRAM_AUDIO_URL
                    if str(streamtype) == "audio"
                    else TELEGRAM_VIDEO_URL,
                    caption=_["stream_3"].format(
                        title, check[0]["dur"], user
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "tg"
            elif videoid == "soundcloud":
                button = telegram_markup(_, chat_id)
                run = await CallbackQuery.message.reply_photo(
                    photo=SOUNCLOUD_IMG_URL
                    if str(streamtype) == "audio"
                    else TELEGRAM_VIDEO_URL,
                    caption=_["stream_3"].format(
                        title, check[0]["dur"], user
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "tg"
            else:
                button = stream_markup(_, videoid, chat_id)
                img = await gen_thumb(videoid)
                run = await CallbackQuery.message.reply_photo(
                    photo=img,
                    caption="**💥 ❰𝐁𝐢𝐤𝐚𝐬𝐡✘𝐏𝐥𝐚𝐲𝐞𝐫❱ 💿 𝐍𝐨𝐰 💞\n🔊 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 😍 𝐎𝐏 🥀 ...**".format(
                        user,
                        f"https://t.me/{app.username}?start=info_{videoid}",
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "stream"
            await CallbackQuery.edit_message_text(txt)
    else:
        playing = db.get(chat_id)
        if not playing:
            return await CallbackQuery.answer(
                "🚫 𝐐𝐮𝐞𝐮𝐞𝐝 𝐋𝐢𝐬𝐭 𝐢𝐬 𝐄𝐦𝐩𝐭𝐲❗...", show_alert=True
            )
        duration_seconds = int(playing[0]["seconds"])
        if duration_seconds == 0:
            return await CallbackQuery.answer(
                "🤖 𝐒𝐨𝐫𝐫𝐲 𝐘𝐨𝐮 𝐂𝐚𝐧'𝐭 𝐒𝐞𝐞𝐤 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐒𝐭𝐫𝐞𝐚𝐦. 𝐈𝐭 𝐂𝐚𝐧 𝐎𝐧𝐥𝐲 𝐁𝐞 𝐒𝐤𝐢𝐩𝐩𝐞𝐝 𝐎𝐫 𝐒𝐭𝐨𝐩𝐩𝐞𝐝.", show_alert=True
            )
        file_path = playing[0]["file"]
        if "index_" in file_path or "live_" in file_path:
            return await CallbackQuery.answer(
                "🤖 𝐒𝐨𝐫𝐫𝐲 𝐘𝐨𝐮 𝐂𝐚𝐧'𝐭 𝐒𝐞𝐞𝐤 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐒𝐭𝐫𝐞𝐚𝐦. 𝐈𝐭 𝐂𝐚𝐧 𝐎𝐧𝐥𝐲 𝐁𝐞 𝐒𝐤𝐢𝐩𝐩𝐞𝐝 𝐎𝐫 𝐒𝐭𝐨𝐩𝐩𝐞𝐝.", show_alert=True
            )
        duration_played = int(playing[0]["played"])
        if int(command) in [1, 2]:
            duration_to_skip = 10
        else:
            duration_to_skip = 30
        duration = playing[0]["dur"]
        if int(command) in [1, 3]:
            if (duration_played - duration_to_skip) <= 10:
                bet = seconds_to_min(duration_played)
                return await CallbackQuery.answer(
                    f"🤖 𝐈 𝐚𝐦 𝐍𝐨𝐭 𝐀𝐛𝐥𝐞 𝐓𝐨 𝐒𝐞𝐞𝐤 𝐃𝐮𝐞 𝐓𝐨 𝐓𝐨𝐭𝐚𝐥 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 𝐇𝐚𝐬 𝐁𝐞𝐞𝐧 𝐄𝐱𝐜𝐞𝐞𝐝𝐞𝐝.\n\n𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐏𝐥𝐚𝐲𝐞𝐝** {bet}** 𝐌𝐢𝐧𝐬 𝐎𝐮𝐭 𝐎𝐟 **{duration}** 𝐌𝐢𝐧𝐬**",
                    show_alert=True,
                )
            to_seek = duration_played - duration_to_skip + 1
        else:
            if (
                duration_seconds
                - (duration_played + duration_to_skip)
            ) <= 10:
                bet = seconds_to_min(duration_played)
                return await CallbackQuery.answer(
                    f"🤖 𝐈 𝐚𝐦 𝐍𝐨𝐭 𝐀𝐛𝐥𝐞 𝐓𝐨 𝐒𝐞𝐞𝐤 𝐃𝐮𝐞 𝐓𝐨 𝐓𝐨𝐭𝐚𝐥 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 𝐇𝐚𝐬 𝐁𝐞𝐞𝐧 𝐄𝐱𝐜𝐞𝐞𝐝𝐞𝐝.\n\n𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐏𝐥𝐚𝐲𝐞𝐝** {bet}** 𝐌𝐢𝐧𝐬 𝐎𝐮𝐭 𝐎𝐟 **{duration}** 𝐌𝐢𝐧𝐬",
                    show_alert=True,
                )
            to_seek = duration_played + duration_to_skip + 1
        await CallbackQuery.answer()
        mystic = await CallbackQuery.message.reply_text(_["admin_32"])
        if "vid_" in file_path:
            n, file_path = await YouTube.video(
                playing[0]["vidid"], True
            )
            if n == 0:
                return await mystic.edit_text("**🤖 𝐒𝐨𝐫𝐫𝐲 𝐘𝐨𝐮 𝐂𝐚𝐧'𝐭 𝐒𝐞𝐞𝐤 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐒𝐭𝐫𝐞𝐚𝐦. 𝐈𝐭 𝐂𝐚𝐧 𝐎𝐧𝐥𝐲 𝐁𝐞 𝐒𝐤𝐢𝐩𝐩𝐞𝐝 𝐎𝐫 𝐒𝐭𝐨𝐩𝐩𝐞𝐝.**")
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
        if int(command) in [1, 3]:
            db[chat_id][0]["played"] -= duration_to_skip
        else:
            db[chat_id][0]["played"] += duration_to_skip
        string = _["admin_33"].format(seconds_to_min(to_seek))
        await mystic.edit_text(
            f"**{string}\n\n𝐂𝐡𝐚𝐧𝐠𝐞𝐬 𝐃𝐨𝐧𝐞 𝐁𝐲: {mention}**"
        )



# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 