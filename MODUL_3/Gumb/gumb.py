# Button(ime_objekta, parametri)

from tkinter import *

t = Tk()
t.config(
    width = 300,
    height = 300,
    bg = 'yellow'
)
g = Button(t, 
    text = 'Crtaj',
    bg = 'yellow',
    fg = 'blue'
)
g.place(x = 10, y = 50, width = 100, height = 30)
t.mainloop()