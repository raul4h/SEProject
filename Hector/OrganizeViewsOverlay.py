from Tkinter import *
from tkFileDialog import askopenfilename


global root
root = Tk()
root.geometry("600x250")
root.title("Dissector Script")
root.resizable(False, False)
root.configure(background="#D9E5EF")

def openFileExplorer():
    filename = askopenfilename()


mainLabel = Label(root, text="Generate a custom dissector script from a selected project.", background="#D9E5EF")
hideLabel = Label(root, text="Hide", background="#D9E5EF")
showLabel = Label(root, text="Show", background="#D9E5EF")
projectNavLabel = Label(root, text="Project Navigation", background="#D9E5EF")
dissectorLabel = Label(root, text="Dissector Building Area", background="#D9E5EF")
palleteLabel = Label(root, text="Palette", background="#D9E5EF")
PacketStreamAreaLabel = Label(root, text="Packet Stream Area", background="#D9E5EF")
DissectedStreamAreaLabel = Label(root, text="Dissected Stream Area", background="#D9E5EF")
RawDataStreamLabel = Label(root, text="Raw Data Area", background="#D9E5EF")
ConsoleAreaLable = Label(root, text="Console Area", background="#D9E5EF")



def showWindows():
    print "here"

def setDefaults():
    pnOff.select()
    dissOff.select()
    palleteOff.select()
    packSOff.select()
    dissSOff.select()
    RDOff.select()
    cOff.select()


show = []
hide = []
vars = []

global default
default = 0;

mainLabel.grid(row=0, column=5)
hideLabel.grid(row=1, column=5)
showLabel.grid(row=1, column=7)

projectNavLabel.grid(row=2, column=0, columnspan=1, sticky='W')
v1 = IntVar()
vars.append(v1)
global pnOff
pnOff = Radiobutton(root, variable=v1, value=0, background="#D9E5EF")
pnOff.grid(row=2, column=5)
hide.append(pnOff)
pnOn = Radiobutton(root, variable=v1, value=1, background="#D9E5EF")
pnOn.grid(row=2, column=7)
show.append(pnOn)


dissectorLabel.grid(row=3, column=0, sticky='W')
var2 = IntVar()
vars.append(var2)
global dissSOff
dissOff = Radiobutton(root, variable=var2, value=0, background="#D9E5EF")
dissOff.grid(row=3, column=5)
hide.append(dissOff)
dissOn = Radiobutton(root, variable=var2, value=1, background="#D9E5EF")
dissOn.grid(row=3, column=7)
show.append(dissOn)

palleteLabel.grid(row=4, column=0, sticky='W')
var3 = IntVar()
vars.append(var3)
global palleteOff
palleteOff = Radiobutton(root, variable=var3, value=0, background="#D9E5EF")
palleteOff.grid(row=4, column=5)
hide.append(palleteOff)
palleteOn = Radiobutton(root, variable=var3, value=1, background="#D9E5EF")
palleteOn.grid(row=4, column=7)
show.append(palleteOn)


PacketStreamAreaLabel.grid(row=5, column=0, sticky='W')
var4 = IntVar()
vars.append(var4)
global packSOff
packSOff = Radiobutton(root, variable=var4, value=0, background="#D9E5EF")
packSOff.grid(row=5, column=5)
hide.append(packSOff)
packSOn = Radiobutton(root, variable=var4, value=1, background="#D9E5EF")
packSOn.grid(row=5, column=7)
show.append(packSOn)

DissectedStreamAreaLabel.grid(row=6, column=0, sticky='W')
var7 = IntVar()
vars.append(var7)
global dissSOff
dissSOff = Radiobutton(root, variable=var7, value=0, background="#D9E5EF")
dissSOff.grid(row=6, column=5)
hide.append(dissSOff)
dissSOn = Radiobutton(root, variable=var7, value=1, background="#D9E5EF")
dissSOn.grid(row=6, column=7)
show.append(dissSOn)


RawDataStreamLabel.grid(row=7, column=0, sticky='W')
var5 = IntVar()
vars.append(var5)
global RDOff
RDOff = Radiobutton(root, variable=var5, value=0, background="#D9E5EF")
RDOff.grid(row=7, column=5)
hide.append(RDOff)
RDOn = Radiobutton(root, variable=var5, value=1, background="#D9E5EF")
RDOn.grid(row=7, column=7)
show.append(RDOn)


ConsoleAreaLable.grid(row=8, column=0, sticky='W')
var6 = IntVar()
vars.append(var6)
global cOff
cOff = Radiobutton(root, variable=var6, value=0, background="#D9E5EF")
cOff.grid(row=8, column=5)
hide.append(cOff)
cOn =  Radiobutton(root, variable=var6, value=1, background="#D9E5EF")
cOn.grid(row=8, column=7)
show.append(cOn)



restoreDefault = Button(root, text="Restore to Default", command=setDefaults).grid(row=10, column=0)
cancel = Button(root, text="Cancel", command=root.destroy).grid(row=10, column=6, columnspan=1)
confirm = Button(root, text="Confrim", command=showWindows).grid(row=10, column=7, columnspan=1)






root.mainloop()
