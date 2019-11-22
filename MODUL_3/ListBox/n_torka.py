# n-torke == tuple


from tkinter import*

def f1():
    k = Lb1.curselection()
    # u n-torki k (na mjestu indeksa 0) se nalazi samo 1 element (onaj oznaceni)
    # ako je to znak '1', odnosno Pcela onda je to tocan odgovor, inace je krivi
    if k[0] == '1':
        a3 = Label(t, text='Tocno!')
    else:
        a3 = Label(t, text='Krivo')
    a3.pack()
    return

t = Tk()
a1 = Label(t, text='Koja zivotinja leti')
a1.pack()
# naveden je mod za oznacavanje jedne stavke
Lb1 = Listbox(t, selectmode=SINGLE)
# dodavanje lemenata liste metodom inesrt()

Lb1.insert(0, "Mrav")
Lb1.insert(1, "Pcela")
Lb1.insert(2, "Slon")
Lb1.insert(3, "Piton")
Lb1.pack()

b = Button(t, text='Provjeri', command=f1)
b.pack()
t.mainloop()
