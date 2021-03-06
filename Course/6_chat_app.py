import tkinter as tk
from frames2.chat import Chat


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except ModuleNotFoundError:
    pass


class Messenger(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1200x500")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.__chat_frame = Chat(self)
        self.__chat_frame.grid(row=0, column=0, sticky="NSEW")


if __name__ == "__main__":
    root = Messenger()
    root.mainloop()
