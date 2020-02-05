#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk

root = Tk()

print("Python:", sys.version)
print("Tcl revision:", root.eval('info patchlevel'))

# Python: 3.8.1
# [Clang 6.0 (clang-600.0.57)]
# Tcl revision: 8.6.8

# ▶ tclsh
# % info patchlevel
# 8.6.9
