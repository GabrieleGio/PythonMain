d = {'pippo':2, 'pluto':1, 'topolino':5}
d2 = {}
#Modificare questa lista e farla diventare cosi':
#d2 = {'pippo': 0.25, 'pluto': 1/8, 'topolino': 5/8}


somma = sum(list(d.values()))
for chiave,valore in d.items():
    nuovo_valore = valore / somma
    d2[chiave] = nuovo_valore

print(d2)

#Esercizio 2
l = [1,2,3,4,5,2,2,6,3,7,16]
#Ottelnere l'output: d = {'somma_pari':32, 'somma_dispari':19}

d = {}
somma_pari = 0
somma_dispari = 0
pari = []
dispari = []
for n in range(l):
    if n % 2 == 0:
        somma_pari = somma_pari + n
    else:
        somma_dispari = somma_dispari + n
print(somma_pari)
print(somma_dispari)