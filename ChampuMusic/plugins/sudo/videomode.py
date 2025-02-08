from pyrogram import filters
from pyrogram.types import Message
from config import OWNER_ID
import config
from strings import get_command
from ChampuMusic import app
from ChampuMusic.misc import SUDOERS, SPECIAL_ID
from ChampuMusic.utils.database import add_off, add_on
from ChampuMusic.utils.decorators.language import language

# Commands
VIDEOMODE_COMMAND = get_command("VIDEOMODE_COMMAND")


@app.on_message(filters.command(VIDEOMODE_COMMAND) & (filters.user(OWNER_ID) | filters.user(SPECIAL_ID)) & SUDOERS)
@language
async def videoloaymode(client, message: Message, _):
    usage = _["vidmode_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "download":
        await add_on(config.YTDOWNLOADER)
        await message.reply_text(_["vidmode_2"])
    elif state == "m3u8":
        await add_off(config.YTDOWNLOADER)
        await message.reply_text(_["vidmode_3"])
    else:
        await message.reply_text(usage)
