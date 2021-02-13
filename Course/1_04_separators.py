import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except ModuleNotFoundError:
    pass

root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Widget Examples')

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

ttk.Label(root, text='Hello, World!', padding=20).pack()

ttk.Separator(root, orient='horizontal').pack(fill='x')

ttk.Label(root, text='Hello, World!', padding=20).pack()

root.mainloop()


