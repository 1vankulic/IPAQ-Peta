from tkinter import*
from turtle import*

def crtaj():
    r = int(b.get())
    fillcolor('green')
    begin_fill()
    circle(r)
    end_fill()
    return

t = Tk()
t.config(width= 300, height= 200)

# napravi ispis teksta
a = Label(t, text='Unesi radijus:')
a.place(x= 30, y= 50)

# napravi polje za unos teksta
b = Entry(t)
b.place(x= 30, y=100)

# napravi gumb; kilkom na gumb izvedi funkciju crtaj()
g = Button(text= 'Crtaj', command = crtaj)
g.place(x= 30, y=150)

mainloop()

