from tkinter import *
from tkinter import ttk

import calculator

class MainApp(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.title("Calculadora")
        self.geometry('270x300+600+150')
        self.resizable(0, 0)

        self.calculator = calculator.Calculator(self)
        self.calculator.pack()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()



        