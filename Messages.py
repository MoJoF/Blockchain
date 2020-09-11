from Data.Profile import Profile
from telebot.types import ReplyKeyboardMarkup
from Reply_Keyboards import *
from Inline_Keyboards import *

profile = Profile()
count = profile.count
adress = profile.adress_generate()

Messages = [
{
	# текст сообщения : ответ на сообщение
	"start_message": f"""Приветствую тебя. Добро пожаловать в <b>Levendauer</b>
	""",
	"kb": start_menu
},
{
	"Профиль 👤": f"""На вашем счете: <b><i>{count} 💵</i></b>\nВаш адрес: <b>{adress}</b>""",
	"kb": profile_kb
}]

MessagesInline = [
	{
		# call.data : text
		"send": f"""Выберите, сколько вы хотите отправить 💵: """,
		"kb": hide
	}
]