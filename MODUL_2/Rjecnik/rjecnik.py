'''
rjecnik = {
    'imena': ['Ana', 'Marko'],
    'pi': 3.14159,
    'parni': [2, 4, 6, 8]
}

dict() # postavljanje novog rjecnika

'''

brojevi = {
    'parni': [2, 4, 6, 8, 10],
    'neparni': [3, 5, 7, 9]
}

for blabla in brojevi:
    print(blabla)

brojevi.update({
    'iracionalni': -1/5
})

# ispis rjecnika
for wtf in brojevi.items():
    print(f"Kljuc: {wtf[0]}, Vrijednost: {wtf[1]}")