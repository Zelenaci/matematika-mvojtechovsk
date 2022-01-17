#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import *
import random
# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Matematika"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Matematika")
        self.lbl.pack()
        self.generuj()
        self.entry = Entry(self,width = 6)
        self.entry.pack()
        #self.entry.grid(row=2,column = 3)
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        


    def generuj(self):
        self.funkce = random.choice([self.plus, self.deleno, self.krat, self.minus])
        self.label = Label(self, text=1)
        self.label.pack(LEFT)

    def plus(self):
        self.cisloA = random.randint(1, 99)
        self.cisloB = random.randint(1, 100-self.cisloA) 
        self.vysledek = self.cisloA + self.cisloB
        self.lbl.config(text="+")

    def deleno(self):
        self.cisloA = random.randint(1, 10)
        self.vysledek =random.randint(1, 10)
        self.cisloB = self.cisloB * self.vysledek
        self.lbl.config(text="/")
    def minus(self):
        self.cisloA = random.randint(1, 99)
        self.cisloB = random.randint(1, self.cisloA) 
        self.vysledek = self.cisloA - self.cisloB
        self.lbl.config(text="-")

    def krat(self):
        self.cisloA = random.randint(1, 10)
        self.cisloB = random.randint(1, 10) 
        self.vysledek = self.cisloA * self.cisloB
        self.lbl.config(text="*")   

    def about(self):
        window = About(self)
        window.grab_set()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
