from tkinter import *
from tkinter import ttk

WIDTH = 68
HEIGHT = 50

def retornaCaracter(tecla):
    print(f"Han pulsado {tecla}")

def opera(num1, num2, operacion):
    if operacion == '+':
        try:
            return int(num1) + int(num2)
        except ValueError:
            return float(num1) + float(num2)
    elif operacion == '-':
        try:
            return int(num1) - int(num2)
        except ValueError:
            return round((float(num1)-float(num2)),2) 
    elif operacion == 'X':
        try:
            return int(int(num1) * int(num2))
        except ValueError:
            return round((float(num1)*float(num2)),2)
    else:
        try:
            return round(int(num1) / int(num2), 2)
        except ValueError:
            return round((float(num1)/float(num2)),2)

dbotones = [
    {
        'text': 'C',
        'r': 0,
        'c': 1,
        'style':'other.TButton'
    },
    {
        'text': '+/-',
        'r': 0,
        'c': 2,
        'style':'other.TButton'
    },
    {
        'text': '÷',
        'r': 0,
        'c': 3,
        'style':'op.TButton'
    },
    {
        'text': '7',
        'r': 1,
        'c': 0,
        'style':'num.TButton'
    },
    {
        'text': '8',
        'r': 1,
        'c': 1,
        'style':'num.TButton'
    },
    {
        'text': '9',
        'r': 1,
        'c': 2,
        'style':'num.TButton'
    },
    {
        'text': 'X',
        'r': 1,
        'c': 3,
        'style':'op.TButton'
    },
    {
        'text': '4',
        'r': 2,
        'c': 0,
        'style':'num.TButton'
    },
    {
        'text': '5',
        'r': 2,
        'c': 1,
        'style':'num.TButton'
    },
    {
        'text': '6',
        'r': 2,
        'c': 2,
        'style':'num.TButton'
    },
    {
        'text': '-',
        'r': 2,
        'c': 3,
        'style':'op.TButton'
    },
    {
        'text': '1',
        'r': 3,
        'c': 0,
        'style':'num.TButton'
    },
    {
        'text': '2',
        'r': 3,
        'c': 1,
        'style':'num.TButton'
    },
    {
        'text': '3',
        'r': 3,
        'c': 2,
        'style':'num.TButton'
    },
    {
        'text': '+',
        'r': 3,
        'c': 3,
        'style':'op.TButton'
    },
    {
        'text':'0',
        'r':4,
        'c':0,
        'w':2,
        'style':'num.TButton'
    },
    {
        'text': '.',
        'r': 4,
        'c': 2,
        'style':'num.TButton'
    },
    {
        'text': '=',
        'r': 4,
        'c': 3,
        'style':'op.TButton'
    },
    ]

class Display(ttk.Frame):
    
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT)
        self.pack_propagate(0)

        self.label = ttk.Label(self, text="0", anchor=E, background="black", 
            foreground="white", font="Helvetica 36")
        self.label.pack(side=TOP, fill=BOTH, expand=True)

    def refresh(self, text):
        self.label.config(text=text)

class CalcButton(ttk.Button):

    def __init__(self, parent, text, style, command=None, width=1, height=1):
        ttk.Frame.__init__(self, parent, width=WIDTH*width, height=HEIGHT*height)
        self.pack_propagate(0)
        
        ttk.Button(self, text=text, command=lambda:command(text), style=style).pack(side=TOP, fill=BOTH, expand=True)

class Keyboard(ttk.Frame):
    def __init__(self, parent, command):
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT*5)
        self.pack_propagate(0)
        self.__style_button()

        for boton in dbotones:
            w = boton.get('w', 1)
            h = boton.get('h', 1)

            btn = CalcButton(self, boton['text'], width=w, height=h, command=command, style=boton['style'])
            btn.grid(row=boton['r'], column=boton['c'], columnspan=w, rowspan=h)
    
    def __style_button(self):
        s = ttk.Style()
        s.theme_use('default')
        s.configure('.', font=('Helvetica', 18), foreground='white')
        s.configure('num.TButton', background='#B3AFAB')
        s.configure('op.TButton', background='#FF7E25')
        s.configure('other.TButton', background='#72706F')
        s.map('num.TButton',
            background=[('active', '#A4A19E'),
                        ('pressed', '#9C9996'),])
        s.map('op.TButton',
            background=[('active', '#FC7519'),])
        s.map('other.TButton',
            background=[('active', '#636261')])

class Calculator(ttk.Frame):

    valor1 = None
    valor2 = None
    r = None
    operador = ''
    cadena = ''

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT*6)
        self.pack_propagate(0)

        self.display = Display(self)
        self.display.pack(side=TOP, fill=BOTH, expand=True)

        self.teclado = Keyboard(self, self.gestiona_calculos)
        self.teclado.pack(side=TOP)

    def gestiona_calculos(self, tecla):
        
        if tecla.isdigit():
            if not (self.cadena == '' and tecla == '0'):
                self.cadena += tecla
                self.display.refresh(self.cadena)
        elif tecla in '+-X÷':
            if self.valor1 == None:
                if ',' in self.cadena:
                    self.cadena.replace(',', '.')
                self.valor1 = float(self.cadena) # <--- Antes era int(self.cadena)
                self.cadena = ''
                self.operador = tecla
            else:
                if not self.cadena:
                    return
                if ','  in self.cadena:
                    self.cadena.replace(',', '.')
                self.valor2 = float(self.cadena)
                self.r = self.calculate()
                self.display.refresh(self.r)
                self.valor1 = self.r
            self.cadena = ''
        elif tecla == '=':
            self.valor2 = float(self.cadena)
            self.r = self.calculate()
            self.display.refresh(self.r)
            self.valor1 = self.r
            self.cadena = ''
        elif tecla == 'C':
            self.valor1 = None
            self.valor2 = None
            self.r = 0
            self.operador = ''
            self.cadena = ''
            self.display.refresh('0')
        elif tecla == '.':
            if not self.cadena:
                self.cadena += '0.'
            elif tecla not in self.cadena:
                self.cadena += tecla

    def calculate(self):
        """
        self.valor1 = 12
        self.valor2 = 34
        self.operador = '+'
        """
        if self.operador == '+':
            if '.' in str(self.valor1) or '' in str(self.valor2):
                return round((self.valor1 + self.valor2), 4)
            else:
                return int(self.valor1+self.valor2)
        elif self.operador == '-':
            return round((self.valor1 - self.valor2), 4)
        elif self.operador == 'X':
            return round((self.valor1 * self.valor2), 4)
        else:
            return round((self.valor1 / self.valor2), 4)

    

       