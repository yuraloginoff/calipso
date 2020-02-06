#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk
# import tkinter.tkFileDialog
from tkinter import font


# create blank window
root = Tk()
root.title("Calipso")

# setting window size
root.geometry('640x480')

mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# handling window resize
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


# Fonts
txtFont = font.Font(family='Avenir Next', size='20')

# create text widget
txt = Text(mainframe, wrap="word", padx=10, pady=6, font=txtFont)
txt.grid(column=0, row=0, sticky="nsew")
txt.focus()  # autofocus


txt.insert('1.0', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')


# create scrollbar
scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=txt.yview)
scrollbar.grid(column=1, row=0, sticky=(N, S))
# txt to communicate back to the scrollbar
txt['yscrollcommand'] = scrollbar.set

# create menus
root.option_add('*tearOff', FALSE)
menubar = Menu(root)
root['menu'] = menubar

menu_file = Menu(menubar)
menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_edit, label='Edit')


def newFile():
    print('new file')


def save_as():
    print('new file')


menu_file.add_command(label='New', command=newFile)
menu_file.add_command(label='Save as', command=save_as)
# menu_file.add_command(label='Close', command=closeFile)


root.mainloop()

# Retrieving the Text
# thetext = txt.get('1.0', 'end')
