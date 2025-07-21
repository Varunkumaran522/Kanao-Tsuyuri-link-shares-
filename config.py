 
import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

# Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8060792535:AAHczThfSkKQkjfXuOxI00r5pVn9EaeznxQ")
APP_ID = int(os.environ.get("APP_ID", "26069929"))
API_HASH = os.environ.get("API_HASH", "b0551dd4dd9e81b47fe6aa92173aff24")

# Main
OWNER_ID = int(os.environ.get("OWNER_ID", "6586630448"))
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sora:sora@sora.vfmsflj.mongodb.net/?retryWrites=true&w=majority&appName=sora")
DB_NAME = os.environ.get("DB_NAME", "sora")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()] # dont change anything 
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʜɪ... ɪ ʜᴏᴘᴇ ɪ'ᴍ ɴᴏᴛ ʙᴏᴛʜᴇʀɪɴɢ ʏᴏᴜ.\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ...\nᴍᴀʏʙᴇ ɪᴛ ᴡᴀꜱ ᴍᴇᴀɴᴛ ᴛᴏ ʙᴇ 🦋\n\n‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ <a href='https://t.me/+9y7dY1ir2nllNjI1'>ᴏʙʟɪᴠɪᴏɴ–⁶ ᴄᴏʀᴇ</a> — ɪ’ʟʟ ʙᴇ ᴡᴀᴛᴄʜɪɴɢ ꜰʀᴏᴍ ᴀꜰᴀʀ… ꜱᴛᴀʏ ꜱᴀꜰᴇ</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

# Start pic
START_PIC_FILE_ID = "https://files.catbox.moe/4lg8qf.jpg"
START_IMG = "https://files.catbox.moe/kk6lfr.jpg"
# Messages
START_MSG = os.environ.get("START_MESSAGE", "<b>H-Hello... 🌸\n\nWelcome to this advanced link-sharing bot. I hope it will be helpful to you... It lets you share links quietly and safely... and protects your channel from copyright issues.\n\n<blockquote>‣ Maintained by: <a href='https://t.me/+9y7dY1ir2nllNjI1'>Oblivion–⁶ Core</a></blockquote>\n\n...Please use it carefully. 💮</b>")
HELP = os.environ.get("HELP_MESSAGE", "<b><blockquote expandable>» Creator: <a href='https://t.me/Momo_Ayase_bot'>ꜱᴇɴᴘᴀɪꜱʜɪꜰᴛ</a>\n» Our Community: <a href='https://t.me/+9y7dY1ir2nllNjI1'>ᴏʙʟɪᴠɪᴏɴ–⁶ ᴄᴏʀᴇ</a>\n»  ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/+fFiQg-aN1XU0YWZl'>ᴇᴄʜᴏɴɪᴍᴇ</a>\n» Developer: <a href='https://t.me/Momo_Ayase_bot'>ꜱᴇɴᴘᴀɪꜱʜɪꜰᴛ</a></b>")
ABOUT = os.environ.get("ABOUT_MESSAGE", "<b>U-Um...\n\nThis bot... it was made by <a href='https://t.me/Momo_Ayase_bot'>SenpaiShift</a>... to help share your Telegram channel links safely. It uses temporary invite links... so your channels stay protected from copyright problems.\n\nI-I hope it’s useful... 🌸</b>")

ABOUT_TXT = """<b>›› ᴄʀᴇᴀᴛᴏʀ: <a href='https://t.me/Momo_Ayase_bot'>ꜱᴇɴᴘᴀɪꜱʜɪꜰᴛ</a>
<blockquote expandable>›› ꜰᴏᴜɴᴅᴇʀ ᴏғ: <a href='https://t.me/AniHorizon'>🌙 ᴀɴɪ𝐇𝐨𝐫𝐢𝐳𝐨𝐧 🍂</a>
›› ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/+fFiQg-aN1XU0YWZl'>ᴇᴄʜᴏɴɪᴍᴇ</a>
›› sᴇʀɪᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/+ywy8pV0RVok0MzM1'>ᴡᴇʙsᴇʀɪᴇs ʜᴏʀɪᴢᴏɴ</a>
›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/'>Pʏᴛʜᴏɴ 3</a>
›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a>
›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/Momo_Ayase_bot'>ꜱᴇɴᴘᴀɪꜱʜɪꜰᴛ</a></b></blockquote>"""

CHANNELS_TXT = """<b>››  ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/+fFiQg-aN1XU0YWZl'>ᴇᴄʜᴏɴɪᴍᴇ</a>
<blockquote expandable>
›› ᴡᴇʙsᴇʀɪᴇs: <a href='https://t.me/+ywy8pV0RVok0MzM1'>ᴡᴇʙsᴇʀɪᴇs ʜᴏʀɪᴢᴏɴ</a>
›› ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟs: <a href='https://t.me/Hentai_HwaX'>ᵀᵉᵐᵖᵗᵃᵗᶦᵒⁿ</a>
›› ᴍᴀɴʜᴡᴀ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/+XHNsgzRxQOY5ZDk1'>ˢᴵᴺᶠᵁᴸ ᴾᴬᴺᴱᴸˢ
</a>
›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/+9y7dY1ir2nllNjI1'>ᴏʙʟɪᴠɪᴏɴ–⁶ ᴄᴏʀᴇ</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/Momo_Ayase_bot'>ꜱᴇɴᴘᴀɪꜱʜɪꜰᴛ</a></b></blockquote>""" 
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🌸 I-I'm sorry... but you're not my master. Please don't speak to me like that... I’ll be going now. 🌸"

# Logging
LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1002832498704")) # Channel where user links are stored
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "6586630448").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Admin == OWNER_ID
ADMINS.append(OWNER_ID)
ADMINS.append(6586630448)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
