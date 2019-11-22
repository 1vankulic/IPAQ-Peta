class Cetverokut:
    def __init__(self, a, b, c, d):
        self.A = a
        self.B = b
        self.C = c
        self.D = d
        return

    def opseg(self):
        return self.A + self.B + self.C + self.D

class Pravokutnik(Cetverokut):
    # Inheriting class Cetverokut
    def __init__(self, a, b):
        super().__init__(a, b, a, b)
        return

    def povrsina(self):
        return self.A * self.B

c = Cetverokut(3, 4, 5, 6)
d = Pravokutnik(3, 5)
e = Pravokutnik(3, 5, 6, 7)
print(c.opseg())
print(d.povrsina())