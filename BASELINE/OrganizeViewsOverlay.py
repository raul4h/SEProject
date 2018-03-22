from Tkinter import *
import Project_Navigator
import Console_Area
import DissectorBuilderArea
import ConstWindow
import Raw_Data
import field
import Packet_Stream
import Dissected_Stream

def manageViews():
    if v1.get() == 0:
        # hide project navigator
        print 'h'
    else:
        # show project navigator
        Project_Navigator.PN("Hello", 0)
    if var2.get() == 0:
        #hide dissector building Area
        print 'h'
    else:
        # show dissector builder area
        DissectorBuilderArea.vp_start_gui()
    
    if var4.get() == 0:
        #hide packet stream Area
        print 'h'
    else:
        # show packet stream area
        Packet_Stream.PS("Hello", 0)
        print 1
    if var5.get() == 0:
        #hide raw data Area
        Raw_Data.hide("No error", 0)

    else:
        # show raw data area
        Raw_Data.RN("No error",0)
    if var6.get() == 0:
        #hide console building Area
        print 'h'
    else:
        # show console builder area
         Console_Area.CN("No error",0)
    if var7.get() == 0:
        #hide dissector stream Area
        print 'h'
    else:
        # show dissector stream area
        Dissected_Stream.DS("Hello", 0)
        print 1



def setDefaults():
    pnOff.select()
    dissOff.select()
    palleteOff.select()
    packSOff.select()
    dissSOff.select()
    RDOff.select()
    cOff.select()

def organize_views():
    root = Toplevel()
    root.geometry("600x250")
    root.title("Dissector Script")
    root.resizable(False, False)
    root.configure(background="#D9E5EF")


    mainLabel = Label(root, text="Generate a custom dissector script from a selected project.", background="#D9E5EF")
    hideLabel = Label(root, text="Hide", background="#D9E5EF")
    showLabel = Label(root, text="Show", background="#D9E5EF")
    projectNavLabel = Label(root, text="Project Navigation", background="#D9E5EF")
    dissectorLabel = Label(root, text="Dissector Building Area", background="#D9E5EF")
    PacketStreamAreaLabel = Label(root, text="Packet Stream Area", background="#D9E5EF")
    DissectedStreamAreaLabel = Label(root, text="Dissected Stream Area", background="#D9E5EF")
    RawDataStreamLabel = Label(root, text="Raw Data Area", background="#D9E5EF")
    ConsoleAreaLable = Label(root, text="Console Area", background="#D9E5EF")


    show = []
    hide = []
    vars = []

    global default
    default = 0;

    mainLabel.grid(row=0, column=5)
    hideLabel.grid(row=1, column=5)
    showLabel.grid(row=1, column=7)

    projectNavLabel.grid(row=2, column=0, columnspan=1, sticky='W')
    global v1
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
    global var2
    var2 = IntVar()
    vars.append(var2)
    global dissOff
    dissOff = Radiobutton(root, variable=var2, value=0, background="#D9E5EF")
    dissOff.grid(row=3, column=5)
    hide.append(dissOff)
    dissOn = Radiobutton(root, variable=var2, value=1, background="#D9E5EF")
    dissOn.grid(row=3, column=7)
    show.append(dissOn)

    PacketStreamAreaLabel.grid(row=4, column=0, sticky='W')
    global var4
    var4 = IntVar()
    vars.append(var4)
    global packSOff
    packSOff = Radiobutton(root, variable=var4, value=0, background="#D9E5EF")
    packSOff.grid(row=4, column=5)
    hide.append(packSOff)
    packSOn = Radiobutton(root, variable=var4, value=1, background="#D9E5EF")
    packSOn.grid(row=4, column=7)
    show.append(packSOn)

    DissectedStreamAreaLabel.grid(row=5, column=0, sticky='W')
    global var7
    var7 = IntVar()
    vars.append(var7)
    global dissSOff
    dissSOff = Radiobutton(root, variable=var7, value=0, background="#D9E5EF")
    dissSOff.grid(row=5, column=5)
    hide.append(dissSOff)
    dissSOn = Radiobutton(root, variable=var7, value=1, background="#D9E5EF")
    dissSOn.grid(row=5, column=7)
    show.append(dissSOn)


    RawDataStreamLabel.grid(row=6, column=0, sticky='W')
    global var5
    var5 = IntVar()
    vars.append(var5)
    global RDOff
    RDOff = Radiobutton(root, variable=var5, value=0, background="#D9E5EF")
    RDOff.grid(row=6, column=5)
    hide.append(RDOff)
    RDOn = Radiobutton(root, variable=var5, value=1, background="#D9E5EF")
    RDOn.grid(row=6, column=7)
    show.append(RDOn)


    ConsoleAreaLable.grid(row=7, column=0, sticky='W')
    global var6
    var6 = IntVar()
    vars.append(var6)
    global cOff
    cOff = Radiobutton(root, variable=var6, value=0, background="#D9E5EF")
    cOff.grid(row=7, column=5)
    hide.append(cOff)
    cOn =  Radiobutton(root, variable=var6, value=1, background="#D9E5EF")
    cOn.grid(row=7, column=7)
    show.append(cOn)



    restoreDefault = Button(root, text="Restore to Default", command=setDefaults)
    restoreDefault.grid(row=9, column=0)
    cancel = Button(root, text="Cancel", command=root.destroy)
    cancel.grid(row=9, column=6, columnspan=1)
    confirm = Button(root, text="Confirm", command=manageViews)
    confirm.grid(row=9, column=7, columnspan=1)
