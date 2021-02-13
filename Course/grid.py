import tkinter as tk
from tkinter import ttk

try:  # Melhora a resolução
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except ModuleNotFoundError:
    pass


def greet():
    print(f'Hello, {user_name.get() or "World"}.')


root = tk.Tk()
root.title('Greeater')
root.columnconfigure(0, weight=1)
user_name = tk.StringVar()


name_frame = ttk.Frame(root, padding=(20, 10, 20, 10))
name_frame.grid(sticky='W')

name_label = ttk.Label(name_frame, text='Name: ')
name_label.grid(row=0, column=0)  # Mesma coisa de não colocar, pois já são zero por padrão
name_entry = ttk.Entry(name_frame, width=25, textvariable=user_name)
name_entry.grid(row=0, column=1)
name_entry.focus()


button_frame = ttk.Frame(root, padding=(20, 0, 20, 10))
button_frame.grid(row=1, column=0, sticky='EW')
button_frame.columnconfigure((0, 1), weight=1)

greet_button = ttk.Button(button_frame, text='Greet', command=greet)
greet_button.grid(sticky='EW',  row=0, column=0)
quit_button = ttk.Button(button_frame, text='Quit', command=root.destroy)
quit_button.grid(sticky='EW', row=0, column=1)


root.mainloop()

