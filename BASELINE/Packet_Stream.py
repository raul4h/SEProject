from Tkinter import*


class PS():
	called=1
	
	def __init__(self,projectName,add_or_del):
		if PS.called:
			self.Console_Area()
		
	def Console_Area(self):
		PS.called=0
		PS.window = Toplevel()
		menu = Menu(PS.window)
		PS.window.title("Packet Stream Area")
		PS.window.configure(menu = menu)
		
		#window.configure(menu = menu)
		PS.window.geometry('800x100')

		submenu = Menu(menu, bg = 'blue')
		menu.add_cascade(label = "No.  ")
		menu.add_cascade(label = "Time     ")
		menu.add_cascade(label = "Source              ")
		menu.add_cascade(label = "Destination              ")
		menu.add_cascade(label = "Protocol             ")
		menu.add_cascade(label = "Info         ")
		
		
		
		
		###### Icon for the main window ######
		winIcon = PhotoImage(file = 'shark.gif')
		PS.window.tk.call('wm', 'iconphoto', PS.window._w, winIcon)
