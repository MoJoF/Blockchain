from Data.Block import Block
from Data.Profile import Profile
from config import TOKEN
from Messages import Messages, MessagesInline
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


@tg.callback_query_handler(func=lambda call: True)
def callback(call):
	for i in MessagesInline:
		for key, value in i.items():
			if call.data == key:
				tg.send_message(call.message.chat.id, value, parse_mode="HTML", reply_markup=i['kb'])


tg.infinity_polling()