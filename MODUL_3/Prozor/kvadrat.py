from tkinter import *

def p():
    povrsina_kvadrata = int(stranica.get()) * int(stranica.get()) 
    text2 = Label(t, text='P=' + str(povrsina_kvadrata))
    text2.place(x=100, y=150)
    return

def o():
    opseg = 4 * int(stranica.get()) 
    text2 = Label(t, text='O=' + str(opseg))
    text2.place(x=150, y=150)
    return




t = Tk()
t.config(width=500, height=500)

text = Label(t, text='Unesi duljinu straince kvadrata: ')
text.place(x=0, y=10)

stranica = Entry(t)
stranica.place(x=0,y=50)

povrsina = Button(text='Povrsina', command=p)
povrsina.place(x=0, y=100)

opseg = Button(text='Opseg', command=o)
opseg.place(x=50, y=100)


t.mainloop()