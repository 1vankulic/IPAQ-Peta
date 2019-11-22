from tkinter import*

def zbroji():
    zbroj = int(prvi_broj.get()) + int(drugi_broj.get())
    rezultat = Label(t, text=str(zbroj))
    rezultat.place(x=200, y=300)
    return


t = Tk()
t.config(width= 1000, height= 1000)

# napravi ispis teksta
label1 = Label(t, text='Unesi prvi broj:')
label1.place(x=100, y=100)
prvi_broj = Entry(t)
prvi_broj.place(x=200, y=100)

label2 = Label(t, text='Unesi drugi broj:')
label2.place(x=100, y=125)
drugi_broj = Entry(t)
drugi_broj.place(x=200, y=125)

# napravi gumb; kilkom na gumb izvedi funkciju crtaj()
g = Button(text= 'Zbroji', command = zbroji)
g.place(x=150, y=200)

t.mainloop()


