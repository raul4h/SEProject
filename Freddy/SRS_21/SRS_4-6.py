# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 23:22:58 2018
@author: Raul
"""
from Tkinter import*

window = Tk()
window.title("LabShark")
window.configure(background="white")

#Title
Label(window, text="Protocol Dissector Generator System", bg="white", fg="orange", font="none 16 bold").grid(row=0,column=0,columnspan=8,sticky=W)

#Create Project Pop Up
def create_window():
    create = Toplevel(window)
    create.configure(background="#D9E5EF")
    create.geometry('{}x{}'.format(500,200))
    create.title("New Project")
    Label(create, text="Create a new project",background="#D9E5EF").grid(row=0,column=0,columnspan=5)
    Label(create, text="Project Name",background="#D9E5EF").grid(row=1,column=0,sticky=W)
    Label(create, text="Description",background="#D9E5EF").grid(row=2,column=0,sticky=W)
    Entry(create,width=50).grid(row=1,column=1,sticky=E,padx=5,pady=5,columnspan=2)
    Entry(create,width=50).grid(row=2,column=1,sticky=E,padx=5,pady=5,columnspan=2)
    Button( create,text="Create", relief="groove").grid(row=3,column=1,padx=2, sticky=E)
    Button( create,text="Cancel", relief="groove").grid(row=3,column=2,padx=2, sticky=W)
    
def launcher_window():
    create = Toplevel(window)
    create.configure(background="#D9E5EF")
    create.geometry('{}x{}'.format(500,200))
    create.title("Workspace Launcher")
    Label(create, text="Select a directory as workspace: PDGS uses the workspace directory to store projects.",background="#D9E5EF").grid(row=0,column=0,columnspan=5)
    Label(create, text="Project Name",background="#D9E5EF").grid(row=1,column=0,sticky=W)
    Entry(create,width=50).grid(row=1,column=1,sticky=E,padx=5,pady=5,columnspan=2)
    Button( create,text="Create", relief="groove").grid(row=3,column=1,padx=2, sticky=E)
    Button( create,text="Cancel", relief="groove").grid(row=3,column=2,padx=2, sticky=W)
    Button( create,text="Browse", relief="groove").grid(row=2,column=3,padx=2, sticky=E)


#Buttons
Button( window,text="Create Project",command=create_window,relief="groove",width=11).grid(row=1,column=0,padx=2)
Button( window,text="Save Project", relief="groove",width=11).grid(row=1,column=1,padx=2)
Button( window,text="Close Project",relief="groove",width=11).grid(row=1,column=2,padx=2)
Button( window,text="Switch Workspace",relief="groove",width=15).grid(row=1,column=3,padx=2)
Button( window,text="Import Project",relief="groove",width=12).grid(row=1,column=4,padx=2)
Button( window,text="Export Project",relief="groove",width=12).grid(row=1,column=5,padx=2)
Button( window,text="Generate Dissector Script",relief="groove",width=20).grid(row=1,column=6,padx=2)
Button( window,text="Organize Views",relief="groove",width=13).grid(row=1,column=7,padx=2)
Button( window,text="Open PCAP",relief="groove",width=11).grid(row=1,column=8,padx=2)
    
#Application Run
window.mainloop()