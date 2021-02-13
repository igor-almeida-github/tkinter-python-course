import tkinter as tk
from tkinter import ttk


def greet():
    print(f'Hello, {user_name.get() or "World"}.')


root = tk.Tk()

user_name = tk.StringVar()

name_label = ttk.Label(root, text='Name: ')  # Pode-se colocar espaço após a label dessa forma
name_label.pack(side='left', padx=(0, 10))  # Ou então dessa forma

name_entry = ttk.Entry(root, width=25, textvariable=user_name)
name_entry.pack(side='left')
name_entry.focus()

greet_button = ttk.Button(root, text='Greet', command=greet)
greet_button.pack(side='left')

quit_button = ttk.Button(root, text='Quit', command=root.destroy)
quit_button.pack(side='right')

root.mainloop()
