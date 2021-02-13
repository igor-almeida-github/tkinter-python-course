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

selected_weekday = tk.StringVar()
weekday = ttk.Combobox(root, textvariable=selected_weekday)
weekday['values'] = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
# weekday['state'] = 'readonly'
weekday.pack()


def handle_selection(event):
    print('Today is', selected_weekday.get())
    print("But we're gonna change it to Friday.")
    selected_weekday.set("Friday")
    print(weekday.get())


weekday.bind('<<ComboboxSelected>>', handle_selection)

root.mainloop()

print(selected_weekday.get())
