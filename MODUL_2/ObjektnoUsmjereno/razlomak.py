class Razlomak:
    def __init__(self, b = 0, n = 1):
        self.B = b
        self.N = n
        self.krati()
        return

    def krati(self):
        b = self.B
        n = self.N
        
        while b != n:
            if b > n:
                b -= n
            else:
                n -= b

        self.B //= b
        self.N //= n
        return 


r = Razlomak(4, 6)

print(r.B)
