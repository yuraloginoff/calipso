#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk

# create blank window
root = Tk()
root.title("Calipso")

# setting window size
root.geometry('640x480')

# handling window resize
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# create text widget
txt = Text(root, wrap="word")
txt.grid(column=0, row=0, sticky="nsew")

# create scrollbar
scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=txt.yview)
scrollbar.grid(column=1, row=0, sticky=(N, S))
# txt to communicate back to the scrollbar
txt['yscrollcommand'] = scrollbar.set

# set focus to text widget
txt.focus()

root.mainloop()
