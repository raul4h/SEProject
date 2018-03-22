from Tkinter import *
from tkFileDialog import askopenfilename

root = Tk()
root.geometry("450x90")
root.title("Dissector Script")
root.resizable(False, False)
root.configure(background="#D9E5EF")

def openFileExplorer():
    filename = askopenfilename()

mainLabel = Label(root, text="Import a project into the current workspace", background="#D9E5EF")
projectLabel = Label(root, text="Project", background="#D9E5EF")
project = Entry(root, text="Project Name", width=50)
projectBrowse = Button(root, text="Browse", command=openFileExplorer)

mainLabel.grid(row=0, column=1)
projectLabel.grid(row=1, column=0)
project.grid(row=1, column=1)
projectBrowse.grid(row=1, column=3)

importProject = Button(root, text="Import")
cancel = Button(root, text="Cancel", command=root.destroy)


importProject.grid(row=2, column=2, )
cancel.grid(row=2, column=3)



root.mainloop()
