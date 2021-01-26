from tkinter import *
from tkinter import ttk

root = Tk()

s = ttk.Style()
s.theme_use('default')

s.configure('Wild.TButton',
    background='black',
    foreground='white',
    highlightthickness='20',
    font=('Helvetica', 18, 'bold'))

s.map('Wild.TButton',
    foreground=[('disabled', 'yellow'),
                ('pressed', 'red'),
                ('active', 'blue')],
    background=[('disabled', 'magenta'),
                ('pressed', 'cyan'),
                ('active', 'green')],
    highlightcolor=[('focus', 'green'),
                    ('!focus', 'red')],
    relief=[('pressed', 'groove'),
            ('!pressed', 'ridge')])

ttk.Button(root, text="Hola", style="Wild.TButton").pack()
ttk.Button(root, text='Adios').pack()


root.mainloop()

