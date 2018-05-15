from Tkinter import *
from tkFileDialog import askopenfilename
from Console_Area import CN


def export():
    def openFileExplorer():
        exFilename = askopenfilename()
        project1.delete(0, END)
        project1.insert(0, exFilename)
	
    def openFileExplorer2():
        eFilename = askopenfilename()
        exportEntry.delete(0, END)
        exportEntry.insert(0, eFilename)
    root = Toplevel()
    root.geometry("500x100")
    root.title("Export a Project")
    root.resizable(False, False)
    root.configure(background="#D9E5EF")
    
    mainLabel = Label(root, text="Export a project to the local file system", background="#D9E5EF")
    projectLabel = Label(root, text="Project", background="#D9E5EF")
    project1 = Entry(root, text="Project Name", width=50)
    projectBrowse = Button(root, text="Browse",command=openFileExplorer)
    
    mainLabel.grid(row=0, column=1)
    projectLabel.grid(row=1, column=0)
    project1.grid(row=1, column=1)
    projectBrowse.grid(row=1, column=3)
    
    
    exportLabel = Label(root, text="To export file", background="#D9E5EF")
    exportEntry = Entry(root, text="Local File Systems Path", width=50)
    exportBrowse = Button(root, text="Browse",command=openFileExplorer2)
    
    
    exportLabel.grid(row=2, column=0)
    exportEntry.grid(row=2, column=1)
    exportBrowse.grid(row=2, column=3)
    
    importProject = Button(root, text="Export",command = lambda: CN("ERROR: No LUA SCRIPT CONTROLLERS DETECTED",0))
    cancel = Button(root, text="Cancel", command=root.destroy)
    importProject.grid(row=3, column=2)
    cancel.grid(row=3, column=3)
