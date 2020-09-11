from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

start_menu = ReplyKeyboardMarkup(True, True)
start_menu.row("Профиль 👤", "Мои транзакции 🧾")

hide = ReplyKeyboardRemove()