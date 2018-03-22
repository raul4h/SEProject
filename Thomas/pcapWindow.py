from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

def vp_start_gui():
    global val, w, root
    root = Toplevel()
    root.iconbitmap("shark.ico")
    top = PCAP (root)
    root.mainloop()

w = None

def browsefile():
        tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                     filetypes=(("text files", "*.txt"), ("all files", "*.*")))

class PCAP:
    def __init__(self, top=None):


        top.geometry("500x250")
        top.title("PCAP")
        top.configure(relief="groove")
        top.configure(background="#f7f9fb")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.02, rely=0.07, relheight=0.9, relwidth=0.97)
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9e5ef")
        self.Frame1.configure(width=565)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.8, rely=0.33, height=33, width=60)
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(pady="0")
        self.Button2.configure(relief="groove")
        self.Button2.configure(text="Browse")
        self.Button2.configure(command=browsefile)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.67, rely=0.57, height=33, width=48)
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(pady="0")
        self.Button3.configure(relief="groove")
        self.Button3.configure(text="Open")

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.8, rely=0.57, height=33, width=56)
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(pady="0")
        self.Button4.configure(relief="groove")
        self.Button4.configure(text="Cancel")
        self.Button2.configure(command=root.destroy)

        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.21, rely=0.33,height=34, relwidth=0.56)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(width=314)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.34, rely=0.12, height=26, width=118)
        self.Label1.configure(background="#D9E5EF")
        self.Label1.configure(text="Open a PCAP file")

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.04, rely=0.33, height=26, width=87)
        self.Label2.configure(background="#D9E5EF")
        self.Label2.configure(text="PCAP NAME")






if __name__ == '__main__':
    vp_start_gui()


