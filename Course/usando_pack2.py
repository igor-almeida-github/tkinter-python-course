import tkinter as tk
from tkinter import ttk


def greet():
    print(f'Hello, {user_name.get() or "World"}.')


root = tk.Tk()
user_name = tk.StringVar()


name_frame = ttk.Frame(root)
name_frame.pack(side='top', fill='x', padx=(20, 20), pady=(10, 10))  # Daria para inserir com padding

name_label = ttk.Label(name_frame, text='Name: ')
name_label.pack(side='left', padx=(0, 10))
name_entry = ttk.Entry(name_frame, width=25, textvariable=user_name)
name_entry.pack(side='left')
name_entry.focus()


button_frame = ttk.Frame(root)
button_frame.pack(side='top', fill='x', padx=(20, 20), pady=(0, 10))

greet_button = ttk.Button(button_frame, text='Greet', command=greet)
greet_button.pack(side='left', fill='x', expand=True)
quit_button = ttk.Button(button_frame, text='Quit', command=root.destroy)
quit_button.pack(side='left', fill='x', expand=True)


root.mainloop()