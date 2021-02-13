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

programming_languages = ('C', 'Go', 'JavaScript', 'Perl', 'Python', 'Rust')

langs = tk.StringVar(value=programming_languages)

langs_select = tk.Listbox(root, listvariable=langs, height=6, selectmode='extended')
langs_select.pack()


def handle_selection_change(event):
    selected_indices = langs_select.curselection()
    print([langs_select.get(idx) for idx in selected_indices])


langs_select.bind('<<ListboxSelect>>', handle_selection_change)

root.mainloop()



