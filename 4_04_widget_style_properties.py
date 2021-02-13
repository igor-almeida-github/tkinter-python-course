import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except ModuleNotFoundError:
    pass

root = tk.Tk()

style = ttk.Style(root)

# OBS: Tudo que for feito com essa label se aplica a qualquer outro widget ttk

name = ttk.Label(root, text='Hello, world!')
name.pack()

print(style.layout('TLabel'))
print(style.element_options('Label.border'))
print(style.element_options('Label.padding'))
print(style.element_options('Label.label'))

# Descobrir o valor de propriedades
print(style.lookup('Tlabel', 'font'))
print(style.lookup('Tlabel', 'foreground'))
print(style.lookup('Tlabel', 'compound'))

style.theme_use('clam')

print(style.layout('TLabel'))
print(style.element_options('Label.border'))
print(style.element_options('Label.padding'))
print(style.element_options('Label.label'))

# Descobrir o valor de propriedades
print(style.lookup('Tlabel', 'font'))
print(style.lookup('Tlabel', 'foreground'))
print(style.lookup('Tlabel', 'compound'))

# Criando borda
style.configure('TLabel', bordercolor='#f00')
style.configure('TLabel', borderwidth=20)
style.configure('TLabel', relief='solid')

root.mainloop()















