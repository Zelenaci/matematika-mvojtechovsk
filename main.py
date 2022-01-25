from os.path import basename, splitext
import re
from select import select
import tkinter as tk
from tkinter import *
import random
from turtle import color
# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Matematika"


    def __init__(self):
        
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Matematika")
        self.lbl.grid(row=0)
        self.lblVysl = tk.Label(self, text="")
        self.lblVysl.grid(row=3,column=2)
        self.generuj()
        self.entry = Entry(self,width = 6)
        self.entry.grid(row=2,column =3)
        self.bind('<Return>', self.kontrola)
        self.btn = tk.Button(self, text="Konec", command=self.quit)
        self.btn.grid(row=5,column=2)
        self.spravne = 0
        self.spatne = 0
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.lbl1 = tk.Label(self, textvariable= self.var1)
        self.lbl1.grid(row=4,column=1)
        self.lbl2 = tk.Label(self, textvariable= self.var2)
        self.lbl2.grid(row=4,column=2)
             
        
 
    


    def kontrola(self,event):
        try:
            if int(self.entry.get()) == self.vysledek:
                self.lblVysl.config(text="SPRÁVNĚ",background = "#7CFC00")
                self.spravne +=1
                self.var1.set(self.spravne)
               
            else:
                self.lblVysl.config(text="ŠPATNĚ", background = "#FF0000")
                self.spatne+=1
                self.var2.set(self.spatne)
                
            self.generuj()
            self.entry.delete(0, END)
        except ValueError:
            return
            


    def generuj(self):
        self.funkce = random.choice([self.plus,self.deleno,self.minus,self.krat])
        self.priklad = self.funkce()
        self.lbl.config(text= self.priklad)
        self.lbl.grid(row=2,column=2)
        
    def plus(self):
        self.cisloA = random.randint(1, 99)
        self.cisloB = random.randint(1, 100-self.cisloA) 
        self.vysledek = self.cisloA + self.cisloB
        self.znamenko = " + "
        return f"{self.cisloA}{self.znamenko}{self.cisloB} ="
   
    def deleno(self):
        self.cisloA = random.randint(1, 10)
        self.vysledek =random.randint(1, 10)
        self.cisloB = self.cisloA * self.vysledek
        self.znamenko = " / "
        return f"{self.cisloB}{self.znamenko}{self.cisloA} ="

    def minus(self):
        self.cisloA = random.randint(1, 99)
        self.cisloB = random.randint(1, self.cisloA) 
        self.vysledek = self.cisloA - self.cisloB
        self.znamenko = " - "
        return f"{self.cisloA}{self.znamenko}{self.cisloB} ="

    def krat(self):
        self.cisloA = random.randint(1, 10)
        self.cisloB = random.randint(1, 10) 
        self.vysledek = self.cisloA * self.cisloB
        self.znamenko = " * "
        return f"{self.cisloA}{self.znamenko}{self.cisloB} ="  

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()