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
            text = f"<b>ᴍʏ ꜱᴇɴꜱᴇɪ ~ @UCSasuke01 </b>",
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
            text = f"<b>ᴍʏ ꜱᴇɴꜱᴇɪ ~ <a href=https://t.me/UCSasuke01>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\nᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ ~ <a href=https://t.me/AnimeArena01>ᴀɴɪᴍᴇ ᴀʀᴇɴᴀ</a>\nᴏɴɢᴏɪɴɢ ᴄʜᴀɴɴᴇʟ ~ <a href=https://t.me/OngoingArena01>ᴏɴɢᴏɪɴɢ ᴀʀᴇɴᴀ</a></b>",
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
