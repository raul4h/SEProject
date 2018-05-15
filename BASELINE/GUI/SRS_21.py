# -*- coding: utf-8 -*-
'''
Title:    Project Navigator View 
Created:  Saturday March 5, 2018. 00:33:00
@author:  Alfredo Garcia
'''


from Tkinter import*


def test_window():
    ##### Window Pane for the Project View #####
    window = Toplevel()
    menu = Menu(window)
    window.title("Project Navigator")
    
    #window.configure(menu = menu)
    window.geometry('300x500')
    
    
    
    
    ###### Icon for the main window ######
#    winIcon = PhotoImage(file = 'shark.gif')
#    window.tk.call('wm', 'iconphoto', window._w, winIcon)
    
    ##### Labels for the Workspace and Projects #####
    Label(text="one").pack()
    separator = Frame(window, cursor='dot', height=500, bd=2, relief=GROOVE)
    separator.pack(fill=X, padx=5, pady=5)

