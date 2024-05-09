#Coded by @Its_Tartaglia_Childe

from pyrogram import Client 
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text = f"<b>ᴍʏ ꜱᴇɴꜱᴇɪ ~ @obitoXbroken </b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("​ᴄʟᴏꜱᴇ​", callback_data="close"),
                        InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text = f"<b>ᴍʏ ꜱᴇɴꜱᴇɪ ~ <a @obitoXbroken>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\nᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ ~ <a href=https://t.me/AnimeArena01>Anime Arena</a>\nOngoing Channel ~ <a href=https://t.me/OngoingArena01>Ongoing Arena</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("​ᴄʟᴏꜱᴇ​", callback_data="close"),
                        InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
