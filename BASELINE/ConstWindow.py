from tkinter import *


def start_gui():
    global val, w, root
    root = Tk()
    top = New_Toplevel(root)
    root.title("Construct")
    root.iconbitmap("shark.ico")
    root.mainloop()


w = None


def create_New_Toplevel(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = New_Toplevel(w)
    return (w, top)

class New_Toplevel:

    def __init__(self, top=None):
        top.geometry("250x325")
        top.title("New Toplevel")
        top.configure(background="#fcfcfc")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.1, relheight=0.16, relwidth=1.02)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#fcfcfc")
        self.Frame1.configure(width=255)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.0, rely=0.15, height=16, width=63)
        self.Label2.configure(background="#fcfcfc")
        self.Label2.configure(text='''Decision''')
        self.Label2.configure(width=63)

        self.expButton = Button(self.Frame1)
        self.expButton.place(relx=0.27, rely=0.31, height=33, width=86)
        self.expButton.configure(background="#d9d9d9")
        self.expButton.configure(pady="0")
        self.expButton.configure(text='''Expression''')
        self.expButton.configure(width=86)

        self.cLabel = Label(top)
        self.cLabel.place(relx=0.0, rely=0.02, height=26, width=132)
        self.cLabel.configure(background="#fcfcfc")
        self.cLabel.configure(font="none 16 bold")
        self.cLabel.configure(text='''Construct''')
        self.cLabel.configure(width=132)

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=-0.04, rely=0.25, relheight=0.16, relwidth=1.06)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#fcfcfc")
        self.Frame1.configure(width=265)

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.04, rely=0.15, height=16, width=72)
        self.Label3.configure(background="#fcfcfc")
        self.Label3.configure(text='''Connector''')
        self.Label3.configure(width=72)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.3, rely=0.31, height=33, width=86)
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''-------->''')
        self.Button3.configure(width=86)

        self.Label4 = Label(top)
        self.Label4.place(relx=0.0, rely=0.42, height=16, width=72)
        self.Label4.configure(background="#fcfcfc")
        self.Label4.configure(text='''Expression''')
        self.Label4.configure(width=72)

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.08, rely=0.47, relheight=0.21, relwidth=0.86)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#fcfcfc")
        self.Frame2.configure(width=215)

        self.Label5 = Label(self.Frame2)
        self.Label5.place(relx=0.05, rely=0.12, height=16, width=152)
        self.Label5.configure(background="#fcfcfc")
        self.Label5.configure(text='''Relational Operator''')
        self.Label5.configure(width=152)

        self.lessThanEqButton = Button(self.Frame2)
        self.lessThanEqButton.place(relx=0.33, rely=0.38, height=23, width=26)
        self.lessThanEqButton.configure(background="#d9d9d9")
        self.lessThanEqButton.configure(pady="0")
        self.lessThanEqButton.configure(text='''<=''')

        self.greaterThanButton = Button(self.Frame2)
        self.greaterThanButton.place(relx=0.19, rely=0.38, height=23, width=26)
        self.greaterThanButton.configure(background="#d9d9d9")
        self.greaterThanButton.configure(pady="0")
        self.greaterThanButton.configure(text='''>''')

        self.greaterThanorEqButton = Button(self.Frame2)
        self.greaterThanorEqButton.place(relx=0.47, rely=0.38, height=23
                , width=26)
        self.greaterThanorEqButton.configure(background="#d9d9d9")
        self.greaterThanorEqButton.configure(pady="0")
        self.greaterThanorEqButton.configure(text='''>=''')

        self.equalButton = Button(self.Frame2)
        self.equalButton.place(relx=0.6, rely=0.38, height=23, width=26)
        self.equalButton.configure(background="#d9d9d9")
        self.equalButton.configure(pady="0")
        self.equalButton.configure(text='''==''')

        self.Button2 = Button(self.Frame2)
        self.Button2.place(relx=0.74, rely=0.38, height=23, width=26)
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''~=''')

        self.LessThanButton = Button(self.Frame2)
        self.LessThanButton.place(relx=0.05, rely=0.38, height=23, width=26)
        self.LessThanButton.configure(background="#d9d9d9")
        self.LessThanButton.configure(pady="0")
        self.LessThanButton.configure(text='''<''')

        self.Frame3 = Frame(top)
        self.Frame3.place(relx=0.08, rely=0.66, relheight=0.18, relwidth=0.86)
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(background="#fcfcfc")
        self.Frame3.configure(width=215)

        self.logicalOperator = Label(self.Frame3)
        self.logicalOperator.place(relx=0.14, rely=0.13, height=16, width=122)
        self.logicalOperator.configure(background="#fcfcfc")
        self.logicalOperator.configure(text='''Logical Operator''')
        self.logicalOperator.configure(width=122)

        self.andButton = Button(self.Frame3)
        self.andButton.place(relx=0.05, rely=0.43, height=23, width=26)
        self.andButton.configure(background="#d9d9d9")
        self.andButton.configure(pady="0")
        self.andButton.configure(text='''And''')

        self.orButton = Button(self.Frame3)
        self.orButton.place(relx=0.23, rely=0.43, height=23, width=26)
        self.orButton.configure(background="#d9d9d9")
        self.orButton.configure(pady="0")
        self.orButton.configure(text='''Or''')

        self.notButton = Button(self.Frame3)
        self.notButton.place(relx=0.42, rely=0.43, height=23, width=26)
        self.notButton.configure(background="#d9d9d9")
        self.notButton.configure(pady="0")
        self.notButton.configure(text='''Not''')

        self.operand = Button(top)
        self.operand.place(relx=0.16, rely=0.88, height=33, width=86)
        self.operand.configure(background="#d9d9d9")
        self.operand.configure(pady="0")
        self.operand.configure(text='''Operand''')
        self.operand.configure(width=86)




if __name__ == '__main__':
    start_gui()

