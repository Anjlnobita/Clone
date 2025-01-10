import math
from typing import Union
from pyrogram.types import InlineKeyboardButton

from RISHUMUSIC.utils.formatters import time_to_seconds

from RISHUMUSIC import app


def track_markup(_, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐑ᴇᴘʟᴀʏ ❍", callback_data=f"ADMIN Replay|{chat_id}"
            ),
            InlineKeyboardButton(text="❍ 𝐄ɴᴅ ❍", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐌ᴏʀᴇ ❍",
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
        ],
    ]

    return buttons


def stream_markup_timer(_,  chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 40:
        bar = "◉——————————"
    elif 10 < umm < 20:
        bar = "—◉—————————"
    elif 20 < umm < 30:
        bar = "——◉————————"
    elif 30 <= umm < 40:
        bar = "———◉———————"
    elif 40 <= umm < 50:
        bar = "————◉——————"
    elif 50 <= umm < 60:
        bar = "——————◉————"
    elif 50 <= umm < 70:
        bar = "———————◉———"
    else:
        bar = "——————————◉"

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐏ᴀᴜ𝐬ᴇ ❍",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(text="❍ 𝐒ᴛᴏᴘ ❍", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(
                text="❍ 𝐒ᴋɪᴘ ❍", callback_data=f"ADMIN Skip|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐑ᴇ𝐬ᴜᴍᴇ ❍", callback_data=f"ADMIN Resume|{chat_id}"
            ),
            InlineKeyboardButton(
                text="❍ 𝐑ᴇᴘʟᴀʏ ❍", callback_data=f"ADMIN Replay|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐅ᴇᴀᴛᴜʀᴇ ❍",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
        ],
    ]

    return buttons



