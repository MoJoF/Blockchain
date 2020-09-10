from tkinter import *


class View:
	def __init__(self):
		self.root = Tk()
		self.root.title("Levendauer Corp")
		self.root.geometry("300x500+320+200")
		self.root.resizable(False, False)

		self.frame1 = Frame(self.root, height=300, width=300, bg='DarkSlateBlue') # В данном фрейме будут кнопки отправки и получения средств на кошелек
		self.frame1.place(x=0, y=0)		

		self.frame2 = Frame(self.root, height=200, width=300, bg='SlateBlue')
		self.frame2.place(x=0, y=300)

		self.button_send = Button(self.frame1, text='Отправить', bg='MediumOrchid', fg='white', command=self.send_coins())
		self.button_send.place(x=50, y=200, width=80, height=50)
		
		self.button_get = Button(self.frame1, text='Получить', bg='MediumOrchid', fg='white', command=self.get_coins())
		self.button_get.place(x=175, y=200, width=80, height=50)

		self.root.mainloop()


	def send_coins(self):
		pass


	def get_coins(self):
		pass