from Data.Profile import Profile
from telebot.types import ReplyKeyboardMarkup
from Reply_Keyboards import *

profile = Profile()
count = profile.count
adress = profile.adress_generate()

Messages = [
{
	"start_message": f"""Приветствую тебя. Добро пожаловать в <b>Levendauer</b>
	""",
	"kb": start_menu
},
{
	"Профиль 👤": f"""На вашем счете: <b><i>{count}💵 </i></b>\nВаш адрес: <b>{adress}</b>""",
	"kb": hide
}]