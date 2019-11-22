'''
def ime_funkcije(popis_parametara):
    blok_naredbi
    return vrijednost
'''

# funkcija za ispisivanje parnost broja

bla = 3 

def parnost(broj):
    if broj % 2 == 0:
        print("Broj je paran")
    else: 
        print("Broj je neparan")

print(parnost(bla))

def prosjek(n):
    zbroj = 0
    for i in range(n):
        zbroj += i
    p = zbroj / n
    return p


