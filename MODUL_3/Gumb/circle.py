from turtle import*
from tkinter import*

def Kruznica():
    turtle.circle(100)
    return

t = Tk()
t.config(width=200, height=200)

g = Button(t, text='Crtaj', command=Kruznica)
g.place(x=80, y=80)
t.mainloop()