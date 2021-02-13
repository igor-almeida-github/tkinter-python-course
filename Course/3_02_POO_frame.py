import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except ModuleNotFoundError:
    pass


class UserInputFrame(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)
        self.user_input = tk.StringVar()
        label = ttk.Label(self, text="Enter you name: ")
        entry = ttk.Entry(self, textvariable=self.user_input)
        button = ttk.Button(self, command=self.greet)

        label.pack(side='left')
        entry.pack(side='left')
        button.pack(side='left')

    def greet(self):
        print(f'Hello, {self.user_input.get()}')


if __name__ == '__main__':
    root = tk.Tk()
    frame = UserInputFrame(root)
    frame.pack()
    root.mainloop()

