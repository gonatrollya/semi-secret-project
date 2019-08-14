import sqlite3
from tkinter import *

def login_screen():
    global screen
    screen = Tk()
    screen.geometry("400x300")
    screen.title("Start")
    screen.configure(background='pink')
    Label(text = "Select",bg = "orange",fg = 'purple' ,width = "300", height = "2",font = ("Calibri", 13)).pack()
    Label(text = "",bg = 'green').pack()
    Button(text = "Spin Dice", height = "2" , width = "30").pack()
    Label(text = "",bg = 'yellow').pack()
    Button(text = "Create Character", height = "2" , width = "30").pack()
    Label(text = "",bg = 'darkgrey').pack()
    Button(text = "Select Campaign", height = "2" , width = "30").pack()
    Label(text = "",bg = 'purple').pack()
    Button(text = "Continue", height = "2" , width = "30" ).pack()
    screen.mainloop()


login_screen()
