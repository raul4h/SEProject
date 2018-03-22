# -*- coding: utf-8 -*-
'''
Title:    Project Navigator View 
Created:  Saturday March 5, 2018. 00:33:00
@author:  Alfredo Garcia
'''


from Tkinter import*
from Project_Navigator import PN
#from Whatever import createGameURLs



##### Window Pane for the Project View #####
window = Tk()
menu = Menu(window)
window.title("Project Navigator")

#window.configure(menu = menu)
window.geometry('300x500')

global number2
number1 = 0
number2 = 0


def change_to_open1(num1):
	
	if num1 == 0:
		print "click!"
		project1.configure(image = open_folderIcon)
		b1.configure(foreground = 'blue')
		b2.configure(foreground = 'black')
		global number1
		number1 = 1
	else:
		print "Again?"
		b1.configure(foreground = 'blue')
		b2.configure(foreground = 'black')
	
	
def change_to_open2(num2):
	if num2 == 0:
		print "click!"
		project2.configure(image = open_folderIcon)
		b1.configure(foreground = 'black')
		b2.configure(foreground = 'blue')
		global number2
		number2 = 1
	else:
		print "Again?"
		b1.configure(foreground = 'black')
		b2.configure(foreground = 'blue')





###### Icon for the main window ######
winIcon = PhotoImage(file = 'shark.gif')
window.tk.call('wm', 'iconphoto', window._w, winIcon)

##### Labels for the Workspace and Projects #####
Label(window, text="Workspace: ", fg="black", font="none 14").grid(row = 1,column = 0,columnspan = 8,sticky = W)

closed_folderIcon = PhotoImage(file = 'closedFolder.gif')
open_folderIcon = PhotoImage(file = 'openFolder.gif')


project1 = Label(window,  font="none 11", image = closed_folderIcon, height = 50, compound = LEFT)
project1.grid(row = 2,column = 6,columnspan = 4,sticky = W)
b1 = Button(window, text="Project 1", bd = 0, foreground = "black", cursor = 'hand2', font = 'none 12', command = lambda: PN("Project",0))

b1.grid(row = 2, column = 8, columnspan = 4, sticky = W)


project2 = Label(window, font="none 11", image = closed_folderIcon, height = 50, compound = LEFT)
project2.grid(row = 3,column = 6,columnspan = 4,sticky = W)
b2 = Button(window, text="Project 2", bd = 0, foreground = "black", cursor = 'hand2', font = 'none 12', command = lambda: PN("Hello",1))

b2.grid(row = 3, column = 8, columnspan = 4, sticky = W)


test = Button(window, image = open_folderIcon, bd = 0, cursor = 'hand2', text = "   TEST", font = 'none 12', compound = LEFT)
test.grid(row = 4, column = 8, columnspan = 4, sticky = W)


#Application Run
window.mainloop()