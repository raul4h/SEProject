# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:16:00 2018

@author: rjhinostrozagarcia
"""
from Tkinter import *

def create_window():
    create = Toplevel()
    create.configure(background="#D9E5EF")
    create.geometry('{}x{}'.format(500,200))
    create.title("New Project")
    Label(create, text="Create a new project",background="#D9E5EF").grid(row=0,column=0,columnspan=5)
    Label(create, text="Project Name",background="#D9E5EF").grid(row=1,column=0,sticky=W)
    Label(create, text="Description",background="#D9E5EF").grid(row=2,column=0,sticky=W)
    Entry(create,width=50).grid(row=1,column=1,sticky=E,padx=5,pady=5,columnspan=2)
    Entry(create,width=50).grid(row=2,column=1,sticky=E,padx=5,pady=5,columnspan=2)
    Button( create,text="Create",command = lambda: createWindow("Project"), relief="groove").grid(row=3,column=1,padx=2, sticky=E)
    Button( create,text="Cancel", relief="groove", command=create.destroy).grid(row=3,column=2,padx=2, sticky=W)