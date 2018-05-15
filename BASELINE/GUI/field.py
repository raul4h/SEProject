from Tkinter import *
#import ttk


def start_gui():
    global val, w, root
    root = Tk()
    top = Field (root)
    root.iconbitmap("shark.ico")
    root.mainloop()

w = None
def create_Field(root):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Field (w)

    return (w, top)

class Field:
    def __init__(self, top=None):

        top.geometry("250x300")
        top.title("Field")
        top.configure(background="#fcfcfc")



        self.fieldLabel = Label(top)
        self.fieldLabel.place(relx=0.04, rely=0.03, height=43, width=68)
        self.fieldLabel.configure(background="#f8f8f8")
        self.fieldLabel.configure(disabledforeground="#a3a3a3")
        self.fieldLabel.configure(font="none 16 bold ")
        self.fieldLabel.configure(foreground="#000000")
        self.fieldLabel.configure(text='''Field''')

        self.startButton = Button(top)
        self.startButton.place(relx=0.07, rely=0.2, height=33, width=76)
        self.startButton.configure(background="#d9d9d9")
        self.startButton.configure(pady="0")
        self.startButton.configure(relief=GROOVE)
        self.startButton.configure(text='''Start Field''')
        self.startButton.configure(width=76)

        self.byte2Button = Button(top)
        self.byte2Button.place(relx=0.07, rely=0.32, height=33, width=96)
        self.byte2Button.configure(background="#d9d9d9")
        self.byte2Button.configure(pady="0")
        self.byte2Button.configure(relief=GROOVE)
        self.byte2Button.configure(text='''Field (2 byte)''')
        self.byte2Button.configure(width=96)

        self.byte8Button = Button(top)
        self.byte8Button.place(relx=0.07, rely=0.43, height=33, width=96)
        self.byte8Button.configure(background="#d9d9d9")
        self.byte8Button.configure(pady="0")
        self.byte8Button.configure(relief=GROOVE)
        self.byte8Button.configure(text='''Field (8 byte)''')

        self.byte82Button = Button(top)
        self.byte82Button.place(relx=0.07, rely=0.55, height=33, width=96)
        self.byte82Button.configure(background="#d9d9d9")
        self.byte82Button.configure(pady="0")
        self.byte82Button.configure(relief=GROOVE)
        self.byte82Button.configure(text='''Field (8 byte)''')

        self.varSizeButton = Button(top)
        self.varSizeButton.place(relx=0.07, rely=0.67, height=33, width=106)
        self.varSizeButton.configure(background="#d9d9d9")
        self.varSizeButton.configure(pady="0")
        self.varSizeButton.configure(relief=GROOVE)
        self.varSizeButton.configure(text='''Field (Var Size)''')
        self.varSizeButton.configure(width=106)

        self.referenceButton = Button(top)
        self.referenceButton.place(relx=0.07, rely=0.78, height=33, width=106)
        self.referenceButton.configure(background="#d9d9d9")
        self.referenceButton.configure(pady="0")
        self.referenceButton.configure(relief=GROOVE)
        self.referenceButton.configure(text='''Reference List''')
        self.referenceButton.configure(width=106)

        self.byte1Button = Button(top)
        self.byte1Button.place(relx=0.55, rely=0.2, height=33, width=96)
        self.byte1Button.configure(background="#d9d9d9")
        self.byte1Button.configure(pady="0")
        self.byte1Button.configure(relief=GROOVE)
        self.byte1Button.configure(text='''Field (1 byte)''')

        self.byte4Button = Button(top)
        self.byte4Button.place(relx=0.55, rely=0.32, height=33, width=96)
        self.byte4Button.configure(background="#d9d9d9")
        self.byte4Button.configure(pady="0")
        self.byte4Button.configure(relief=GROOVE)
        self.byte4Button.configure(text='''Field (4 byte)''')

        self.byte16Button = Button(top)
        self.byte16Button.place(relx=0.55, rely=0.43, height=33, width=106)
        self.byte16Button.configure(background="#d9d9d9")
        self.byte16Button.configure(pady="0")
        self.byte16Button.configure(relief=GROOVE)
        self.byte16Button.configure(text='''Field (16 byte)''')
        self.byte16Button.configure(width=106)

        self.byte162Button = Button(top)
        self.byte162Button.place(relx=0.55, rely=0.55, height=33, width=106)
        self.byte162Button.configure(background="#d9d9d9")
        self.byte162Button.configure(pady="0")
        self.byte162Button.configure(relief=GROOVE)
        self.byte162Button.configure(text='''Field (16 byte)''')
        self.byte162Button.configure(width=106)

        self.endButton = Button(top)
        self.endButton.place(relx=0.55, rely=0.67, height=33, width=96)
        self.endButton.configure(background="#d9d9d9")
        self.endButton.configure(pady="0")
        self.endButton.configure(relief=GROOVE)
        self.endButton.configure(text='''End Field''')

        self.pInfoButton = Button(top)
        self.pInfoButton.place(relx=0.55, rely=0.78, height=33, width=96)
        self.pInfoButton.configure(background="#d9d9d9")
        self.pInfoButton.configure(pady="0")
        self.pInfoButton.configure(relief=GROOVE)
        self.pInfoButton.configure(text='''Packet Info.''')






if __name__ == '__main__':
   start_gui()

