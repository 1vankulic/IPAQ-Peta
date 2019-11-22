from tkinter import*
from tkinter.messagebox import*

def zivotinja():
    if var.get()==2:
        showinfo('', 'Tocno :)')
    else:
        showinfo('', 'Netocno :(')
    return

t = Tk()
var = IntVar()

L1 = Label(t, text='Koja zivotnja leti?')
L1.pack()

R1 = Radiobutton(t, text='Slon', variable=var, value=1, command=zivotinja)
R1.pack()

R2 = Radiobutton(t, text='Vrabac', variable=var, value=2, command=zivotinja)
R2.pack()

R3 = Radiobutton(t, text='Aligator', variable=var, value=3, command=zivotinja)
R3.pack()

t.mainloop()
