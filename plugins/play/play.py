# Powered By @BikashHalder @AdityaHalder

import random
from ast import ExceptHandler

from pyrogram import filters
from pyrogram.types import (InlineKeyboardMarkup, InputMediaPhoto,
                            Message)
from pytgcalls.exceptions import NoActiveGroupCall

from modules import config
from modules.config import BANNED_USERS, lyrical
from modules.utils.helpers.filters import command
from modules import (Apple, Resso, SoundCloud, Spotify, Telegram,
                        YouTube, app)
from modules.core.call import Aditya
from modules.utils import seconds_to_min, time_to_seconds
from modules.utils.channelplay import get_channeplayCB
from modules.utils.database import is_video_allowed
from modules.utils.decorators.language import languageCB
from modules.utils.decorators.play import PlayWrapper
from modules.utils.formatters import formats
from modules.utils.inline.play import (livestream_markup,
                                          playlist_markup,
                                          slider_markup, track_markup)
from modules.utils.inline.playlist import botplaylist_markup
from modules.utils.logger import play_logs
from modules.utils.stream.stream import stream


@app.on_message(
    command(["play", "bgt", "vplay", "cplay", "cvplay", "playforce", "bgtforce", "vplayforce", "cplayforce", "cvplayforce"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@PlayWrapper
async def play_commnd(
    client,
    message: Message,
    _,
    chat_id,
    video,
    channel,
    playmode,
    url,
    fplay,
):
    mystic = await message.reply_text("**🏷𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐏𝐥𝐚𝐲 𝐌𝐨𝐝𝐞**\n\n**🔄 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 ...**\n**𝐋𝐢𝐧𝐤𝐞𝐝 𝐂𝐡𝐚𝐧𝐧𝐞𝐥:** {0}".format(channel) if channel else "**🔄 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 ...**")
    plist_id = None
    slider = None
    plist_type = None
    spotify = None
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    audio_telegram = (
        (
            message.reply_to_message.audio
            or message.reply_to_message.voice
        )
        if message.reply_to_message
        else None
    )
    video_telegram = (
        (
            message.reply_to_message.video
            or message.reply_to_message.document
        )
        if message.reply_to_message
        else None
    )
    if audio_telegram:
        if audio_telegram.file_size > config.TG_AUDIO_FILESIZE_LIMIT:
            return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐝 𝐓𝐨 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐀𝐮𝐝𝐢𝐨 𝐅𝐢𝐥𝐞.**\n\n**𝑨𝒖𝒅𝒊𝒐 𝑭𝒊𝒍𝒆 𝑺𝒊𝒛𝒆 𝑺𝒉𝒐𝒖𝒍𝒅 𝑩𝒆 𝑳𝒆𝒔𝒔 𝑻𝒉𝒂𝒏 __𝟏𝟎𝟎__𝑴𝑩**")
        duration_min = seconds_to_min(audio_telegram.duration)
        if (audio_telegram.duration) > config.DURATION_LIMIT:
            return await mystic.edit_text(
                "**🤖 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 𝐋𝐢𝐦𝐢𝐭 𝐄𝐫𝐫𝐨𝐫❗**\n\n**𝐀𝐥𝐥𝐨𝐰𝐞𝐝 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧: **{0} 𝐌𝐢𝐧𝐮𝐭𝐞(𝐬)\n**𝐑𝐞𝐜𝐞𝐢𝐯𝐞𝐝 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧:** {1} 𝐇𝐨𝐮𝐫(𝐬)".format(
                    config.DURATION_LIMIT_MIN, duration_min
                )
            )
        file_path = await Telegram.get_filepath(audio=audio_telegram)
        if await Telegram.download(_, message, mystic, file_path):
            message_link = await Telegram.get_link(message)
            file_name = await Telegram.get_filename(
                audio_telegram, audio=True
            )
            dur = await Telegram.get_duration(audio_telegram)
            details = {
                "title": file_name,
                "link": message_link,
                "path": file_path,
                "dur": dur,
            }

            try:
                await stream(
                    _,
                    mystic,
                    user_id,
                    details,
                    chat_id,
                    user_name,
                    message.chat.id,
                    streamtype="telegram",
                    forceplay=fplay,
                )
            except Exception as e:
                ex_type = type(e).__name__
                err = (
                    e
                    if ex_type == "AssistantErr"
                    else "**🥀 𝐒𝐨𝐦𝐞 𝐄𝐱𝐜𝐞𝐩𝐭𝐢𝐨𝐧 𝐎𝐜𝐜𝐮𝐫𝐞𝐝, 𝐖𝐡𝐢𝐥𝐞 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐐𝐮𝐞𝐫𝐲.\n\n❗ 𝐄𝐱𝐜𝐞𝐩𝐭𝐢𝐨𝐧 𝐓𝐲𝐩𝐞:-** `{0}`".format(e)
                )
                return await mystic.edit_text(err)
            return await mystic.delete()
        return
    elif video_telegram:
        if not await is_video_allowed(message.chat.id):
            return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐐𝐮𝐞𝐫𝐲 ✨...**")
        if message.reply_to_message.document:
            try:
                ext = video_telegram.file_name.split(".")[-1]
                if ext.lower() not in formats:
                    return await mystic.edit_text(
                        "**❌ 𝐓𝐡𝐢𝐬 𝐅𝐢𝐥𝐞 𝐍𝐨𝐭 𝐀 𝐕𝐚𝐥𝐢𝐝 𝐕𝐢𝐝𝐞𝐨 𝐅𝐢𝐥𝐞 𝐄𝐱𝐭𝐞𝐧𝐭𝐢𝐨𝐧❗**\n\n**𝐒𝐮𝐩𝐩𝐨𝐫𝐭𝐞𝐝 𝐅𝐨𝐫𝐦𝐚𝐭𝐬:** {0}".format(f"{' | '.join(formats)}")
                    )
            except:
                return await mystic.edit_text(
                    "**❌ 𝐓𝐡𝐢𝐬 𝐅𝐢𝐥𝐞 𝐍𝐨𝐭 𝐀 𝐕𝐚𝐥𝐢𝐝 𝐕𝐢𝐝𝐞𝐨 𝐅𝐢𝐥𝐞 𝐄𝐱𝐭𝐞𝐧𝐭𝐢𝐨𝐧❗**\n\n**𝐒𝐮𝐩𝐩𝐨𝐫𝐭𝐞𝐝 𝐅𝐨𝐫𝐦𝐚𝐭𝐬:** {0}".format(f"{' | '.join(formats)}")
                )
        if video_telegram.file_size > config.TG_VIDEO_FILESIZE_LIMIT:
            return await mystic.edit_text("**🥀 𝐕𝐢𝐝𝐞𝐨 𝐅𝐢𝐥𝐞 𝐒𝐢𝐳𝐞 𝐒𝐡𝐨𝐮𝐥𝐝 𝐁𝐞\n𝐋𝐞𝐬𝐬 𝐓𝐡𝐚𝐧 1 𝐆𝐢𝐁 ✨ ...**")
        file_path = await Telegram.get_filepath(video=video_telegram)
        if await Telegram.download(_, message, mystic, file_path):
            message_link = await Telegram.get_link(message)
            file_name = await Telegram.get_filename(video_telegram)
            dur = await Telegram.get_duration(video_telegram)
            details = {
                "title": file_name,
                "link": message_link,
                "path": file_path,
                "dur": dur,
            }
            try:
                await stream(
                    _,
                    mystic,
                    user_id,
                    details,
                    chat_id,
                    user_name,
                    message.chat.id,
                    video=True,
                    streamtype="telegram",
                    forceplay=fplay,
                )
            except Exception as e:
                ex_type = type(e).__name__
                err = (
                    e
                    if ex_type == "AssistantErr"
                    else "**🥀 𝐒𝐨𝐦𝐞 𝐄𝐱𝐜𝐞𝐩𝐭𝐢𝐨𝐧 𝐎𝐜𝐜𝐮𝐫𝐞𝐝, 𝐖𝐡𝐢𝐥𝐞 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐐𝐮𝐞𝐫𝐲.\n\n❗ 𝐄𝐱𝐜𝐞𝐩𝐭𝐢𝐨𝐧 𝐓𝐲𝐩𝐞:-** `{0}`".format(e)
                )
                return await mystic.edit_text(err)
            return await mystic.delete()
        return
    elif url:
        if await YouTube.exists(url):
            if "playlist" in url:
                try:
                    details = await YouTube.playlist(
                        url,
                        config.PLAYLIST_FETCH_LIMIT,
                        message.from_user.id,
                    )
                except Exception as e:
                    print(e)
                    return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐐𝐮𝐞𝐫𝐲 ✨...**")
                streamtype = "playlist"
                plist_type = "yt"
                if "&" in url:
                    plist_id = (url.split("=")[1]).split("&")[0]
                else:
                    plist_id = url.split("=")[1]
                img = config.PLAYLIST_IMG_URL
                cap = "**💿 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐅𝐞𝐚𝐭𝐮𝐫𝐞**\n\n🌺 𝐒𝐞𝐥𝐞𝐜𝐭 𝐓𝐡𝐞 𝐌𝐨𝐝𝐞 𝐢𝐧 𝐖𝐡𝐢𝐜𝐡 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐏𝐥𝐚𝐲 𝐖𝐡𝐨𝐥𝐞 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ✨ ...**"
            else:
                try:
                    details, track_id = await YouTube.track(url)
                except Exception as e:
                    print(e)
                    return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐐𝐮𝐞𝐫𝐲 ✨...**")
                streamtype = "youtube"
                img = details["thumb"]
                cap = "**🥀 𝐓𝐢𝐭𝐭𝐥𝐞: {0}**\n\n**⏳ 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧: {1} 𝐌𝐢𝐧𝐬**".format(
                    details["title"],
                    details["duration_min"],
                )
        elif await Spotify.valid(url):
            spotify = True
            if (
                not config.SPOTIFY_CLIENT_ID
                and not config.SPOTIFY_CLIENT_SECRET
            ):
                return await mystic.edit_text(
                    "**❌  𝐈 𝐚𝐦 𝐍𝐨𝐭 𝐀𝐛𝐥𝐞 𝐓𝐨 𝐏𝐥𝐚𝐲 𝐒𝐩𝐨𝐭𝐢𝐟𝐲 𝐐𝐮𝐞𝐫𝐢𝐞𝐬. 𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐬𝐤 𝐌𝐲 𝐎𝐰𝐧𝐞𝐫 𝐓𝐨 𝐄𝐧𝐚𝐛𝐥𝐞 𝐒𝐩𝐨𝐭𝐢𝐟𝐲.❗**"
                )
            if "track" in url:
                try:
                    details, track_id = await Spotify.track(url)
                except Exception:
                    return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐐𝐮𝐞𝐫𝐲 ✨...**")
                streamtype = "youtube"
                img = details["thumb"]
                cap = "**🥀 𝐓𝐢𝐭𝐭𝐥𝐞: {0}**\n**⏳ 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧: {1} 𝐌𝐢𝐧𝐬**".format(
                    details["title"], details["duration_min"]
                )
            elif "playlist" in url:
                try:
                    details, plist_id = await Spotify.playlist(url)
                except Exception:
                    return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐐𝐮𝐞𝐫𝐲 ✨...**")
                streamtype = "playlist"
                plist_type = "spplay"
                img = config.SPOTIFY_PLAYLIST_IMG_URL
                cap = _["play_12"].format(
                    message.from_user.first_name
                )
            elif "album" in url:
                try:
                    details, plist_id = await Spotify.album(url)
                except Exception:
                    return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐐𝐮𝐞𝐫𝐲 ✨...**")
                streamtype = "playlist"
                plist_type = "spalbum"
                img = config.SPOTIFY_ALBUM_IMG_URL
                cap = "**✅ 𝐒𝐩𝐨𝐭𝐢𝐟𝐲 𝐏𝐥𝐚𝐲 𝐌𝐨𝐝𝐞**\n\n**𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐁𝐲:- {0}**".format(
                    message.from_user.first_name
                )
            elif "artist" in url:
                try:
                    details, plist_id = await Spotify.artist(url)
                except Exception:
                    return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐐𝐮𝐞𝐫𝐲 ✨...**")
                streamtype = "playlist"
                plist_type = "spartist"
                img = config.SPOTIFY_ARTIST_IMG_URL
                cap = "**✅ 𝐒𝐩𝐨𝐭𝐢𝐟𝐲 𝐏𝐥𝐚𝐲 𝐌𝐨𝐝𝐞**\n\n**𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐁𝐲:- {0}**".format(
                    message.from_user.first_name
                )
            else:
                return await mystic.edit_text("**❌ 𝐔𝐧𝐚𝐛𝐥𝐞 𝐓𝐨 𝐏𝐥𝐚𝐲 𝐓𝐡𝐢𝐬 𝐓𝐲𝐩𝐞 𝐎𝐟 𝐒𝐩𝐨𝐭𝐢𝐟𝐲 𝐐𝐮𝐞𝐫𝐲❗\n\n✅ 𝐈 𝐂𝐚𝐧 𝐎𝐧𝐥𝐲 𝐏𝐥𝐚𝐲 𝐒𝐩𝐨𝐭𝐢𝐟𝐲 𝐓𝐫𝐚𝐜𝐤𝐬, 𝐀𝐥𝐛𝐮𝐦𝐬, 𝐀𝐫𝐭𝐢𝐬𝐭𝐬 𝐚𝐧𝐝 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭𝐬 💞 ...**")
        elif await Apple.valid(url):
            if "album" in url:
                try:
                    details, track_id = await Apple.track(url)
                except Exception:
                    return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐐𝐮𝐞𝐫𝐲 ✨...**")
                streamtype = "youtube"
                img = details["thumb"]
                cap = "**🥀 𝐓𝐢𝐭𝐭𝐥𝐞: {0}**\n**⏳𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧: {1} 𝐌𝐢𝐧𝐬**".format(
                    details["title"], details["duration_min"]
                )
            elif "playlist" in url:
                spotify = True
                try:
                    details, plist_id = await Apple.playlist(url)
                except Exception:
                    return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐐𝐮𝐞𝐫𝐲 ✨...**")
                streamtype = "playlist"
                plist_type = "apple"
                cap = "**🍎 𝐀𝐩𝐩𝐥𝐞 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭𝐬 🌷 ...**\n\n**😎 𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐁𝐲:- {0}**".format(
                    message.from_user.first_name
                )
                img = url
            else:
                return await mystic.edit_text("**❌ 𝐒𝐨𝐧𝐠 𝐍𝐨𝐭 𝐅𝐨𝐮𝐧𝐝, 𝐓𝐫𝐲 𝐀𝐧𝐨𝐭𝐡𝐞𝐫 ✨ ...**")
        elif await Resso.valid(url):
            try:
                details, track_id = await Resso.track(url)
            except Exception as e:
                return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐐𝐮𝐞𝐫𝐲 ✨...**")
            streamtype = "youtube"
            img = details["thumb"]
            cap = "**🥀 𝐓𝐢𝐭𝐭𝐥𝐞: {0}**\n**⏳ 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧: {1} 𝐌𝐢𝐧𝐬**".format(
                details["title"], details["duration_min"]
            )
        elif await SoundCloud.valid(url):
            try:
                details, track_path = await SoundCloud.download(url)
            except Exception:
                return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐐𝐮𝐞𝐫𝐲 ✨...**")
            duration_sec = details["duration_sec"]
            if duration_sec > config.DURATION_LIMIT:
                return await mystic.edit_text(
                    "**🤖 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 𝐋𝐢𝐦𝐢𝐭 𝐄𝐫𝐫𝐨𝐫❗**\n\n**𝐀𝐥𝐥𝐨𝐰𝐞𝐝 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧: **{0} 𝐌𝐢𝐧𝐮𝐭𝐞(𝐬)\n**𝐑𝐞𝐜𝐞𝐢𝐯𝐞𝐝 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧:** {1} 𝐇𝐨𝐮𝐫(𝐬)".format(
                        config.DURATION_LIMIT_MIN,
                        details["duration_min"],
                    )
                )
            try:
                await stream(
                    _,
                    mystic,
                    user_id,
                    details,
                    chat_id,
                    user_name,
                    message.chat.id,
                    streamtype="soundcloud",
                    forceplay=fplay,
                )
            except Exception as e:
                ex_type = type(e).__name__
                err = (
                    e
                    if ex_type == "AssistantErr"
                    else "**🥀 𝐒𝐨𝐦𝐞 𝐄𝐱𝐜𝐞𝐩𝐭𝐢𝐨𝐧 𝐎𝐜𝐜𝐮𝐫𝐞𝐝, 𝐖𝐡𝐢𝐥𝐞 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐐𝐮𝐞𝐫𝐲.\n\n❗ 𝐄𝐱𝐜𝐞𝐩𝐭𝐢𝐨𝐧 𝐓𝐲𝐩𝐞:-** `{0}`".format(e)
                )
                return await mystic.edit_text(err)
            return await mystic.delete()
        else:
            try:
                await Aditya.stream_call(url)
            except NoActiveGroupCall:
                await mystic.edit_text(
                    "**🥀 𝐓𝐡𝐞𝐫𝐞 𝐢𝐬 𝐚𝐧 𝐈𝐬𝐬𝐮𝐞 𝐖𝐢𝐭𝐡 𝐓𝐡𝐞 𝐁𝐨𝐭. 𝐏𝐥𝐞𝐚𝐬𝐞 𝐑𝐞𝐩𝐨𝐫𝐭 𝐈𝐭 𝐓𝐨 𝐌𝐲 𝐎𝐰𝐧𝐞𝐫 𝐀𝐧𝐝 𝐀𝐬𝐤 𝐓𝐡𝐞𝐦 𝐓𝐨 𝐂𝐡𝐞𝐜𝐤 𝐋𝐨𝐠𝐠𝐞𝐫 𝐆𝐫𝐨𝐮𝐩❗...**"
                )
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    "**🥀 𝐏𝐥𝐞𝐚𝐬𝐞 𝐓𝐮𝐫𝐧 𝐎𝐧 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭, 𝐁𝐨𝐭 𝐢𝐬 𝐍𝐨𝐭 𝐀𝐛𝐥𝐞 𝐓𝐨 𝐒𝐭𝐫𝐞𝐚𝐦 𝐔𝐫𝐥𝐬 ✨ ...**",
                )
            except Exception as e:
                return await mystic.edit_text(
                    "**🥀 𝐒𝐨𝐦𝐞 𝐄𝐱𝐜𝐞𝐩𝐭𝐢𝐨𝐧 𝐎𝐜𝐜𝐮𝐫𝐞𝐝, 𝐖𝐡𝐢𝐥𝐞 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐐𝐮𝐞𝐫𝐲.\n\n❗ 𝐄𝐱𝐜𝐞𝐩𝐭𝐢𝐨𝐧 𝐓𝐲𝐩𝐞:-** `{0}`".format(type(e).__name__)
                )
            await mystic.edit_text("**✅ 𝐕𝐚𝐥𝐢𝐝 𝐒𝐭𝐫𝐞𝐚𝐦 𝐕𝐞𝐫𝐢𝐟𝐢𝐞𝐝 💞\n\n🥀 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐋𝐢𝐧𝐤 ✨...**")
            try:
                await stream(
                    _,
                    mystic,
                    message.from_user.id,
                    url,
                    chat_id,
                    message.from_user.first_name,
                    message.chat.id,
                    video=video,
                    streamtype="index",
                    forceplay=fplay,
                )
            except Exception as e:
                ex_type = type(e).__name__
                err = (
                    e
                    if ex_type == "AssistantErr"
                    else "**🥀 𝐒𝐨𝐦𝐞 𝐄𝐱𝐜𝐞𝐩𝐭𝐢𝐨𝐧 𝐎𝐜𝐜𝐮𝐫𝐞𝐝, 𝐖𝐡𝐢𝐥𝐞 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐐𝐮𝐞𝐫𝐲.\n\n❗ 𝐄𝐱𝐜𝐞𝐩𝐭𝐢𝐨𝐧 𝐓𝐲𝐩𝐞:-** `{0}`".format(e)
                )
                return await mystic.edit_text(err)
            return await play_logs(
                message, streamtype="M3u8 or Index Link"
            )
    else:
        if len(message.command) < 2:
            buttons = botplaylist_markup(_)
            return await mystic.edit_text(
                "**🤖 𝐆𝐢𝐯𝐞 🙃 𝐒𝐨𝐦𝐞 💿 𝐐𝐮𝐞𝐫𝐲 😍\n💞 𝐓𝐨 🔊 𝐏𝐥𝐚𝐲 🥀 𝐒𝐨𝐧𝐠 🌷...**",
            )
        slider = True
        query = message.text.split(None, 1)[1]
        if "-v" in query:
            query = query.replace("-v", "")
        try:
            details, track_id = await YouTube.track(query)
        except Exception:
            return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐐𝐮𝐞𝐫𝐲 ✨...**")
        streamtype = "youtube"
    if str(playmode) == "Direct":
        if not plist_type:
            if details["duration_min"]:
                duration_sec = time_to_seconds(
                    details["duration_min"]
                )
                if duration_sec > config.DURATION_LIMIT:
                    return await mystic.edit_text(
                        "**🤖 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 𝐋𝐢𝐦𝐢𝐭 𝐄𝐫𝐫𝐨𝐫❗**\n\n**𝐀𝐥𝐥𝐨𝐰𝐞𝐝 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧: **{0} 𝐌𝐢𝐧𝐮𝐭𝐞(𝐬)\n**𝐑𝐞𝐜𝐞𝐢𝐯𝐞𝐝 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧:** {1} 𝐇𝐨𝐮𝐫(𝐬)".format(
                            config.DURATION_LIMIT_MIN,
                            details["duration_min"],
                        )
                    )
            else:
                buttons = livestream_markup(
                    _,
                    track_id,
                    user_id,
                    "v" if video else "a",
                    "c" if channel else "g",
                    "f" if fplay else "d",
                )
                return await mystic.edit_text(
                    "**✅ 𝐋𝐢𝐯𝐞 𝐒𝐭𝐫𝐞𝐚𝐦 𝐃𝐞𝐭𝐞𝐜𝐭𝐞𝐝 🌷 ...\n\n🥀 𝐒𝐲𝐬𝐭𝐞𝐦 𝐇𝐚𝐯𝐞 𝐃𝐞𝐭𝐞𝐜𝐭𝐞𝐝 𝐘𝐨𝐮𝐫\n𝐋𝐢𝐧𝐤 𝐀𝐬 𝐋𝐢𝐯𝐞 𝐒𝐭𝐫𝐞𝐚𝐦 ✨ ...\n\n💐 𝐂𝐥𝐢𝐜𝐤 𝐒𝐭𝐚𝐫𝐭 » 𝐋𝐢𝐯𝐞 𝐁𝐮𝐭𝐭𝐨𝐧❣️\n𝐓𝐨 𝐏𝐥𝐚𝐲 𝐋𝐢𝐯𝐞 𝐒𝐭𝐫𝐞𝐚𝐦 💞 ...**",
                    reply_markup=InlineKeyboardMarkup(buttons),
                )
        try:
            await stream(
                _,
                mystic,
                user_id,
                details,
                chat_id,
                user_name,
                message.chat.id,
                video=video,
                streamtype=streamtype,
                spotify=spotify,
                forceplay=fplay,
            )
        except Exception as e:
            ex_type = type(e).__name__
            err = (
                e
                if ex_type == "AssistantErr"
                else "**🥀 𝐒𝐨𝐦𝐞 𝐄𝐱𝐜𝐞𝐩𝐭𝐢𝐨𝐧 𝐎𝐜𝐜𝐮𝐫𝐞𝐝, 𝐖𝐡𝐢𝐥𝐞 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐐𝐮𝐞𝐫𝐲.\n\n❗ 𝐄𝐱𝐜𝐞𝐩𝐭𝐢𝐨𝐧 𝐓𝐲𝐩𝐞:-** `{0}`".format(e)
            )
            return await mystic.edit_text(err)
        await mystic.delete()
        return await play_logs(message, streamtype=streamtype)
    else:
        if plist_type:
            ran_hash = "".join(
                random.choices(
                    string.ascii_uppercase + string.digits, k=10
                )
            )
            lyrical[ran_hash] = plist_id
            buttons = playlist_markup(
                _,
                ran_hash,
                message.from_user.id,
                plist_type,
                "c" if channel else "g",
                "f" if fplay else "d",
            )
            await mystic.delete()
            await message.reply_photo(
                photo=img,
                caption=cap,
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            return await play_logs(
                message, streamtype=f"Playlist : {plist_type}"
            )
        else:
            if slider:
                buttons = slider_markup(
                    _,
                    track_id,
                    message.from_user.id,
                    query,
                    0,
                    "c" if channel else "g",
                    "f" if fplay else "d",
                )
                await mystic.delete()
                await message.reply_photo(
                    photo=details["thumb"],
                    caption="**🥀 𝐓𝐢𝐭𝐭𝐥𝐞: {0}**\n**⏳ 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧: {1} 𝐌𝐢𝐧𝐬**".format(
                        details["title"].title(),
                        details["duration_min"],
                    ),
                    reply_markup=InlineKeyboardMarkup(buttons),
                )
                return await play_logs(
                    message, streamtype=f"Searched on Youtube"
                )
            else:
                buttons = track_markup(
                    _,
                    track_id,
                    message.from_user.id,
                    "c" if channel else "g",
                    "f" if fplay else "d",
                )
                await mystic.delete()
                await message.reply_photo(
                    photo=img,
                    caption=cap,
                    reply_markup=InlineKeyboardMarkup(buttons),
                )
                return await play_logs(
                    message, streamtype=f"URL Searched Inline"
                )


@app.on_callback_query(filters.regex("MusicStream") & ~BANNED_USERS)
@languageCB
async def play_music(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    vidid, user_id, mode, cplay, fplay = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        try:
            return await CallbackQuery.answer(
                "🥀 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐍𝐨𝐭 𝐅𝐨𝐫 𝐘𝐨𝐮❗ 𝐒𝐞𝐚𝐫𝐜𝐡 𝐘𝐨𝐮𝐫 𝐎𝐰𝐧 𝐒𝐨𝐧𝐠 ✨ ...", show_alert=True
            )
        except:
            return
    try:
        chat_id, channel = await get_channeplayCB(
            _, cplay, CallbackQuery
        )
    except:
        return
    user_name = CallbackQuery.from_user.first_name
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        pass
    mystic = await CallbackQuery.message.reply_text(
        "**🏷𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐏𝐥𝐚𝐲 𝐌𝐨𝐝𝐞**\n\n**🔄 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 ...**\n**𝐋𝐢𝐧𝐤𝐞𝐝 𝐂𝐡𝐚𝐧𝐧𝐞𝐥:** {0}".format(channel) if channel else _["play_1"]
    )
    try:
        details, track_id = await YouTube.track(vidid, True)
    except Exception:
        return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐐𝐮𝐞𝐫𝐲 ✨...**")
    if details["duration_min"]:
        duration_sec = time_to_seconds(details["duration_min"])
        if duration_sec > config.DURATION_LIMIT:
            return await mystic.edit_text(
                "**🤖 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 𝐋𝐢𝐦𝐢𝐭 𝐄𝐫𝐫𝐨𝐫❗**\n\n**𝐀𝐥𝐥𝐨𝐰𝐞𝐝 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧: **{0} 𝐌𝐢𝐧𝐮𝐭𝐞(𝐬)\n**𝐑𝐞𝐜𝐞𝐢𝐯𝐞𝐝 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧:** {1} 𝐇𝐨𝐮𝐫(𝐬)".format(
                    config.DURATION_LIMIT_MIN, details["duration_min"]
                )
            )
    else:
        buttons = livestream_markup(
            _,
            track_id,
            CallbackQuery.from_user.id,
            mode,
            "c" if cplay == "c" else "g",
            "f" if fplay else "d",
        )
        return await mystic.edit_text(
            "**✅ 𝐋𝐢𝐯𝐞 𝐒𝐭𝐫𝐞𝐚𝐦 𝐃𝐞𝐭𝐞𝐜𝐭𝐞𝐝 🌷 ...\n\n🥀 𝐒𝐲𝐬𝐭𝐞𝐦 𝐇𝐚𝐯𝐞 𝐃𝐞𝐭𝐞𝐜𝐭𝐞𝐝 𝐘𝐨𝐮𝐫\n𝐋𝐢𝐧𝐤 𝐀𝐬 𝐋𝐢𝐯𝐞 𝐒𝐭𝐫𝐞𝐚𝐦 ✨ ...\n\n💐 𝐂𝐥𝐢𝐜𝐤 𝐒𝐭𝐚𝐫𝐭 » 𝐋𝐢𝐯𝐞 𝐁𝐮𝐭𝐭𝐨𝐧❣️\n𝐓𝐨 𝐏𝐥𝐚𝐲 𝐋𝐢𝐯𝐞 𝐒𝐭𝐫𝐞𝐚𝐦 💞 ...**",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    video = True if mode == "v" else None
    ffplay = True if fplay == "f" else None
    try:
        await stream(
            _,
            mystic,
            CallbackQuery.from_user.id,
            details,
            chat_id,
            user_name,
            CallbackQuery.message.chat.id,
            video,
            streamtype="youtube",
            forceplay=ffplay,
        )
    except Exception as e:
        ex_type = type(e).__name__
        err = (
            e
            if ex_type == "AssistantErr"
            else "**🥀 𝐒𝐨𝐦𝐞 𝐄𝐱𝐜𝐞𝐩𝐭𝐢𝐨𝐧 𝐎𝐜𝐜𝐮𝐫𝐞𝐝, 𝐖𝐡𝐢𝐥𝐞 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐐𝐮𝐞𝐫𝐲.\n\n❗ 𝐄𝐱𝐜𝐞𝐩𝐭𝐢𝐨𝐧 𝐓𝐲𝐩𝐞:-** `{0}`".format(e)
        )
        return await mystic.edit_text(err)
    return await mystic.delete()


@app.on_callback_query(
    filters.regex("AnonymousAdmin") & ~BANNED_USERS
)
async def anonymous_check(client, CallbackQuery):
    try:
        await CallbackQuery.answer(
            "🤖 𝐒𝐨𝐫𝐫𝐲, 𝐘𝐨𝐮 𝐀𝐫𝐞 𝐚𝐧 𝐀𝐧𝐨𝐧𝐲𝐦𝐨𝐮𝐬 𝐀𝐝𝐦𝐢𝐧❗",
            show_alert=True,
        )
    except:
        return


@app.on_callback_query(
    filters.regex("AdityaPlaylists") & ~BANNED_USERS
)
@languageCB
async def play_playlists_command(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    (
        videoid,
        user_id,
        ptype,
        mode,
        cplay,
        fplay,
    ) = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        try:
            return await CallbackQuery.answer(
                "🥀 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐍𝐨𝐭 𝐅𝐨𝐫 𝐘𝐨𝐮❗ 𝐒𝐞𝐚𝐫𝐜𝐡 𝐘𝐨𝐮𝐫 𝐎𝐰𝐧 𝐒𝐨𝐧𝐠 ✨ ...", show_alert=True
            )
        except:
            return
    try:
        chat_id, channel = await get_channeplayCB(
            _, cplay, CallbackQuery
        )
    except:
        return
    user_name = CallbackQuery.from_user.first_name
    await CallbackQuery.message.delete()
    try:
        await CallbackQuery.answer()
    except:
        pass
    mystic = await CallbackQuery.message.reply_text(
        "**🏷𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐏𝐥𝐚𝐲 𝐌𝐨𝐝𝐞**\n\n**🔄 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 ...**\n**𝐋𝐢𝐧𝐤𝐞𝐝 𝐂𝐡𝐚𝐧𝐧𝐞𝐥:** {0}".format(channel) if channel else "**🔄 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 ...**"
    )
    videoid = lyrical.get(videoid)
    video = True if mode == "v" else None
    ffplay = True if fplay == "f" else None
    spotify = True
    if ptype == "yt":
        spotify = False
        try:
            result = await YouTube.playlist(
                videoid,
                config.PLAYLIST_FETCH_LIMIT,
                CallbackQuery.from_user.id,
                True,
            )
        except Exception:
            return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐐𝐮𝐞𝐫𝐲 ✨...**")
    if ptype == "spplay":
        try:
            result, spotify_id = await Spotify.playlist(videoid)
        except Exception:
            return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐐𝐮𝐞𝐫𝐲 ✨...**")
    if ptype == "spalbum":
        try:
            result, spotify_id = await Spotify.album(videoid)
        except Exception:
            return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐐𝐮𝐞𝐫𝐲 ✨...**")
    if ptype == "spartist":
        try:
            result, spotify_id = await Spotify.artist(videoid)
        except Exception:
            return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐐𝐮𝐞𝐫𝐲 ✨...**")
    if ptype == "apple":
        try:
            result, apple_id = await Apple.playlist(videoid, True)
        except Exception:
            return await mystic.edit_text("**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐐𝐮𝐞𝐫𝐲 ✨...**")
    try:
        await stream(
            _,
            mystic,
            user_id,
            result,
            chat_id,
            user_name,
            CallbackQuery.message.chat.id,
            video,
            streamtype="playlist",
            spotify=spotify,
            forceplay=ffplay,
        )
    except Exception as e:
        ex_type = type(e).__name__
        err = (
            e
            if ex_type == "AssistantErr"
            else "**🥀 𝐒𝐨𝐦𝐞 𝐄𝐱𝐜𝐞𝐩𝐭𝐢𝐨𝐧 𝐎𝐜𝐜𝐮𝐫𝐞𝐝, 𝐖𝐡𝐢𝐥𝐞 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐐𝐮𝐞𝐫𝐲.\n\n❗ 𝐄𝐱𝐜𝐞𝐩𝐭𝐢𝐨𝐧 𝐓𝐲𝐩𝐞:-** `{0}`".format(e)
        )
        return await mystic.edit_text(err)
    return await mystic.delete()


@app.on_callback_query(filters.regex("slider") & ~BANNED_USERS)
@languageCB
async def slider_queries(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    (
        what,
        rtype,
        query,
        user_id,
        cplay,
        fplay,
    ) = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        try:
            return await CallbackQuery.answer(
                "🥀 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐍𝐨𝐭 𝐅𝐨𝐫 𝐘𝐨𝐮❗ 𝐒𝐞𝐚𝐫𝐜𝐡 𝐘𝐨𝐮𝐫 𝐎𝐰𝐧 𝐒𝐨𝐧𝐠 ✨ ...", show_alert=True
            )
        except:
            return
    what = str(what)
    rtype = int(rtype)
    if what == "F":
        if rtype == 9:
            query_type = 0
        else:
            query_type = int(rtype + 1)
        try:
            await CallbackQuery.answer("🔃 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐍𝐞𝐱𝐭 𝐑𝐞𝐬𝐮𝐥𝐭 🌷 ...")
        except:
            pass
        title, duration_min, thumbnail, vidid = await YouTube.slider(
            query, query_type
        )
        buttons = slider_markup(
            _, vidid, user_id, query, query_type, cplay, fplay
        )
        med = InputMediaPhoto(
            media=thumbnail,
            caption="**🥀 𝐓𝐢𝐭𝐭𝐥𝐞: {0}**\n**⏳ 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧: {1} 𝐌𝐢𝐧𝐬**".format(
                title.title(),
                duration_min,
            ),
        )
        return await CallbackQuery.edit_message_media(
            media=med, reply_markup=InlineKeyboardMarkup(buttons)
        )
    if what == "B":
        if rtype == 0:
            query_type = 9
        else:
            query_type = int(rtype - 1)
        try:
            await CallbackQuery.answer("🔃 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐍𝐞𝐱𝐭 𝐑𝐞𝐬𝐮𝐥𝐭 🌷 ...")
        except:
            pass
        title, duration_min, thumbnail, vidid = await YouTube.slider(
            query, query_type
        )
        buttons = slider_markup(
            _, vidid, user_id, query, query_type, cplay, fplay
        )
        med = InputMediaPhoto(
            media=thumbnail,
            caption="**🥀 𝐓𝐢𝐭𝐭𝐥𝐞: {0}**\n**⏳ 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧: {1} 𝐌𝐢𝐧𝐬**".format(
                title.title(),
                duration_min,
            ),
        )
        return await CallbackQuery.edit_message_media(
            media=med, reply_markup=InlineKeyboardMarkup(buttons)
        )
