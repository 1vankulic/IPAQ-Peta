from tkinter import*
from tkinter.messagebox import*

def poruka():
    showinfo('Naslov', 'blablabla')
    return 



t = Tk()

t.config(width=300, height=200)
g = Button(t, text='Click me', command=poruka)
g.place(x=100, y=100)
t.mainloop()