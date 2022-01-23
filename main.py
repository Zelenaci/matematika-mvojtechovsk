#!/usr/bin/env python3

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
        self.lblVysl.grid(row=2,column=1)
        self.generuj()
        self.entry = Entry(self,width = 6)
        self.entry.grid(row=1,column = 2)
        self.btn = tk.Button(self, text="Konec", command=self.quit)
        self.btn.grid(row=5,column=1)
        #self.btnSummary = Button(self, text=u"Vyhodnocení", width=10, command=self.summary, font="ArialNarrow 10")
        #self.btnSummary.grid(row=4,column=1)
        self.bind('<Return>', self.kontrola)
        self.spravne = 0
        self.spatne = 0
          
        
 
    
    def summary(self):
        win = Tk()
        win.geometry("200x200")
        lbl1 = tk.Label(self, text= self.spravne)
        lbl1.grid(row=1,column=1)
        lbl2 = tk.Label(self, text= self.spravne)
        lbl2.grid(row=2,column=1)

    def kontrola(self,event):
        try:
            if int(self.entry.get()) == self.vysledek:
                self.lblVysl.config(text="SPRÁVNĚ",background = "#7CFC00")
                self.spravne +=1 
            else:
                self.lblVysl.config(text="ŠPATNĚ", background = "#FF0000")
                self.spatne+=1
            self.generuj()
            self.entry.delete(0, END)
        except ValueError:
            return
            


    def generuj(self):
        self.funkce = random.choice([self.plus,self.deleno,self.minus,self.krat])
        self.priklad = self.funkce()
        self.lbl.config(text= self.priklad)
        self.lbl.grid(row=1,column=1)
        
    def plus(self):
        self.cisloA = random.randint(1, 99)
        self.cisloB = random.randint(1, 100-self.cisloA) 
        self.vysledek = self.cisloA + self.cisloB
        self.znamenko = " + "
        return f"{self.cisloA}{self.znamenko}{self.cisloB} = "
   
    def deleno(self):
        self.cisloA = random.randint(1, 10)
        self.vysledek =random.randint(1, 10)
        self.cisloB = self.cisloA * self.vysledek
        self.znamenko = " / "
        return f"{self.cisloB}{self.znamenko}{self.cisloA} = "

    def minus(self):
        self.cisloA = random.randint(1, 99)
        self.cisloB = random.randint(1, self.cisloA) 
        self.vysledek = self.cisloA - self.cisloB
        self.znamenko = " - "
        return f"{self.cisloA}{self.znamenko}{self.cisloB} = "

    def krat(self):
        self.cisloA = random.randint(1, 10)
        self.cisloB = random.randint(1, 10) 
        self.vysledek = self.cisloA * self.cisloB
        self.znamenko = " * "
        return f"{self.cisloA}{self.znamenko}{self.cisloB} = "  

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
