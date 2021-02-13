import tkinter as tk
from tkinter import ttk
import tkinter.font as font

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except ModuleNotFoundError:
    pass

root = tk.Tk()
style = ttk.Style(root)
# style.configure('LargeEntry.TEntry', font=('Segoe UI', 15))

font.nametofont('TkDefaultFont').configure(size=15)
font.nametofont('TkTextFont').configure(size=15)  # Afeta os entry fields

name = ttk.Label(root, text='Hello, world!')
entry = ttk.Entry(root, width=15)  # style='LargeEntry.TEntry')
button = ttk.Button(root, text='Press me.')
name.pack()
entry.pack()
button.pack()

root.mainloop()


