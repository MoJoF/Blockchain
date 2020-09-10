from tkinter import *

class View:
	def __init__(self):
		self.root = Tk()
		self.root.title("Levendauer Corp")
		self.root.geometry("300x500+320+200")

		self.frame1 = Frame() # В данном фрейме будут кнопки отправки и получения средств на кошелек

		self.root.mainloop()