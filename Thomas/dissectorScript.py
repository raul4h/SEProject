from Tkinter import *
from tkFileDialog import askopenfilename

OPTIONS = [
"lua"
]

def openFileExplorer():
    filename = askopenfilename()

def dissectorScript():
    root = Toplevel()
    root.geometry("550x150")
    root.title("Dissector Script Generator")
    root.resizable(False, False)
    root.configure(background="#D9E5EF")
                   
    mainLabel = Label(root, text="Generate a custom dissector script from a selected project.", background="#D9E5EF")
    projectLabel = Label(root, text="Project", background="#D9E5EF")
    project = Entry(root, text="Project Name", width=50)
    projectBrowse = Button(root, text="Browse",command=openFileExplorer)
    
    mainLabel.grid(row=0, column=1)
    projectLabel.grid(row=1, column=0)
    project.grid(row=1, column=1)
    projectBrowse.grid(row=1, column=3)
    
    variable = StringVar(root)
    variable.set(OPTIONS[0])
    dissectorLabel = Label(root, text="Dissector Format", background="#D9E5EF")
    dissectorFormat = OptionMenu(root, variable, *OPTIONS)
    dissectorFormat.config(width=44)
    dissectorFormat.config(bg = "WHITE")
    dissectorLabel.grid(row=3, column=0)
    dissectorFormat.grid(row=3, column=1)
    
    
    saveLocation = Label(root, text="Save Location")
    dissectorLocation = Entry(root, width=50)
    browseSaveL = Button(root, text="Browse", command=openFileExplorer)
    
    
    saveLocation.grid(row=6, column=0)
    dissectorLocation.grid(row=6, column=1)
    browseSaveL.grid(row=6, column=3)
    
    generateDissector = Button(root, text="Generate")
    cancel = Button(root, text="Cancel", command=root.destroy)
    generateDissector.grid(row=10, column=2)
    cancel.grid(row=10, column=3)
