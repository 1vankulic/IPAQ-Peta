from tkinter import*

t = Tk()
t.config(bg = 'orange')
g = Label(t, text = 'Unesi broj', bg = 'pink')
g.place(x = 0, y = 0)
a = Entry(t, bg = 'green')
a.place(x = 0, y = 30)
t.mainloop()
