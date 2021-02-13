import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except ModuleNotFoundError:
    pass


class HelloWorld(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Hello, World!')
        ttk.Label(self, text='Hello, World!').pack()


if __name__ == '__main__':
    root = HelloWorld()
    root.mainloop()
