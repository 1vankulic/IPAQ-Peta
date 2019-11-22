from tkinter import*
from tkinter.messagebox import*

def provjeri():
    if var1.get() == 1 and var2.get() == 0 and var3.get() == 1 and var4.get() == 0:
        showinfo('', 'Tocno :)')
    else:
        showinfo('', 'Netocno :(')
    return

t = Tk()

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

L1 = Label(t, text='Koje zivotnje zive u vodi')
L1.pack()

C1 = Checkbutton(t, text='Brancin', variable = var1)
C1.pack()
C2 = Checkbutton(t, text='Slon', variable = var2)
C2.pack()
C3 = Checkbutton(t, text='Kit', variable = var3)
C3.pack()
C4 = Checkbutton(t, text='Majmun', variable = var4)
C4.pack()

G1 = Button(t, text='Provjeri', command=provjeri)
G1.pack()

t.mainloop()