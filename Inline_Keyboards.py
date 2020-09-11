from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


profile_kb = InlineKeyboardMarkup()
send = InlineKeyboardButton("Отправить 💵", callback_data="send")
profile_kb.row(send)