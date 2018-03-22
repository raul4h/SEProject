from Tkinter import *


def start_Field():
    create =Tk()
    create.configure(background="#D9E5EF")
    create.geometry('{}x{}'.format(500, 120))
    create.title("Start Field[Protocol Name]")
    Label(create, text="Protocol Name", background="#D9E5EF").grid(row=0, column=0, sticky=W)
    Label(create, text="Protocol Description", background="#D9E5EF").grid(row=1, column=0, sticky=W)
    Label(create, text="Dependant Protocol Name", background="#D9E5EF").grid(row=2, column=0, sticky=W)
    Label(create, text="Dependancy Pattern", background="#D9E5EF").grid(row=3, column=0, sticky=W)

    Entry(create, width=50).grid(row=0, column=1, sticky=E, padx=5, pady=5, columnspan=2)
    Entry(create, width=50).grid(row=1, column=1, sticky=E, padx=5, pady=5, columnspan=2)
    Entry(create, width=50).grid(row=2, column=1, sticky=E, padx=5, pady=5, columnspan=2)
    Entry(create, width=50).grid(row=3, column=1, sticky=E, padx=5, pady=5, columnspan=2)
    create.mainloop()

def create_Field():
    create = Tk()
    create.configure(background="#D9E5EF")
    create.geometry('{}x{}'.format(500,400))
    create.title("Field[Abbreviation]")
    Label(create, text="Name", background="#D9E5EF").grid(row=0, column=0, sticky=W)
    Label(create, text="Abbreviation", background="#D9E5EF").grid(row=1, column=0, sticky=W)
    Label(create, text="Description", background="#D9E5EF").grid(row=2, column=0, sticky=W)
    Label(create, text="Reference List", background="#D9E5EF").grid(row=3, column=0, sticky=W)
    Label(create, text="Data Type", background="#D9E5EF").grid(row=4, column=0, sticky=W)
    Label(create, text="Base", background="#D9E5EF").grid(row=5, column=0, sticky=W)
    Label(create, text="Mask", background="#D9E5EF").grid(row=6, column=0, sticky=W)
    Label(create, text="Value Constraint", background="#D9E5EF").grid(row=7, column=0, sticky=W)
    Label(create, text="Required", background="#D9E5EF").grid(row=8, column=0, sticky=W)

    # Create a Tkinter variable
    tkvar = StringVar(create)

    # Dictionary with options
    choices = {'thiS area will be filled out more when controllers work',
               'This area will be filled out more when controllers work',
               'tHis area will be filled out more when controllers work',
               'thIs area will be filled out more when controllers work'}
    tkvar.set('Select from the predefined list of reference lists')  # set the default option

    refMenu = OptionMenu(create, tkvar, *choices)

    refMenu.grid(row=3, column=1, sticky="ew", columnspan=5)

    # Create a Tkinter variable
    tkvar1 = StringVar(create)

    # Dictionary with options
    choices1 = {'thiS area will be filled out more when controllers work',
                'This area will be filled out more when controllers work',
                'tHis area will be filled out more when controllers work',
                'thIs area will be filled out more when controllers work'}
    tkvar1.set('Select from list of data types')  # set the default option

    dataMenu = OptionMenu(create, tkvar1, *choices1)

    dataMenu.grid(row=4, column=1, sticky="ew", columnspan=5)

    # Create a Tkinter variable
    tkvar2 = StringVar(create)

    # Dictionary with options
    choices2 = {'thiS area will be filled out more when controllers work',
                'This area will be filled out more when controllers work',
                'tHis area will be filled out more when controllers work',
                'thIs area will be filled out more when controllers work'}
    tkvar2.set('Select from the list of bases')  # set the default option

    refMenu = OptionMenu(create, tkvar2, *choices)

    refMenu.grid(row=5, column=1, sticky="ew", columnspan=5)

    # on change dropdown value
    def change_dropdown(*args):
        print(tkvar2.get())

    # link function to change dropdown
    tkvar.trace('w', change_dropdown)
    v= IntVar
    Entry(create, width=50).grid(row=1, column=1, sticky=E, padx=5, pady=5, columnspan=2)
    Entry(create, width=50).grid(row=2, column=1, sticky=E, padx=5, pady=5, columnspan=2)
    Entry(create, width=50).grid(row=6, column=1, sticky=E, padx=5, pady=5, columnspan=2)
    Entry(create, width=50).grid(row=7, column=1, sticky=E, padx=5, pady=5, columnspan=2)
    Checkbutton(create, text="Yes", variable=v).grid(row=8, column=1, sticky="ew", padx=5, pady=5, columnspan=2)
    Entry(create, width=50).grid(row=0, column=1, sticky=E, padx=5, pady=5, columnspan=2)
    Button(create, text="Create", relief="groove").grid(row=9, column=1, padx=2, sticky=E)
    Button(create, text="Cancel", relief="groove").grid(row=9, column=2, padx=2, sticky=W)
    create.mainloop()


def End_window():
    create = Tk()
    create.configure(background="#D9E5EF")
    create.geometry('{}x{}'.format(500, 20))
    create.title("End Block")
    create.mainloop()

def ref_window():

    create = Tk()
    create.configure(background="#D9E5EF")
    create.geometry('{}x{}'.format(500, 110))
    create.title("Reference List [Reference List Name]")
    Label(create, text="Reference List Name", background="#D9E5EF").grid(row=0, column=0, sticky=W)
    Entry(create, width=50).grid(row=0, column=1, sticky=E, padx=5, pady=5, columnspan=2)

    Label(create, text="Value", background="#D9E5EF").grid(row=2, column=0, sticky=W, pady=5, columnspan=1)
    Entry(create, width=25).grid(row=3, column=0, sticky=W, padx=5)
    Label(create, text="Text Description", background="#D9E5EF").grid(row=2, column=1, sticky=W, columnspan=3)

    Entry(create, width=50).grid(row=3, column=2, sticky=E, padx=5, columnspan=1)
    Button(create, text="ADD", relief="groove").grid(row=8, column=2, padx=0, pady=5, sticky=E)
    create.mainloop()

def packet_info():
    create =Tk()
    create.configure(background="#D9E5EF")
    create.geometry('{}x{}'.format(500, 85))
    create.title("Packet Information")

    Label(create, text="Value", background="#D9E5EF").grid(row=0, column=0, sticky=W, pady=5, columnspan=1)
    Entry(create, width=25).grid(row=1, column=0, sticky=W, padx=5)
    Label(create, text="Text Description", background="#D9E5EF").grid(row=0, column=1, sticky=W, columnspan=3)

    Entry(create, width=50).grid(row=1, column=2, sticky=E, padx=5, columnspan=1)
    Button(create, text="ADD", relief="groove").grid(row=8, column=2, padx=0, pady=5, sticky=E)
    create.mainloop()

