import tkinter as tk
import tkinter.font as font
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except ModuleNotFoundError:
    pass

root = tk.Tk()
root.title('Distance Converter')

font.nametofont('TkDefaultFont').configure(size=15)

meters_value = tk.StringVar()
feet_value = tk.StringVar()


def calculate_feet(*args):
    try:
        meters = float(meters_value.get())
        feet = meters * 3.28084
        feet_value.set(f'{feet:.3g} pés')

    except ValueError:
        pass


main = ttk.Frame(root, padding=(30, 15))
main.grid()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

meters_label = ttk.Label(main, text='Metros: ')
meters_input = ttk.Entry(main, width=10, textvariable=meters_value, font=('Segoe UI', 15))
feet_label = ttk.Label(main, text='Pés:')
feet_display = ttk.Label(main, textvariable=feet_value)
calc_button = ttk.Button(main, text='Calcular', command=calculate_feet)

meters_label.grid(column=0, row=0, sticky='w')
meters_input.grid(column=1, row=0, sticky='ew')
meters_input.focus()

feet_label.grid(column=0, row=1, sticky='w')
feet_display.grid(column=1, row=1, sticky='ew')
calc_button.grid(column=0, row=2, columnspan=2, sticky='ew')

# Mudando todos os pads de uma vez, ao invés da forma anterior de definir um de cada vez
for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)

root.bind('<Return>', calculate_feet)
root.bind('<KP_Enter>', calculate_feet)  # Keypad


root.mainloop()

