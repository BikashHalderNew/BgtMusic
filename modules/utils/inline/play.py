# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 

import random
from modules.config import SUPPORT_GROUP
from modules.config import SUPPORT_CHANNEL
from pyrogram.types import InlineKeyboardButton



def stream_markup_timer(_, videoid, chat_id, played, dur):
    buttons = [
        [
            InlineKeyboardButton(
                        "💥 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩 💞", url=f"{SUPPORT_GROUP}"
            )
        ],
        [           
            InlineKeyboardButton(
                text="💥 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💞", url=f"{SUPPORT_CHANNEL}"
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 📱", url=f"https://youtube.com/@BikashGadgetsTech"
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    buttons = [
        [
            InlineKeyboardButton(
                        "💥 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩 💞", url=f"{SUPPORT_GROUP}"
            )
        ],
         [           
            InlineKeyboardButton(
                text="💥 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💞", url=f"{SUPPORT_CHANNEL}"
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 📱", url=f"https://youtube.com/@BikashGadgetsTech"
            )
        ],
    ]
    return buttons


## Inline without Timer Bar


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                        "💥 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩 💞", url=f"{SUPPORT_GROUP}"
            )
        ],
         [           
            InlineKeyboardButton(
                text="💥 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💞", url=f"{SUPPORT_CHANNEL}"
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 📱", url=f"https://youtube.com/@BikashGadgetsTech"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                        "💥 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩 💞", url=f"{SUPPORT_GROUP}"
            )
        ],
         [           
            InlineKeyboardButton(
                text="💥 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💞", url=f"{SUPPORT_CHANNEL}"
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 📱", url=f"https://youtube.com/@BikashGadgetsTech"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔊 𝐏𝐥𝐚𝐲 𝐀𝐮𝐝𝐢𝐨",
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="𝐏𝐥𝐚𝐲 𝐕𝐢𝐝𝐞𝐨 📺",
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔊 𝐏𝐥𝐚𝐲 𝐀𝐮𝐝𝐢𝐨",
                callback_data=f"BikashPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="𝐏𝐥𝐚𝐲 𝐕𝐢𝐝𝐞𝐨 📺",
                callback_data=f"BikashPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
        [           
            InlineKeyboardButton(
                text="💥 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💞", url=f"{SUPPORT_CHANNEL}"
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 📱", url=f"https://youtube.com/@BikashGadgetsTech"
            )
        ],
    ]
    return buttons


## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text="🖥️ 𝐒𝐭𝐚𝐫𝐭 𝐋𝐢𝐯𝐞 𝐒𝐭𝐫𝐞𝐚𝐦 🖥️",
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            )
        ],
        [
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
         [           
            InlineKeyboardButton(
                text="💥 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💞", url=f"{SUPPORT_CHANNEL}"
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 📱", url=f"https://youtube.com/@BikashGadgetsTech"
            )
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text="🔊 𝐏𝐥𝐚𝐲 𝐀𝐮𝐝𝐢𝐨",
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="𝐏𝐥𝐚𝐲 𝐕𝐢𝐝𝐞𝐨 📺",
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❮",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌",
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
         [           
            InlineKeyboardButton(
                text="💥 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💞", url=f"{SUPPORT_CHANNEL}"
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 📱", url=f"https://youtube.com/@BikashGadgetsTech"
            )
        ],
    ]
    return buttons


## Cpanel Markup


def panel_markup_1(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="⏸ 𝐏𝐚𝐮𝐬𝐞", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▶️ 𝐑𝐞𝐬𝐮𝐦𝐞",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⏯ 𝐒𝐤𝐢𝐩", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="⏹ 𝐒𝐭𝐨𝐩", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◀️",
                callback_data=f"Pages Back|0|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🔙 𝐁𝐚𝐜𝐤 🔙",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="▶️",
                callback_data=f"Pages Forw|0|{videoid}|{chat_id}",
            ),
        ],
         [           
            InlineKeyboardButton(
                text="💥 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💞", url=f"{SUPPORT_CHANNEL}"
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 📱", url=f"https://youtube.com/@BikashGadgetsTech"
            )
        ],
    ]
    return buttons


def panel_markup_2(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔇 𝐌𝐮𝐭𝐞", callback_data=f"ADMIN Mute|{chat_id}"
            ),
            InlineKeyboardButton(
                text="🔊 𝐔𝐧𝐦𝐮𝐭𝐞",
                callback_data=f"ADMIN Unmute|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🔀 𝐒𝐡𝐮𝐟𝐟𝐥𝐞",
                callback_data=f"ADMIN Shuffle|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🔁 𝐋𝐨𝐨𝐩", callback_data=f"ADMIN Loop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◀️",
                callback_data=f"Pages Back|1|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🔙 𝐁𝐚𝐜𝐤 🔙",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="▶️",
                callback_data=f"Pages Forw|1|{videoid}|{chat_id}",
            ),
        ],
         [           
            InlineKeyboardButton(
                text="💥 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💞", url=f"{SUPPORT_CHANNEL}"
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 📱", url=f"https://youtube.com/@BikashGadgetsTech"
            )
        ],
    ]
    return buttons


def panel_markup_3(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="⏮ 𝟏𝟎 𝐒𝐞𝐜𝐨𝐧𝐝𝐬",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏭ 𝟏𝟎 𝐒𝐞𝐜𝐨𝐧𝐝𝐬",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⏮ 𝟑𝟎 𝐒𝐞𝐜𝐨𝐧𝐝𝐬",
                callback_data=f"ADMIN 3|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏭ 𝟑𝟎 𝐒𝐞𝐜𝐨𝐧𝐝𝐬",
                callback_data=f"ADMIN 4|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◀️",
                callback_data=f"Pages Back|2|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🔙 𝐁𝐚𝐜𝐤 🔙",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="▶️",
                callback_data=f"Pages Forw|2|{videoid}|{chat_id}",
            ),
        ],
         [           
            InlineKeyboardButton(
                text="💥 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💞", url=f"{SUPPORT_CHANNEL}"
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 📱", url=f"https://youtube.com/@BikashGadgetsTech"
            )
        ],
    ]
    return buttons



# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 
