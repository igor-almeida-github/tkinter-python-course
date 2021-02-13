import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry('600x400')  # Inicial
root.minsize(400, 200)  # Mínimo
'''
rectangle_1 = tk.Label(root, text='Rectangle 1', bg='green', fg='white')
rectangle_1.pack(ipadx=10, ipady=10)
# rectangle_1.pack(ipadx=10, ipady=10, fill='x')
# rectangle_1.pack(ipadx=10, ipady=10, fill='y', expand=True)
# rectangle_1.pack(ipadx=10, ipady=10, fill='both', expand=True)
# rectangle_1.pack(ipadx=10, ipady=10, expand=True)  # Se expande sem preencher
# rectangle_1.pack(side='left', ipadx=10, ipady=10, fill='both')
rectangle_1.pack(side='left', ipadx=10, ipady=10, fill='both', expand=True)

rectangle_2 = tk.Label(root, text='Rectangle 2', bg='red', fg='white')
rectangle_2.pack(ipadx=10, ipady=10)
# rectangle_2.pack(ipadx=10, ipady=10, expand=True)  # Se expande sem preencher
# rectangle_2.pack(side='top', ipadx=10, ipady=10, fill='both')
rectangle_2.pack(side='top', ipadx=10, ipady=10, fill='both', expand=True)
'''

rectangle_1 = tk.Label(root, text='Rectangle 1', bg='green', fg='white')
rectangle_1.pack(side='left', ipadx=10, ipady=10, fill='both', expand=True)

rectangle_2 = tk.Label(root, text='Rectangle 2', bg='red', fg='white')
rectangle_2.pack(side='top', ipadx=10, ipady=10, fill='both', expand=True)

rectangle_3 = tk.Label(root, text='Rectangle 3', bg='black', fg='white')
rectangle_3.pack(side='left', ipadx=10, ipady=10, fill='both', expand=True)

root.mainloop()