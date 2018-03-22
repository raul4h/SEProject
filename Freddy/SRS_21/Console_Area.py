

from Tkinter import*


class CN():
	called=1
	
	def __init__(self,projectName,add_or_del):
		if CN.called:
			self.Console_Area()
		
	def Console_Area(self):
		CN.called=0
		CN.window = Toplevel()
		menu = Menu(CN.window)
		CN.window.title("Console Area")
		
		#window.configure(menu = menu)
		CN.window.geometry('800x100')


		###### Icon for the main window ######
		winIcon = PhotoImage(file = 'shark.gif')
		CN.window.tk.call('wm', 'iconphoto', CN.window._w, winIcon)

		##### Labels for the Workspace and Projects #####
		Label(CN.window, text="No Error Message is Displayed", fg="Dark Gray", font="none 10").grid(row = 0,column = 0,columnspan = 8,sticky = W)
	