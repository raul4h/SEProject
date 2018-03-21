from tkinter import *
#from tkFileDialog import askopenfilename


def export():
    root = Toplevel()
    root.geometry("500x100")
    root.title("Dissector Script")
    root.resizable(False, False)
    root.configure(background="#D9E5EF")
    
    #def openFileExplorer():
    #    filename = askopenfilename()
    
    mainLabel = Label(root, text="Export a project to the local file system", background="#D9E5EF")
    projectLabel = Label(root, text="Project", background="#D9E5EF")
    project = Entry(root, text="Project Name", width=50)
    projectBrowse = Button(root, text="Browse")
    
    mainLabel.grid(row=0, column=1)
    projectLabel.grid(row=1, column=0)
    project.grid(row=1, column=1)
    projectBrowse.grid(row=1, column=3)
    
    
    exportLabel = Label(root, text="To export file", background="#D9E5EF")
    exportEntry = Entry(root, text="Local File Systems Path", width=50)
    exportBrowse = Button(root, text="Browse")
    
    
    exportLabel.grid(row=2, column=0)
    exportEntry.grid(row=2, column=1)
    exportBrowse.grid(row=2, column=3)
    
    importProject = Button(root, text="Export")
    cancel = Button(root, text="Cancel", command=root.destroy)
    importProject.grid(row=3, column=2)
    cancel.grid(row=3, column=3)
