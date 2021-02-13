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
root.resizable(False, False)
root.title('Greeater')
root.columnconfigure(0, weight=1)

style = ttk.Style(root)

print(style.theme_names())
print(style.theme_use('clam'))

main = ttk.Frame(root, padding=(40, 20))
main.grid()

user_name = tk.StringVar()

name_label = ttk.Label(main, text='Name: ')
name_label.grid(row=0, column=0, padx=(0, 10))
name_entry = ttk.Entry(main, width=25, textvariable=user_name)
name_entry.grid(row=0, column=1, padx=(10, 0))
name_entry.focus()

greet_button = ttk.Button(main, text='Greet', command=greet)
greet_button.grid(row=0, column=2, sticky='EW')

root.mainloop()

