
from Tkinter import*
#from Project_Navigator import Project_Navigator


class Whatever():

	def createGameURLs(self):
		self.button = []
		for i in range(3):
			self.button.append(Button(self, text='Game '+str(i+1),command=lambda:self.open_this(i)))
			self.button[i].grid(column=4, row=i+1, sticky=W)
	def open_this(self, myNum):
		sprint(myNum)