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

# check_button = ttk.Checkbutton(root, text="Check me!")
# check_button.pack()
#
# check_button['state'] = 'disabled'  # Fica cinza e inacessivel. (normal) para ativar


def print_current_option():
    print(selected_option.get())


selected_option = tk.StringVar()

check_button = ttk.Checkbutton(
    root,
    text="Check example",
    variable=selected_option,
    command=print_current_option,
    onvalue="On",
    offvalue='Off'
)

check_button.pack()


root.mainloop()



