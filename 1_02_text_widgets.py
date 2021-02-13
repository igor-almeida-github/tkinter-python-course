import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except ModuleNotFoundError:
    pass


def print_text():
    text_content = text.get("1.0", "end")
    print(text_content)


root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Widget Examples')

text = tk.Text(root, height=8)
text.pack()

button = ttk.Button(root, text="Imprimir", command=print_text)
button.pack()

text.insert('1.0', 'Please enter a comment...')  # 1.0 é a primeira linha e primeira coluna ( não é 0.0 )
# text['state'] = 'disable'  # Desabilita a possibilidade de escrita na caixa de texto ('normal') para reativar

root.mainloop()


