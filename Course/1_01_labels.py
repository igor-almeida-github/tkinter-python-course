import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except ModuleNotFoundError:
    pass


root = tk.Tk()
root.title('Greeater')
root.geometry('600x400')
root.resizable(False, False)
root.title('Widget Examples')

# Configurando fonte da Label
'''
label = ttk.Label(root, text='Hello, world!', padding=20)
label.config(font=('Times New Roman', 20))
label.pack()
'''

# Imagem
'''
image = Image.open('logo.jpg')
image = image.resize((243, 149))
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image=photo, padding=5)
label.pack()

label['image'] = photo  # Trocaria a imagem, se photo fosse outra.
'''

# Imagem e texto
'''
image = Image.open('logo.jpg')
image = image.resize((243, 149))
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, text='Texto na imagem', image=photo, padding=5, compound='left', font=("Courier", 12))
label.pack()
'''

# Mudar o texto sobre label de modo dinâmico
greeting = tk.StringVar()

label = ttk.Label(root, padding=10, textvariable=greeting)
label.pack()

greeting.set('Hello, Igor!')

root.mainloop()




