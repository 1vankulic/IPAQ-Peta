# napisi program koji ce unosti prirodan broj n
# zatim listu od n cijelih brojeva
# Program treba ispisati sve pozitivne elemente liste

broj= int(input("Koliko brojeva zelis unijeti u listu: "))

lista = []
for i in range(broj):
    b = int(input(f"{i+1}. broj liste: "))
    lista.append(b)

pozitivni = []
for x in lista:
    if x > 0:
        pozitivni.append(x)

print(f"Pozitivni elementi liste su: {pozitivni}")