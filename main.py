from Tkinter import *
import sys, os
import tkFont
top = Tk()

#Fonts Settings
headfont = tkFont.Font(family="Helvetica", size=24)

#Title
head = Label(top, text = "Presburn \n \n \n", font=headfont)
head.pack()
top.title("Presburn")

top.mainloop()
