from Tkinter import *
import sys, os
import tkFont
top = Tk()
top.geometry('640x480+200+200')
#Fonts Settings
headfont = tkFont.Font(family="Helvetica", size=24)
headtwofont = tkFont.Font(family="Helvetica", size=18)
headlinetitle = tkFont.Font(family="Helvetica", size=14)

def main():
  #Title
  head = Label(top, text = "Presburn \n ", font=headfont)
  head.pack()
  top.title("Presburn")

  #News
  #ONLY ONE HEADLINE!
  hlines = Label(top, text = "Headlines \n ", font=headtwofont)
  hlines.pack()
  hlinesone = Label(top, text = "Headline One Title \n", font=headlinetitle)
  hlinesone.pack()
#Citizenship
def citizenship
  
top.mainloop()
