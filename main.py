from Data.Block import Block
from Data.Profile import Profile
from config import TOKEN
from Messages import Messages
import random
import telebot

tg = telebot.TeleBot(TOKEN)


@tg.message_handler(commands=['start'])
def start_message(message):
	tg.send_message(message.chat.id, Messages[0]['start_message'], parse_mode="HTML", reply_markup=Messages[0]['kb'])


tg.infinity_polling()