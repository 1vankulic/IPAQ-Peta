class Trokut:
    def __init__(self, a = 0, b = 0, c = 0):
        self.A = a
        self.B = b
        self.C = c
        return

    def opseg(self):
        return self.A + self.B + self.C

    def povrsina(self):
        s = self.opseg() / 2
        return (s * (s - self.A) * (s - self.B) * (s - self.C)) ** 0.5

# Calling a function
t = Trokut(3, 4, 5)
print(t.opseg())
print(t.povrsina())
