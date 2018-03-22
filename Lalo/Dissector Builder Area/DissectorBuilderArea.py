from Tkinter import *
import ConstWindow
import field

def vp_start_gui():

    global val, w, root
    root = Tk()
    top = DissectorBuilderArea (root)
    root.iconbitmap("shark.ico")
    root.mainloop()

w = None
def create_Dissector_Builder_Area(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = DissectorBuilderArea (w)
    return (w, top)
def fieldWindow():
    field.start_gui()
    field.create_Field()
    field.Field

def conWindow():
 ConstWindow.start_gui()
 ConstWindow.create_New_Toplevel()
 ConstWindow.New_Toplevel


class DissectorBuilderArea:
    def __init__(self, top=None):


        top.geometry("979x359")
        top.title("Dissector Builder Area")
        top.configure(background="#bfbfbf")



        self.drawingCanvas = Canvas(top)
        self.drawingCanvas.place(relx=0.01, rely=0.08, relheight=0.84
                , relwidth=0.66)
        self.drawingCanvas.configure(background="#ffffff")
        self.drawingCanvas.configure(borderwidth="2")
        self.drawingCanvas.configure(insertbackground="black")
        self.drawingCanvas.configure(relief=RIDGE)
        self.drawingCanvas.configure(selectbackground="#c4c4c4")
        self.drawingCanvas.configure(selectforeground="black")
        self.drawingCanvas.configure(width=643)

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.68, rely=0.08, relheight=0.85, relwidth=0.3)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(width=295)

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.0, rely=0.0, height=36, width=302)
        self.Label4.configure(background="#d9e5ef")
        self.Label4.configure(relief=GROOVE)
        self.Label4.configure(text='''Palette''')
        self.Label4.configure(width=302)


        self.fieldButton = Button(self.Frame1, command = fieldWindow)
        self.fieldButton.place(relx=0.0, rely=0.13, height=43, width=296)
        self.fieldButton.configure(background="#d9d9d9")
        self.fieldButton.configure(pady="0")
        self.fieldButton.configure(relief=GROOVE)
        self.fieldButton.configure(text='''Field''')
        self.fieldButton.configure(width=296)


        self.cButton = Button(self.Frame1, command = conWindow)
        self.cButton.place(relx=-0.03, rely=0.3, height=43, width=316)
        self.cButton.configure(background="#d9d9d9")
        self.cButton.configure(foreground="#000000")
        self.cButton.configure(pady="0")
        self.cButton.configure(relief=GROOVE)
        self.cButton.configure(text='''Construct''')
        self.cButton.configure(width=316)

        self.Label7 = Label(top)
        self.Label7.place(relx=-0.01, rely=0.0, height=36, width=1002)
        self.Label7.configure(background="#d9e5ef")
        self.Label7.configure(relief=GROOVE)
        self.Label7.configure(text='''Dissector Builder Area''')
        self.Label7.configure(width=1002)





if __name__ == '__main__':
    vp_start_gui()


