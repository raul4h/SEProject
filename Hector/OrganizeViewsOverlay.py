from tkinter import *
#from tkFileDialog import askopenfilename


global root
root = Tk()
root.geometry("600x250")
root.title("Dissector Script")
root.resizable(False, False)
root.configure(background="#D9E5EF")

#def openFileExplorer():
#    filename = askopenfilename()


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
    print ("here")




mainLabel.grid(row=0, column=5)
hideLabel.grid(row=1, column=5)
showLabel.grid(row=1, column=7)
projectNavLabel.grid(row=2, column=0, columnspan=1, sticky='W')
v1 = IntVar()
pnOff = Radiobutton(root, variable=v1, value=0, background="#D9E5EF").grid(row=2, column=5)
pnOn = Radiobutton(root, variable=v1, value=1, background="#D9E5EF").grid(row=2, column=7)
dissectorLabel.grid(row=3, column=0, sticky='W')
var2 = IntVar()
dissOff = Radiobutton(root, variable=var2, value=0, background="#D9E5EF").grid(row=3, column=5)
dissOn = Radiobutton(root, variable=var2, value=1, background="#D9E5EF").grid(row=3, column=7)
palleteLabel.grid(row=4, column=0, sticky='W')
var3 = IntVar()
palleteOff = Radiobutton(root, variable=var3, value=0, background="#D9E5EF").grid(row=4, column=5)
palleteOn = Radiobutton(root, variable=var3, value=1, background="#D9E5EF").grid(row=4, column=7)
PacketStreamAreaLabel.grid(row=5, column=0, sticky='W')
var4 = IntVar()
packSOff = Radiobutton(root, variable=var4, value=0, background="#D9E5EF").grid(row=5, column=5)
packSOn = Radiobutton(root, variable=var4, value=1, background="#D9E5EF").grid(row=5, column=7)
DissectedStreamAreaLabel.grid(row=6, column=0, sticky='W')
var4 = IntVar()
dissSOff = Radiobutton(root, variable=var4, value=0, background="#D9E5EF").grid(row=6, column=5)
dissSOn = Radiobutton(root, variable=var4, value=1, background="#D9E5EF").grid(row=6, column=7)
RawDataStreamLabel.grid(row=7, column=0, sticky='W')
var5 = IntVar()
RDOff = Radiobutton(root, variable=var5, value=0, background="#D9E5EF").grid(row=7, column=5)
RDOn = Radiobutton(root, variable=var5, value=1, background="#D9E5EF").grid(row=7, column=7)
ConsoleAreaLable.grid(row=8, column=0, sticky='W')
var6 = IntVar()
cOff = Radiobutton(root, variable=var6, value=0, background="#D9E5EF").grid(row=8, column=5)
cOn =  Radiobutton(root, variable=var6, value=1, background="#D9E5EF",).grid(row=8, column=7)

restoreDefault = Button(root, text="Restore to Default").grid(row=10, column=0)
cancel = Button(root, text="Cancel", command=root.destroy).grid(row=10, column=6, columnspan=1)
confirm = Button(root, text="Confrim", command=showWindows).grid(row=10, column=7, columnspan=1)



root.mainloop()
