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

storage_variable = tk.StringVar()
storage_variable.set('First option')

option_one = ttk.Radiobutton(
    root,
    text='Option 1',
    variable=storage_variable,
    value='First option',
)

option_two = ttk.Radiobutton(
    root,
    text='Option 2',
    variable=storage_variable,
    value='Second option'
)

option_three = ttk.Radiobutton(
    root,
    text='Option 3',
    variable=storage_variable,
    value='Third option'
)

option_one.pack()
option_two.pack()
option_three.pack()


root.mainloop()



