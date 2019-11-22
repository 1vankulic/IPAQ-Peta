# Algoritam zbrajanje prvih n prirodnih brojeva
# Napiši program koji će unositi prirodan broj n te ispisati zbroj svih brojeva do n.

n = int(input("Unesi prirodan broj: "))
x = int(input("Unesi broj do kojeg zelis zbrojiti sve brojeve izmedu: "))

y = 0

for n in range(x+1):
    y += n

print(y)
