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
print(font.families())

# warninge_label_font = font.Font(family='Helvetica', size=14, weight='bold')
warninge_label_font = font.nametofont('TkDefaultFont').copy()  # Se não tiver o copy, mudará tudo pois TkDefaultFont mudaria
warninge_label_font.configure(family='Helvetica', size=14, weight='bold')

name = ttk.Label(root, text='Hello, world!', font=warninge_label_font)
entry = ttk.Entry(root, width=15)
button = ttk.Button(root, text='Press me.')
name.pack()
entry.pack()
button.pack()

root.mainloop()
