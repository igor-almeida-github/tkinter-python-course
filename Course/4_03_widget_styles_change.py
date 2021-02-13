import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except ModuleNotFoundError:
    pass

root = tk.Tk()
root.geometry('400x100')
style = ttk.Style(root)

name = ttk.Label(root, text='Hello, world!', style='CustomLabel')  # Assim que muda, se tivessemos o CustomStyle
entry = ttk.Entry(root, width=15)
name.pack()

# style.configure('TLabel', font=('Segoe UI', 20))

root.mainloop()



