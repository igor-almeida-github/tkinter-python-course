import tkinter as tk
import tkinter.font as font
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except ModuleNotFoundError:
    pass


class DistanceConverterRoot(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Distance Converter')
        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky='EW')
        frame_mf = MetersToFeetFrame(container, padding=(30, 15))
        frame_mf.grid(row=0, column=0)
        frame_fm = FeetToMetersFrame(container, padding=(30, 15))
        frame_fm.grid(row=1, column=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


class MetersToFeetFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.meters_value = tk.StringVar()
        self.feet_value = tk.StringVar()
        meters_label = ttk.Label(self, text='Metros: ')
        meters_input = ttk.Entry(self, width=10, textvariable=self.meters_value, font=('Segoe UI', 12))
        feet_label = ttk.Label(self, text='Pés:')
        feet_display = ttk.Label(self, textvariable=self.feet_value)
        calc_button = ttk.Button(self, text='Calcular', command=self.calculate_feet)
        meters_label.grid(column=0, row=0, sticky='w')
        meters_input.grid(column=1, row=0, sticky='ew')
        feet_label.grid(column=0, row=1, sticky='w')
        feet_display.grid(column=1, row=1, sticky='ew')
        calc_button.grid(column=0, row=2, columnspan=2, sticky='ew')
        meters_input.focus()
        meters_input.bind('<Return>', self.calculate_feet)
        meters_input.bind('<KP_Enter>', self.calculate_feet)
        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=12)

    def calculate_feet(self, *args):
        try:
            meters = float(self.meters_value.get())
            feet = meters * 3.28084
            self.feet_value.set(f'{feet:.5g} pés')

        except ValueError:
            pass


class FeetToMetersFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.meters_value = tk.StringVar()
        self.feet_value = tk.StringVar()
        feet_label = ttk.Label(self, text='Pés: ')
        feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value, font=('Segoe UI', 12))
        meters_label = ttk.Label(self, text='Metros:')
        meters_display = ttk.Label(self, textvariable=self.meters_value)
        calc_button = ttk.Button(self, text='Calcular', command=self.calculate_meters)
        feet_label.grid(column=0, row=0, sticky='w')
        feet_input.grid(column=1, row=0, sticky='ew')
        meters_label.grid(column=0, row=1, sticky='w')
        meters_display.grid(column=1, row=1, sticky='ew')
        calc_button.grid(column=0, row=2, columnspan=2, sticky='ew')
        feet_input.focus()
        feet_input.bind('<Return>', self.calculate_meters)
        feet_input.bind('<KP_Enter>', self.calculate_meters)
        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=12)

    def calculate_meters(self, *args):
        try:
            feet = float(self.feet_value.get())
            meters = feet / 3.28084
            self.meters_value.set(f'{meters:.5g} pés')

        except ValueError:
            pass


if __name__ == '__main__':
    root = DistanceConverterRoot()
    font.nametofont('TkDefaultFont').configure(size=12)
    root.mainloop()

