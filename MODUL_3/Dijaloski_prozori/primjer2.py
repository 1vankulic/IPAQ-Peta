from tkinter import*
from tkinter.messagebox import*

def poruka():
    if askyesno('', 'Pada li danas kisa?'):
        showinfo('', ':(')
    else:
        showinfo('', ':)')
    return

t = Tk()
t.config(width=300, height=200)
g = Button(t, text='Ptanje dana', command=poruka)
g.place(x=100, y=100)
t.mainloop()