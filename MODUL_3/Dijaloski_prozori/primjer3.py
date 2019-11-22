from tkinter import*
from tkinter.messagebox import *

def poruka():
    if askokcancel('', 'Kraj webinara?'):
        t.destroy()
    else:
        showinfo('', 'Dobar odabir')
    return

t = Tk()
t.config(width=300,height=200)
g=Button(t, text='Kako si?', command=poruka)
g.place(x=100,y=100)
t.mainloop()





















