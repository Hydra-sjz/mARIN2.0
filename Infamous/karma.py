# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/107434c32dae37f05712e.jpg",
    "https://telegra.ph/file/8c8c6c881e48fcae3bf59.jpg",
    "https://telegra.ph/file/48cf12ee447b359320a21.jpg",
    "https://telegra.ph/file/48cf12ee447b359320a21.jpg",
    "https://telegra.ph/file/651d1d6b921e77b754598.jpg",
    "https://telegra.ph/file/95058a3da1167aad02846.jpg",
    "https://telegra.ph/file/67e4016560498beaadbc6.jpg",
    "https://telegra.ph/file/95058a3da1167aad02846.jpg",
    "https://telegra.ph/file/9a459f18449d9f2e9d8dd.jpg",
]

HEY_IMG = "https://telegra.ph/file/67e4016560498beaadbc6.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph/file/d841c02b6607e06bf4105.mp4",
    "https://telegra.ph/file/d841c02b6607e06bf4105.mp4",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "✨ *ᴋᴏɴɪᴄʜɪᴡᴀ, ɪ ᴀᴍ Mᴀʀɪɴ, ʜᴀᴊɪᴍᴇᴍᴀꜱʜɪᴛ. ᴀɴ ᴀɴɪᴍᴇ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="HELP", callback_data="extra_command_handler"),
    ],
    [
        InlineKeyboardButton(text="DETAILS", callback_data="Miko_"),
        InlineKeyboardButton(text="SOURCE", callback_data="git_source"),
    ],
    [
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/Hydra_Updates"),
        ib(text="SUPPORT", url="https://t.me/hydraXsupport"),
    ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *Yae-Miko* 🫧 [ㅤ](https://telegra.ph/file/b05535884267a19ee5c93.jpg)

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
