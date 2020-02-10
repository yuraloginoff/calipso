#!/usr/bin/env python3

import os
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox
from colors import *

APP_NAME = "Calipso"
_fileName = None

# create blank window
root = Tk()
root.title(APP_NAME)


# setting window size
root.geometry('640x480+0+0')
root.minsize(600, 300)
root.update()

mainframe = Frame(root)
mainframe['background'] = gray8
mainframe['padx'] = 10*root.winfo_width()/100
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# handling window resize
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


# Set padding on resize
def onResize(event):
    mainframe['padx'] = 10*root.winfo_width()/100


root.bind('<Configure>', onResize)

# Fonts
txtFont = font.Font(family='Avenir Next', size='20')

# create text widget
txt = Text(mainframe, wrap="word", padx=10, pady=10, font=txtFont)
txt.grid(column=0, row=0, sticky="nsew")
txt.focus()  # autofocus
txt['background'] = gray8
txt['foreground'] = gray2
txt['insertbackground'] = gray2  # text cursor
txt['highlightthickness'] = 0  # no widget border

txt.insert('1.0', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

# create scrollbar
scrollbar = Scrollbar(root, orient=VERTICAL, command=txt.yview)
scrollbar.grid(column=1, row=0, sticky=(N, S))
scrollbar['background'] = gray8
scrollbar['highlightthickness'] = 0
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


def openFile():
    filename = filedialog.askopenfilename()


def writeToFile(_fileName):
    try:
        content = txt.get(1.0, 'end')
        with open(_fileName, 'w') as theFile:
            theFile.write(content)
    except IOError:
        messagebox.showwarning("Save", "Could not save the file.")


def saveAs():
    filename = filedialog.asksaveasfilename(
        defaultextension='.txt',
        filetypes=[
            ('TXT (*.txt)', 'TXT'), ("All Files", "*.*")
        ])

    if filename:
        global _fileName
        _fileName = filename
        writeToFile(_fileName)
        root.title('{} - {}'.format(os.path.basename(_fileName), APP_NAME))
    return "break"


def save(event=None):
    global _fileName
    if not _fileName:
        saveAs()
    else:
        writeToFile(_fileName)
    return "break"


# menu_file.add_command(label='New', command=newFile)
# menu_file.add_command(label='Open', command=openFile)
menu_file.add_command(label='Save as', command=saveAs)
menu_file.add_command(label='Save', command=save)


root.mainloop()

# Retrieving the Text
# thetext = txt.get('1.0', 'end')
