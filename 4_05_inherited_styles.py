import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except ModuleNotFoundError:
    pass

root = tk.Tk()
style = ttk.Style(root)

style.configure("CustomEntryStyle.TEntry", padding=20)  # Não funciona para Entry por bug do tkinter

name = ttk.Label(root, text='Hello, world!')
entry = ttk.Entry(root, width=15)
entry['style'] = "CustomEntryStyle.TEntry"
name.pack()
entry.pack()

root.mainloop()



