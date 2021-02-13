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

value = tk.StringVar(value=1)
# tk.Label(root, textvariable=value).pack()

# scale = ttk.Scale(root, orient='horizontal', from_=0, to=1, variable=value)
scale = tk.Scale(root, orient='horizontal', from_=0, to=1, variable=value, resolution=0.05)
scale.pack()

# scale['state'] = 'disabled'

root.mainloop()




