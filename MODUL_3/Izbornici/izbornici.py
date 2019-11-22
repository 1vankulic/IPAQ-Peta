# add_command(opcije) = dodaje stavke izbornika
# add_cascade(opcije) = stvara novi hijerarhijski izbornik povezivanjem zadanog izbornika s glavnim ozbornikom
# add_separator() = dodaje liniju odvajanje u izborniku

from tkinter import *

# funkcija koja ce se izvesti kada kliknemo na neki podizbornik

def ispis():
    t1 = Tk()
    button = Button(t1, text="Proba")
    button.pack()
    return

t = Tk() # Otvaranje prozora

izbornik = Menu(t) # Defininiranje gl.izbornika u prozoru
datoteka_izbornik = Menu(izbornik) # Definiiranje izbornika Datoteka
datoteka_izbornik.add_command(label="Kreiraj novu", command=ispis)
datoteka_izbornik.add_command(label="Otvori postojecu", command=ispis)
# povezuje sadrzaj ibornika datoteka s glavnim izbornikom
izbornik.add_cascade(label="Datoteka", menu=datoteka_izbornik)

uredi_izbornik = Menu(izbornik)
uredi_izbornik.add_command(label="Izrezi", command=ispis)
uredi_izbornik.add_command(label="Kopiraj", command=ispis)
#povezuje sadrzaj izbornika Uredi s glanim izbornikom
izbornik.add_cascade(label="Uredi", menu=uredi_izbornik)

t.config(menu=izbornik) #konfiguracija prozora
t.mainloop()












t.config(menu=izbornik)
t.mainloop()