import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except ModuleNotFoundError:
    pass

root = tk.Tk()
style = ttk.Style(root)
style.theme_use('clam')
style.map(
    'CustomButton.TButton',
    foreground=[("pressed", "white"), ("active", "green")],
    background=[("pressed", "!disabled", "black"), ("active", "black")],  # Não faz nada em alguns temas
    font=[("pressed", ('TkDefaultFont', 11))]
)

name = ttk.Label(root, text='Hello, world!')
entry = ttk.Entry(root, width=15)
button = ttk.Button(root, text='Press me.', style='CustomButton.TButton')
name.pack()
entry.pack()
button.pack()

root.mainloop()