def stream_markup(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "❖◈◈◈◈◈◈◈◈◈"
    elif 10 < umm < 20:
        bar = "◈❖◈◈◈◈◈◈◈◈"
    elif 20 <= umm < 30:
        bar = "◈◈❖◈◈◈◈◈◈◈"
    elif 30 <= umm < 40:
        bar = "◈◈◈❖◈◈◈◈◈◈"
    elif 40 <= umm < 50:
        bar = "◈◈◈◈❖◈◈◈◈◈"
    elif 50 <= umm < 60:
        bar = "◈◈◈◈◈❖◈◈◈◈"
    elif 60 <= umm < 70:
        bar = "◈◈◈◈◈◈❖◈◈◈"
    elif 70 <= umm < 80:
        bar = "◈◈◈◈◈◈◈❖◈◈"
    elif 80 <= umm < 95:
        bar = "◈◈◈◈◈◈◈◈❖◈"
    else:
        bar = "◈◈◈◈◈◈◈◈◈❖"
    buttons = [   
            [
                   InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer"
                )
         ],
         [
            InlineKeyboardButton(text="ᴘᴀᴜsᴇ", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="ʀᴇsᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="sᴋɪᴘ", callback_data=f"ADMIN Skip|{chat_id}")
        ],
        [
            InlineKeyboardButton(text="sᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="ʀᴇᴘʟᴀʏ", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons
        


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"RISHUPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"RISHUPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons


## Telegram Markup


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="❍ 𝐍ᴇ𝐱ᴛ ❍",
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
            InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


## Queue Markup


def queue_markup(_, videoid, chat_id):

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐏ᴀᴜ𝐬ᴇ ❍",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(text="❍ 𝐒ᴛᴏᴘ ❍", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(
                text="❍ 𝐒ᴋɪᴘ ❍", callback_data=f"ADMIN Skip|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐑ᴇ𝐬ᴜᴍᴇ ❍", callback_data=f"ADMIN Resume|{chat_id}"
            ),
            InlineKeyboardButton(
                text="❍ 𝐑ᴇᴘʟᴀʏ ❍", callback_data=f"ADMIN Replay|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐌ᴏʀᴇ ❍",
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
        ],
    ]

    return buttons


def stream_markup2(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def stream_markup_timer2(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 40:
        bar = "◉——————————"
    elif 10 < umm < 20:
        bar = "—◉—————————"
    elif 20 < umm < 30:
        bar = "——◉————————"
    elif 30 <= umm < 40:
        bar = "———◉———————"
    elif 40 <= umm < 50:
        bar = "————◉——————"
    elif 50 <= umm < 60:
        bar = "——————◉————"
    elif 50 <= umm < 70:
        bar = "———————◉———"
    else:
        bar = "——————————◉"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def panel_markup_1(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐒ᴜғғʟᴇ ❍",
                callback_data=f"ADMIN Shuffle|{chat_id}",
            ),
            InlineKeyboardButton(text="❍ 𝐋ᴏᴏᴘ ❍", callback_data=f"ADMIN Loop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="10 𝐒ᴇᴄ ❍",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            InlineKeyboardButton(
                text="10 𝐒ᴇᴄ ❍",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐇ᴏᴍᴇ ❍",
                callback_data=f"Pages Back|2|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="❍ 𝐍ᴇ𝐱ᴛ ❍",
                callback_data=f"Pages Forw|2|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons


def panel_markup_2(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🕒 0.5x",
                callback_data=f"SpeedUP {chat_id}|0.5",
            ),
            InlineKeyboardButton(
                text="🕓 0.75x",
                callback_data=f"SpeedUP {chat_id}|0.75",
            ),
            InlineKeyboardButton(
                text="🕤 1.0x",
                callback_data=f"SpeedUP {chat_id}|1.0",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🕤 1.5x",
                callback_data=f"SpeedUP {chat_id}|1.5",
            ),
            InlineKeyboardButton(
                text="🕛 2.0x",
                callback_data=f"SpeedUP {chat_id}|2.0",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐁ᴀᴄᴋ ❍",
                callback_data=f"Pages Back|1|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons


def panel_markup_5(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="❍ 𝐏ᴀᴜ𝐬ᴇ ❍", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="❍ 𝐒ᴛᴏᴘ ❍", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="❍ 𝐒ᴋɪᴘ ❍", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐑ᴇ𝐬ᴜᴍᴇ ❍", callback_data=f"ADMIN Resume|{chat_id}"
            ),
            InlineKeyboardButton(
                text="❍ 𝐑ᴇᴘʟᴀʏ ❍", callback_data=f"ADMIN Replay|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐇ᴏᴍᴇ ❍",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="❍ 𝐍ᴇ𝐱ᴛ ❍",
                callback_data=f"Pages Forw|1|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons


def panel_markup_3(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🕒 0.5x",
                callback_data=f"SpeedUP {chat_id}|0.5",
            ),
            InlineKeyboardButton(
                text="🕓 0.75x",
                callback_data=f"SpeedUP {chat_id}|0.75",
            ),
            InlineKeyboardButton(
                text="🕤 1.0x",
                callback_data=f"SpeedUP {chat_id}|1.0",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🕤 1.5x",
                callback_data=f"SpeedUP {chat_id}|1.5",
            ),
            InlineKeyboardButton(
                text="🕛 2.0x",
                callback_data=f"SpeedUP {chat_id}|2.0",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐁ᴀᴄᴋ ❍",
                callback_data=f"Pages Back|2|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons


def panel_markup_4(_, vidid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 40:
        bar = "◉——————————"
    elif 10 < umm < 20:
        bar = "—◉—————————"
    elif 20 < umm < 30:
        bar = "——◉————————"
    elif 30 <= umm < 40:
        bar = "———◉———————"
    elif 40 <= umm < 50:
        bar = "————◉——————"
    elif 50 <= umm < 60:
        bar = "——————◉————"
    elif 50 <= umm < 70:
        bar = "———————◉———"
    else:
        bar = "——————————◉"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐏ᴀᴜ𝐬ᴇ ❍",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(
                text="❍ 𝐒ᴛᴏᴘ ❍", callback_data=f"ADMIN Stop|{chat_id}"
            ),
            InlineKeyboardButton(
                text="❍ 𝐒ᴋɪᴘ ❍", callback_data=f"ADMIN Skip|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐑ᴇ𝐬ᴜᴍᴇ ❍", callback_data=f"ADMIN Resume|{chat_id}"
            ),
            InlineKeyboardButton(
                text="❍ 𝐑ᴇᴘʟᴀʏ ❍", callback_data=f"ADMIN Replay|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐇ᴏᴍᴇ ❍",
                callback_data=f"MainMarkup {vidid}|{chat_id}",
            ),
        ],
    ]

    return buttons


def panel_markup_clone(_, vidid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐔ᴘᴅᴀᴛᴇ ❍", url=f"https://t.me/UR_RISHU_143"
            ),
            InlineKeyboardButton(
                text="❍ 𝐒ᴜᴘᴘᴏʀᴛ ❍", url=f"https://t.me/Ur_support07"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐏ʟᴀʏʟɪ𝐬ᴛ ❍", callback_data=f"shukla_playlist {vidid}"
            ),
        ],
    ]

    return buttons