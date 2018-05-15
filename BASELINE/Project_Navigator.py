# -*- coding: utf-8 -*-
'''
Title:    Project Navigator View 
Created:  Saturday March 5, 2018. 00:33:00
@author:  Alfredo Garcia
'''


from Tkinter import*



class PN():
	called=1
	buttonList = []
	rowNum = 1
	window = None
	def __init__(self,projectName,add_or_del):
		if PN.called:
			self.Project_Navigator()
			
		if not add_or_del:
			self.createWindow(projectName+ " " + str(PN.rowNum))
			
		else:
			PN.buttonList[0].grid_remove()
			PN.buttonList.pop(0)


	############################################################     Adding Buttons Array     ###########################################################
	#@static_vars(counter=0)
	def Project_Navigator(self):
		PN.called=0
		PN.window = Toplevel()
		
		menu = Menu(PN.window)
		PN.window.title("Project Navigator")
		
		#window.configure(menu = menu)
		PN.window.geometry('300x500')


		###### Icon for the main window ######
		winIcon = PhotoImage(file = 'shark.gif')
		PN.window.tk.call('wm', 'iconphoto', PN.window._w, winIcon)

		##### Labels for the Workspace and Projects #####
		Label(PN.window, text="Workspace: ", fg="black", font="none 14").grid(row = 0,column = 0,columnspan = 8,sticky = W)



		closed_folderIcon = PhotoImage(file = 'closedFolder.gif')
		
		
		
		

	############################################################        Placing Buttons       ###########################################################
	def createWindow(self,projectName):
		open_folderIcon = PhotoImage(file = 'openFolder.gif')
		PN.buttonList.append(Button(PN.window,bd = 0, cursor = 'hand2', text = "   " + projectName, font = 'none 12', compound = LEFT))
		PN.buttonList[-1].grid(row = PN.rowNum, column = 6, columnspan = 8, sticky = W)
		PN.rowNum = PN.rowNum + 1
			


