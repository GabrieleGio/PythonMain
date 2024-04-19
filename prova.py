def rewrite_dict(d: dict[str, int]) -> dict[str, int]:
    somma = sum(d.values())
    out = {}
    for key in d:
        out[key] = d[key] / somma
    return out
#########################################################################################################
def substract(a: float,b:float):
    risultato: float = a-b
    return print(f"Il risultato di {a} - {b} è {risultato}")
a = 10
b = 5
substract(a,b)
print(substract(a,b))
#################################################################################################
#Questa funzione prende in input una lista di numeri reali e ne restituisce la mediana
def mediana(lista: list[float]):
    mediana = 0
    if len(lista) % 2 == 0:
        mediana = (lista[len(lista) // 2] + lista[(len(lista) // 2)-1]) / 2
        return mediana
    else:
        mediana = lista[len(lista) // 2]
        return mediana

l = [4,23,16,78,24,-12,23,15]
l2 = [3,4,5,6,7]
print(mediana(l))
print(mediana(l2))
#######################################################################################
def diff_cum(l: list[float]) -> float: 
    #l = [1,2,3,4,5,6]
    #deve restituire 1-2-3-4-5-6 = -qualcosa
    diff: float = l[0]
    for n in range (1,len(l)):
        diff -= l[n]
    return diff
l3 = [1,2,3,4,5,6]
print(diff_cum(l3))