# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 

from typing import Union

from pyrogram.types import InlineKeyboardButton


def setting_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔊 𝐀𝐮𝐝 𝐐𝐮𝐚𝐥𝐢𝐭𝐲", callback_data="AQ"
            ),
            InlineKeyboardButton(
                text="🎥 𝐕𝐢𝐝 𝐐𝐮𝐚𝐥𝐢𝐭𝐲", callback_data="VQ"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🎩 𝐀𝐮𝐭𝐡 𝐔𝐬𝐞𝐫𝐬", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="🤖 𝐁𝐨𝐭 𝐎𝐰𝐧𝐞𝐫", url=f"https://t.me/Bikashhalder"
            ),
        ],
        [
            InlineKeyboardButton(
                text="▶️ 𝐏𝐥𝐚𝐲 𝐌𝐨𝐝𝐞", callback_data="PM"
            ),
            InlineKeyboardButton(
                text="🔥𝐂𝐥𝐞𝐚𝐧 𝐌𝐨𝐝𝐞", callback_data="CM"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 ❌", callback_data="close"
            ),
        ],
    ]
    return buttons


def audio_quality_markup(
    _,
    low: Union[bool, str] = None,
    medium: Union[bool, str] = None,
    high: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="{0} 𝐋𝐨𝐰 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐀𝐮𝐝𝐢𝐨".format("✅")
                if low == True
                else "{0} 𝐋𝐨𝐰 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐀𝐮𝐝𝐢𝐨".format(""),
                callback_data="LQA",
            )
        ],
        [
            InlineKeyboardButton(
                text="{0} 𝐌𝐞𝐝𝐢𝐮𝐦 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐀𝐮𝐝𝐢𝐨".format("✅")
                if medium == True
                else "{0} 𝐌𝐞𝐝𝐢𝐮𝐦 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐀𝐮𝐝𝐢𝐨".format(""),
                callback_data="MQA",
            )
        ],
        [
            InlineKeyboardButton(
                text="{0} 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐀𝐮𝐝𝐢𝐨".format("✅")
                if high == True
                else "{0} 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐀𝐮𝐝𝐢𝐨".format(""),
                callback_data="HQA",
            )
        ],
        [
            InlineKeyboardButton(
                text="⬅️ 𝐁𝐚𝐜𝐤",
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞", callback_data="close"
            ),
        ],
    ]
    return buttons


def video_quality_markup(
    _,
    low: Union[bool, str] = None,
    medium: Union[bool, str] = None,
    high: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="{0} 𝐋𝐨𝐰 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐕𝐢𝐝𝐞𝐨".format("✅")
                if low == True
                else "{0} 𝐋𝐨𝐰 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐕𝐢𝐝𝐞𝐨".format(""),
                callback_data="LQV",
            )
        ],
        [
            InlineKeyboardButton(
                text="{0} 𝐌𝐞𝐝𝐢𝐮𝐦 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐕𝐢𝐝𝐞𝐨".format("✅")
                if medium == True
                else "{0} 𝐌𝐞𝐝𝐢𝐮𝐦 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐕𝐢𝐝𝐞𝐨".format(""),
                callback_data="MQV",
            )
        ],
        [
            InlineKeyboardButton(
                text="{0} 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐕𝐢𝐝𝐞𝐨".format("✅")
                if high == True
                else "{0} 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐕𝐢𝐝𝐞𝐨".format(""),
                callback_data="HQV",
            )
        ],
        [
            InlineKeyboardButton(
                text="⬅️ 𝐁𝐚𝐜𝐤",
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞", callback_data="close"
            ),
        ],
    ]
    return buttons


def cleanmode_settings_markup(
    _,
    status: Union[bool, str] = None,
    dels: Union[bool, str] = None,
    sug: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔥𝐂𝐥𝐞𝐚𝐧 𝐌𝐨𝐝𝐞", callback_data="CMANSWER"
            ),
            InlineKeyboardButton(
                text="✅ 𝐄𝐧𝐚𝐛𝐥𝐞𝐝" if status == True else "❌ 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝",
                callback_data="CLEANMODE",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🗑 𝐂𝐦𝐝 𝐂𝐥𝐞𝐚𝐧", callback_data="COMMANDANSWER"
            ),
            InlineKeyboardButton(
                text="✅ 𝐄𝐧𝐚𝐛𝐥𝐞𝐝" if dels == True else "❌ 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝",
                callback_data="COMMANDELMODE",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🧑‍🚀 𝐒𝐮𝐠𝐠 𝐌𝐨𝐝𝐞", callback_data="SUGGANSWER"
            ),
            InlineKeyboardButton(
                text="✅ 𝐄𝐧𝐚𝐛𝐥𝐞𝐝" if sug == True else "❌ 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝",
                callback_data="SUGGESTIONCHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ 𝐁𝐚𝐜𝐤",
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞", callback_data="close"
            ),
        ],
    ]
    return buttons


def auth_users_markup(_, status: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎩 𝐀𝐮𝐭𝐡 𝐔𝐬𝐞𝐫𝐬", callback_data="AUTHANSWER"
            ),
            InlineKeyboardButton(
                text="👤 𝐀𝐝𝐦𝐢𝐧𝐬" if status == True else "👥 𝐄𝐯𝐞𝐫𝐲𝐨𝐧𝐞",
                callback_data="AUTH",
            ),
        ],
        [
            InlineKeyboardButton(
                text="📋 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 𝐔𝐬𝐞𝐫𝐬 𝐋𝐢𝐬𝐭𝐬", callback_data="AUTHLIST"
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ 𝐁𝐚𝐜𝐤",
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞", callback_data="close"
            ),
        ],
    ]
    return buttons


def playmode_users_markup(
    _,
    Direct: Union[bool, str] = None,
    Group: Union[bool, str] = None,
    Playtype: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔎 𝐒𝐞𝐚𝐫𝐜𝐡 𝐌𝐨𝐝𝐞", callback_data="SEARCHANSWER"
            ),
            InlineKeyboardButton(
                text="✅ 𝐃𝐢𝐫𝐞𝐜𝐭" if Direct == True else "✅ 𝐈𝐧𝐥𝐢𝐧𝐞",
                callback_data="MODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text="👨‍⚖️ 𝐀𝐝𝐦𝐢𝐧 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", callback_data="AUTHANSWER"
            ),
            InlineKeyboardButton(
                text="👤 𝐀𝐝𝐦𝐢𝐧𝐬" if Group == True else "👥 𝐄𝐯𝐞𝐫𝐲𝐨𝐧𝐞",
                callback_data="CHANNELMODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🫂 𝐏𝐥𝐚𝐲 𝐓𝐲𝐩𝐞", callback_data="PLAYTYPEANSWER"
            ),
            InlineKeyboardButton(
                text="👤 𝐀𝐝𝐦𝐢𝐧𝐬"
                if Playtype == True
                else "👥 𝐄𝐯𝐞𝐫𝐲𝐨𝐧𝐞",
                callback_data="PLAYTYPECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ 𝐁𝐚𝐜𝐤",
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞", callback_data="close"
            ),
        ],
    ]
    return buttons




# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 