from tkinter import *

class View:
	def __init__(self):
		self.root = Tk()
		self.root.title("Levendauer Corp")
		self.root.geometry("300x500+320+200")

		self.frame1 = Frame(self.root, height=300, width=300, bg='DarkSlateBlue') # В данном фрейме будут кнопки отправки и получения средств на кошелек
		self.frame1.pack(anchor=N)

		self.button_send = Button(self.frame1, text='Отправить', bg='MediumOrchid', fg='white', command=self.send())
		self.button_send.pack(anchor=NW)

		self.frame2 = Frame(self.root, height=200, width=300, bg='SlateBlue')
		self.frame2.pack(anchor=S)


		


		self.root.mainloop()


	def send(self):
		pass