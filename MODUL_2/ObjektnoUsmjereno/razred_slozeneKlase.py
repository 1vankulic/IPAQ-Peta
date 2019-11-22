class Ucenik:
    def __init__(self, ime, prezime):
        self.Im = ime
        self.Pr = prezime
        return

    def __repr__(self):
        i = ' ' * (20 - len(self.Im)) + self.Im
        p = ' ' * (20 - len(self.Pr)) + self.Pr
        return i + p

class Razred:
    def __init__(self, oznaka):
        self.Oz = oznaka
        self.Uc = []
        return

    def dodaj_Ucenika(self, uc):
        self.Uc.append(uc)
        return

    def __str__(self):
        s = 'Razred: ' + self.Oz + '\n'
        s += '=' * 52 + '\n'

r = Razred('2B')
u = Ucenik('Pero', 'Perić')
r.dodaj_Ucenika(u)

print(r)


