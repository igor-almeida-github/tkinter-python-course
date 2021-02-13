import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except ModuleNotFoundError:
    pass

root = tk.Tk()
style = ttk.Style(root)

name = ttk.Label(root, text='Hello, world!')
entry = ttk.Entry(root, width=15)
name.pack()

print(name['style'])  # Se for padrão não mostra nada
print(name.winfo_class())

root.mainloop()




