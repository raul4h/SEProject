# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 23:22:58 2018

@author: Raul
"""
from Tkinter import *
from dissectorScript import dissectorScript
from projectExport import export
from projectImport import project_import
from SRS_21 import test_window
from OrganizeViewsOverlay import organize_views
from pcapWindow import vp_start
from Project_Navigator import PN
from Console_Area import CN

#window = Tk()
#window.title("LabShark")
#window.configure(background="white")
#
##Title
#Label(window, text="Protocol Dissector Generator System", bg="white", fg="orange", font="none 16 bold").grid(row=0,column=0,columnspan=8,sticky=W)

#Create Project Pop Up

def create_window():
    create = Toplevel()
    create.configure(background="#D9E5EF")
    create.geometry('{}x{}'.format(500,200))
    create.title("New Project")
    Label(create, text="Create a new project",background="#D9E5EF").grid(row=0,column=0,columnspan=5)
    Label(create, text="Project Name",background="#D9E5EF").grid(row=1,column=0,sticky=W)
    Label(create, text="Description",background="#D9E5EF").grid(row=2,column=0,sticky=W)
    e1 = Entry(create,width=50)
    e1.grid(row=1,column=1,sticky=E,padx=5,pady=5,columnspan=2)
    e2 = Entry(create,width=50)
    e2.grid(row=2,column=1,sticky=E,padx=5,pady=5,columnspan=2)
    Button( create,text="Create",command = lambda: addProject(e1.get()), relief="groove").grid(row=3,column=1,padx=2, sticky=E)
    Button( create,text="Cancel", relief="groove", command=create.destroy).grid(row=3,column=2,padx=2, sticky=W)

#Launcher    
def launcher_window():
    create = Toplevel()
    create.configure(background="#D9E5EF")
    create.geometry('{}x{}'.format(500,200))
    create.title("Workspace Launcher")
    Label(create, text="Select a directory as workspace: PDGS uses the workspace directory to store projects.",background="#D9E5EF").grid(row=0,column=0,columnspan=5)
    Label(create, text="Project Name",background="#D9E5EF").grid(row=1,column=0,sticky=W)
    Entry(create,width=50).grid(row=1,column=1,sticky=E,padx=5,pady=5,columnspan=2)
    Button( create,text="Create", relief="groove").grid(row=3,column=1,padx=2, sticky=E)
    Button( create,text="Cancel", relief="groove", command=create.destroy).grid(row=3,column=2,padx=2, sticky=W)
    Button( create,text="Browse", relief="groove").grid(row=2,column=3,padx=2, sticky=E)


##### Labels for the Workspace and Projects #####
#Label(separator, text="Workspace: ", fg="black", font="none 14").grid(row = 2,column = 0,columnspan = 8,sticky = W)
#closed_folderIcon = PhotoImage(file = 'closedFolder.gif')		

buttonList = []
#rowNum = 3


	############################################################        Placing Buttons       ###########################################################
#def addProject(projectName):
#    global buttonList
#    global rowNum
#    open_folderIcon = PhotoImage(file = 'openFolder.gif')
#    buttonList.append(Button(separator,bd = 0, cursor = 'hand2', text = "   " + projectName + str(rowNum), font = 'none 12',background="#D9E5EF", compound = LEFT))
#    buttonList[-1].grid(row = rowNum, column = 0, columnspan = 8, sticky = W)
#    rowNum = rowNum + 1
#    
#def closeProject():
#    global buttonList
#    global rowNum
#    buttonList[0].grid_remove()
#    buttonList.pop(0)
#    rowNum= rowNum - 1
                  

##Application Run
#window.mainloop()


class DragManager():
    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        widget.configure(cursor="hand1")

    def on_start(self, event):
        # you could use this method to create a floating window
        # that represents what is being dragged.
        pass

    def on_drag(self, event):
        # you could use this method to move a floating window that
        # represents what you're dragging
        pass

    def on_drop(self, event):
        # find the widget under the cursor
        x,y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x,y)
        try:
            target.configure(image=event.widget.cget("image"))
        except:
            pass