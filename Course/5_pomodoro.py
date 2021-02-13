import tkinter as tk
from tkinter import ttk
from collections import deque
from frames import Timer, Settings

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except ModuleNotFoundError:
    pass

COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"


class PomodoroTimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Timer.TFrame", background=COLOUR_LIGHT_BACKGROUND)
        style.configure("Background.TFrame", background=COLOUR_PRIMARY)
        style.configure(
            "TimerText.TLabel",
            background=COLOUR_LIGHT_TEXT,
            foreground=COLOUR_DARK_TEXT,
            font="Courier 38"
        )
        style.configure(
            "LightText.TLabel",
            background=COLOUR_PRIMARY,
            foreground=COLOUR_LIGHT_TEXT,

        )
        style.configure(
            "PomodoroButton.TButton",
            background=COLOUR_SECONDARY,
            foreground=COLOUR_LIGHT_TEXT
        )
        style.configure(
            "PomodoroButton.TButton",
            background=COLOUR_SECONDARY,
            foreground=COLOUR_LIGHT_TEXT,

        )
        style.map(
            "PomodoroButton.TButton",
            background=[("active", COLOUR_PRIMARY), ("disabled", COLOUR_LIGHT_TEXT)]
        )
        self["background"] = COLOUR_PRIMARY
        self.title("Pomodoro Timer")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.__pomodoro = tk.StringVar(value=25)
        self.__long_break = tk.StringVar(value=15)
        self.__short_break = tk.StringVar(value=5)
        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        self.__timer_frame = Timer(self, self.__pomodoro, self.__long_break, self.__short_break, container)
        self.__timer_frame.grid(row=0, sticky="NSEW")
        self.__settings_frame = Settings(self, self.__pomodoro, self.__long_break, self.__short_break, container)
        self.__settings_frame.grid(row=0, sticky="NSEW")
        self.__timer_frame.tkraise()

    def show_time_frame(self):
        self.__timer_frame.tkraise()

    def show_settings_frame(self):
        self.__settings_frame.tkraise()


if __name__ == "__main__":
    root = PomodoroTimer()
    root.mainloop()
