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

'''
initial_value = tk.StringVar(value=20)
spin_box = ttk.Spinbox(root, from_=0, to=30, textvariable=initial_value, wrap=False)  # wrap = False - não reseta valores
spin_box.pack()
'''
# ciclando em valores específicos
initial_value = tk.StringVar(value=20)
spin_box = ttk.Spinbox(root, value=(10, 20, 30, 40), textvariable=initial_value, wrap=False)  # wrap = False - não reseta valores
spin_box.pack()

root.mainloop()



