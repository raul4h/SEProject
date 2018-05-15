from Tkinter import*


class DS():
	called=1
	
	def __init__(self,projectName,add_or_del):
		if DS.called:
			self.Console_Area()
		
	def Console_Area(self):
		DS.called=0
		DS.window = Toplevel()
		menu = Menu(DS.window)
		DS.window.title("Dissected Stream Area")
		
		#window.configure(menu = menu)
		DS.window.geometry('800x100')


		###### Icon for the main window ######
		winIcon = PhotoImage(file = 'shark.gif')
		DS.window.tk.call('wm', 'iconphoto', DS.window._w, winIcon)
		
		#dissectedPhoto = PhotoImage(file = 'DissectedStream.gif')
		##### Labels for the Workspace and Projects #####
		Label(DS.window).grid(row = 0,column = 0,columnspan = 8,sticky = W)
	