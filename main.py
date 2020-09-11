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


@tg.message_handler(content_types=['text'])
def text_answer(message):
	for i in Messages:
		for key, value in i.items():
			if message.text == key:
				tg.send_message(message.chat.id, value, parse_mode="HTML", reply_markup=i['kb'])


tg.infinity_polling()